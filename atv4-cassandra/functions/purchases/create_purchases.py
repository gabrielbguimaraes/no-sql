from uuid import uuid4, UUID
from datetime import datetime
from utils.utils_product import get_product, list_products
from utils.utils_users import get_user
from utils.cassandra_conversor import convert_row_pydict_user

def create_purchase(session, user_id):
    try:
        purchase_id = uuid4()
        
        print("_" * 50)
        print("Compra de Produtos")
        print("_" * 50)

        user = get_user(session, UUID(user_id))
        if user is None:
            print("Usuário não encontrado")
            return
        
        user_dict = convert_row_pydict_user(user)

        products = list_products(session)
        if not products:
            print("Nenhum produto cadastrado")
            return
        
        productss = []

        while True:
            print("_" * 50)
            product_id = input("ID do Produto: ")
            
            product = get_product(session, UUID(product_id))
            if product is None:
                print("Produto não encontrado")
                continue

            productss.append({
                "produto_id": str(product.id),
                "nome": str(product.nome),
            })

            if input("Deseja adicionar outro endereço? (s/n): ").lower() == "n":
                break

        print("_" * 50)
        print("Endereço de Entrega")
        print("_" * 50)

        enderecos = user_dict.get("enderecos", [])
        if not enderecos:
            print("Nenhum endereço cadastrado")
            return
        
        for i, endereco in enumerate(enderecos, start=1):
            print(f"{i} - {endereco['rua']} {endereco['numero']}, {endereco['complemento']}, {endereco['cidade']} - {endereco['estado']}")

        try:
            index = int(input("Escolha um endereço: / 0 - Cancelar: "))
            if 0 < index <= len(enderecos):
                endereco_ent = dict(enderecos[index - 1])
            else:
                print("Endereço não encontrado")
                return
        except ValueError:
            print("Endereço não encontrado")
            return
        
        data = datetime.now()

        script = """
            INSERT INTO purchase (id, user_id, produtos, entrega_final, data)
            VALUES (%s, %s, %s, %s, %s)
        """

        endereco_dict = {
            "rua": endereco_ent["rua"],
            "numero": endereco_ent["numero"],
            "complemento": endereco_ent["complemento"],
            "cep": endereco_ent["cep"],
            "cidade": endereco_ent["cidade"],
            "estado": endereco_ent["estado"],
            "pais": endereco_ent["pais"],
        }

        session.execute(script, (purchase_id, UUID(user_id), productss, endereco_dict, data))

        print("Compra realizada com sucesso! Código da Compra:", purchase_id)

        compra_dict = {
            "id": str(purchase_id),
            "data": data.isoformat(),
        }

        compras = user_dict['compras'] if user_dict.get('compras') else []
        compras.append(compra_dict)

        script_update_user = """
            UPDATE user
            SET compras = %s
            WHERE id = %s
        """

        session.execute(script_update_user, (compras, UUID(user_id)))

    except Exception as e:
        print(f"An error occurred: {e}")

        

            
