from database import vendedores_collection

def criar_vendedor():
    nome = input("Digite o nome do vendedor: ")
    email = input("Digite o email do vendedor: ")
    novo_vendedor = {'nome': nome, 'email': email}
    vendedor_id = vendedores_collection.insert_one(novo_vendedor).inserted_id
    print(f"Vendedor {nome} criado com sucesso! ID: {vendedor_id}")