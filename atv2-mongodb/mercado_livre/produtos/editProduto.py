from database import produtos_collection, ObjectId

def atualizar_produto():
    produto_id = input("Digite o ID do produto que deseja atualizar: ")
    nome = input("Novo nome do produto: ")
    preco = float(input("Novo preço do produto: "))
    produtos_collection.update_one(
        {'_id': ObjectId(produto_id)},
        {'$set': {'nome': nome, 'preco': preco}}
    )
    print(f"Produto {produto_id} atualizado com sucesso!")