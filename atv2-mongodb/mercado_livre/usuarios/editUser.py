from database import usuarios_collection, ObjectId

def atualizar_usuario():
    usuario_id = input("Digite o ID do usuário que deseja atualizar: ")
    nome = input("Novo nome do usuário: ")
    email = input("Novo email do usuário: ")
    if nome == '' or email == '' or usuario_id == '':
        print("Nome e email são obrigatórios!")
        return atualizar_usuario()
    usuarios_collection.update_one(
        {'_id': ObjectId(usuario_id)},
        {'$set': {'nome': nome, 'email': email}}
    )
    print(f"Usuário {usuario_id} atualizado com sucesso!")