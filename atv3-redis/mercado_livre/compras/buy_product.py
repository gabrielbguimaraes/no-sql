import json
from bson import ObjectId
from utils.utils import list_products, find_product
from auth import user_logged
import uuid

def buy_product(produtos_collection, db_redis, user, compras_collection):
    if not user or '_id' not in user:
        print("Erro: Usuário não autenticado corretamente.")
        return

    user_email = user['email']
    if not user_logged(db_redis, user_email):
        print("Erro: Usuário não está logado.")
        return
    
    list_products(produtos_collection)

    compras = []
    while True:
        product_id = input("Digite o ID do produto que deseja comprar: ")
        product = find_product(product_id, produtos_collection)
        if not product:
            print("Produto não encontrado!")
            continue

        compras.append({"product": product})

        continue_process = input("Deseja selecionar mais algum produto? (S/N) ").lower()
        if continue_process == "n":
            break

    # Formata a lista de compras
    lista_compras = [{"id_produto": str(item["product"]["_id"]),
                      "nome": item["product"]["nome"],
                      "preco": item["product"]["preco"]} for item in compras]

    id_compra = str(uuid.uuid4())
    nova_compra = {
        'id_compra': id_compra,
        'id_usuario': str(user['_id']),
        'produtos': lista_compras  # Este campo é uma lista e precisa ser serializado
    }

    compra_key = f"compra:{id_compra}"
    db_redis.hset(compra_key, mapping={
        key: json.dumps(value) if isinstance(value, (list, dict)) else value
        for key, value in nova_compra.items()
    })
    print("Compra adicionada ao Redis com sucesso!")
