from database import vendedores_collection

def listar_vendedores():
    vendedores = list(vendedores_collection.find())
    if not vendedores:
        print("Nenhum vendedor encontrado.")
        return
    print("Vendedores cadastrados:")
    for vendedor in vendedores:
        print(f"ID: {vendedor['_id']}, Nome: {vendedor['nome']}, Email: {vendedor['email']}")