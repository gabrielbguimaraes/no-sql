from database import vendedores_collection, ObjectId


def deletar_vendedor():
    vendedor_id = input("Digite o ID do vendedor que deseja excluir: ")
    if vendedor_id == '':
        print("ID do vendedor é obrigatório!")
        return
    vendedores_collection.delete_one({'_id': ObjectId(vendedor_id)})
    print(f"Vendedor {vendedor_id} excluído com sucesso!")