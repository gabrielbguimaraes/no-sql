from database import produtos_collection, ObjectId

def deletar_produto():
    produto_id = input("Digite o ID do produto que deseja excluir: ")
    produtos_collection.delete_one({'_id': ObjectId(produto_id)})
    print(f"Produto {produto_id} excluído com sucesso!")