from database import produtos_collection

def criar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    vendedor_id = input("Digite o ID do vendedor responsável: ")
    if nome == '' or preco == '' or vendedor_id == '':
        print("Nome, preço e ID do vendedor são obrigatórios!")
        return
    novo_produto = {'nome': nome, 'preco': preco, 'vendedor_id': vendedor_id}
    produto_id = produtos_collection.insert_one(novo_produto).inserted_id
    print(f"Produto {nome} criado com sucesso! ID: {produto_id}")