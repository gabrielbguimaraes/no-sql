from uuid import UUID
from utils.cassandra_conversor import convert_row_pydict_seller
from utils.utils_seller import get_seller

def search_seller(session, seller_id):
    print("Buscando vendedor...")
    print("_" * 50)

    seller = get_seller(session, UUID(seller_id))

    if seller is None:
        print("Vendedor não encontrado!")
        return
    
    seller_dict = convert_row_pydict_seller(seller)

    print("Vendedor encontrado:")
    print("Nome:", {seller_dict["nome"]})
    print("Email:", {seller_dict["email"]})
    print("CNPJ:", {seller_dict["cnpj"]})

    if seller_dict["produtos"]:
        print("Produtos:")
        for produto in seller_dict["produtos"]:
            print(produto)

    else:
        print("Nenhum produto cadastrado")

    if seller_dict["enderecos"]:
        print("Endereços:")
        for endereco in seller_dict["enderecos"]:
            print("Rua:", endereco["rua"], "Número:", endereco["numero"], "CEP:", endereco["cep"], "Cidade:", endereco["cidade"], "Estado:", endereco["estado"])

    else:
        print("Nenhum endereço cadastrado")

    print("_" * 50)