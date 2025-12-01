from database import usuarios_collection, produtos_collection, ObjectId

def deletar_favorito():
    usuario_id = input("Digite o ID do usuário: ")
    produto_id = input("Digite o ID do produto a ser desfavoritado: ")

    if usuario_id == '' or produto_id == '':
        print("ID do usuário e do produto são obrigatórios!")
        return
    
    try:
        produto_id = ObjectId(produto_id)
    except Exception as e:
        print("ID do produto inválido!")
        return
    
    produto = produtos_collection.find_one({'_id': produto_id})
    if not produto:
        print("Produto não encontrado!")
        return
    
    usuarios_collection.update_one(
        {'_id': ObjectId(usuario_id)},
        {'$pull': {'favoritos': {'_id': produto_id}}}
    )
    print(f"Produto {produto_id} desfavoritado pelo usuário {usuario_id}.")
