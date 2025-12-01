from utils.cassandra_conversor import convert_row_pydict_user
from utils.utils_users import get_user
from uuid import UUID

def search_user(session, user_id):

    print("_" * 50)
    print("Busca de Usuário")
    print("_" * 50)

    user = get_user(session, UUID(user_id))

    if user is None:
        print("Usuário não encontrado")
        return
    
    user_dict = convert_row_pydict_user(user)

    print("_" * 50)
    print("Usuário Encontrado")
    print("Nome:", {user_dict["nome"]})
    print("Senha:", {user_dict["senha"]})
    print("Email:", {user_dict["email"]})
    print("CPF:", {user_dict["cpf"]})

    if user_dict["enderecos"]:
        print("Endereços:")
        for endereco in user_dict["enderecos"]:
            print("_" * 50)
            print("Rua:", endereco["rua"])
            print("Número:", endereco["numero"])
            print("Complemento:", endereco["complemento"])
            print("CEP:", endereco["cep"])
            print("Cidade:", endereco["cidade"])
            print("Estado:", endereco["estado"])
            print("País:", endereco["pais"])
            print("_" * 50)
    else:
        print("Usuário não possui endereços cadastrados")

    if user_dict["favoritos"]:
        print("Favoritos:")
        for favorito in user_dict["favoritos"]:
            print("_" * 50)
            print("Nome:", favorito["nome"])
            print("Marca:", favorito["marca"])
            print("Preço:", favorito["preco"])
            print("_" * 50)
    else:
        print("Usuário não possui favoritos cadastrados")

    if user_dict["compras"]:
        print("Compras:")
        for compra in user_dict["compras"]:
            print("_" * 50)
            print("ID:", compra["id"])
            print("Data:", compra["data"])
    else:
        print("Usuário não possui compras cadastradas")

    print("_" * 50)

    
