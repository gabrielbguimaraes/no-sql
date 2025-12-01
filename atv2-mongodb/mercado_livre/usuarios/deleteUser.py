from database import usuarios_collection, ObjectId

def deletar_usuario():
    usuario_id = input("Digite o ID do usuário que deseja excluir: ")
    if usuario_id == '':
        print("ID do usuário é obrigatório!")
        return
    usuarios_collection.delete_one({'_id': ObjectId(usuario_id)})
    print(f"Usuário {usuario_id} excluído com sucesso!")