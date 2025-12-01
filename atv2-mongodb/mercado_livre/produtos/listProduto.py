from database import produtos_collection

def listar_produtos():
    produtos = list(produtos_collection.find())
    if not produtos:
        print("Nenhum produto encontrado.")
        return
    print("Produtos cadastrados:")
    for produto in produtos:
        print(f"ID: {produto['_id']}, Nome: {produto['nome']}, Preço: {produto['preco']}, Vendedor ID: {produto['vendedor_id']}")