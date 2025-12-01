from database import compras_collection, produtos_collection
import uuid
from bson import ObjectId

def comprar_produto():
    id_usuario = input("Digite o ID do usuário: ")
    id_produto = input("Digite o ID do produto: ")
    if id_usuario == '' or id_produto == '':
        print("ID do usuário e ID do produto são obrigatórios!")
        return comprar_produto()
    
    try:
        produto_id = ObjectId(id_produto)
    except Exception as e:
        print("ID do produto inválido!")
        return comprar_produto()

    
    produto = produtos_collection.find_one({'_id': produto_id})
    if not produto:
        print("Produto não encontrado!")
        return comprar_produto()
    
    id_compra = str(uuid.uuid4())
    nova_compra = {
        'id_compra': id_compra,
        'id_usuario': id_usuario,
        'produto': produto 
    }
    compra_id = compras_collection.insert_one(nova_compra).inserted_id
    print(f"Compra criada com sucesso! ID da compra: {compra_id}")
