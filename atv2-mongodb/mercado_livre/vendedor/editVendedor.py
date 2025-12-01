from database import vendedores_collection, ObjectId

def atualizar_vendedor():
    vendedor_id = input("Digite o ID do vendedor que deseja atualizar: ")
    nome = input("Novo nome do vendedor: ")
    email = input("Novo email do vendedor: ")
    if vendedor_id == '' or nome == '' or email == '':
        print("ID, nome e email são obrigatórios!")
        return atualizar_vendedor()
    vendedores_collection.update_one(
        {'_id': ObjectId(vendedor_id)},
        {'$set': {'nome': nome, 'email': email}}
    )
    print(f"Vendedor {vendedor_id} atualizado com sucesso!")