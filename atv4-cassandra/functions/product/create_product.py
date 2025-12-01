from uuid import uuid4, UUID
from utils.utils_seller import get_seller
from utils.cassandra_conversor import convert_row_pydict_seller

def create_product(session, seller_id):
    try:
        product_id = uuid4()

        print("_" * 50)
        print("Cadastro do Produto")
        print("_" * 50)

        seller = get_seller(session, UUID(seller_id))
        if seller is None:
            print("Vendedor não encontrado!")
            return

        nome_produto = input("Nome do Produto: ")
        marca_produto = input("Marca do Produto: ")
        preco_produto = float(input("Preço do Produto: "))
        print("_" * 50)

        seller_dict = convert_row_pydict_seller(seller)

        produto = {
            "id": product_id,
            "nome": nome_produto,
            "marca": marca_produto,
            "preco": preco_produto,
            "vendedor_id": UUID(seller_id),
            "vendedor_nome": seller.nome,
            "vendedor_email": seller.email,
            "cnpj_vendedor": seller.cnpj,
        }

        produto_map = {
            "id": str(produto["id"]),
            "nome": produto["nome"],
            "marca": produto["marca"],
            "preco": str(produto["preco"]),
            "vendedor_id": str(produto["vendedor_id"]),
            "vendedor_nome": produto["vendedor_nome"],
            "vendedor_email": produto["vendedor_email"],
            "cnpj_vendedor": produto["cnpj_vendedor"],
        }

        produtos = seller_dict['produtos']
        produtos.append(produto_map)

        script_insert_product = """
            INSERT INTO products (id, nome, marca, preco, vendedor_id, vendedor_nome, vendedor_email, cnpj_vendedor)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        session.execute(
            script_insert_product,
            (
                produto["id"],
                produto["nome"],
                produto["marca"],
                produto["preco"],
                produto["vendedor_id"],
                produto["vendedor_nome"],
                produto["vendedor_email"],
                produto["cnpj_vendedor"],
            )
        )
        print("Produto cadastrado com sucesso!")

        script_update_seller = """
            UPDATE seller
            SET produtos = %s
            WHERE id = %s
        """
        session.execute(script_update_seller, (produtos, UUID(seller_id)))
        print(f"Produto '{nome_produto}' adicionado à lista de produtos do vendedor com sucesso!")
        
        return

    except Exception as e:
        print(f"Erro ao registrar produto: {e}")
        return None
