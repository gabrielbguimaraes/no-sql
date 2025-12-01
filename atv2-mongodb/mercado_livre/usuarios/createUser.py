from database import usuarios_collection

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    if nome == '' or email == '':
        print("Nome e email são obrigatórios!")
        return criar_usuario()
    novo_usuario = {'nome': nome, 'email': email, 'favoritos': []}
    usuario_id = usuarios_collection.insert_one(novo_usuario).inserted_id
    print(f"Usuário {nome} criado com sucesso! ID: {usuario_id}")