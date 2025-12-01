from functions.user.create_user import create_user
from functions.user.edit_user import edit_user
from functions.user.search_user import search_user
from utils.utils_users import list_users

def menu_user(session):

    while True:
        print("_"*50)
        print("1 - Cadastrar Usuário")
        print("2 - Editar Usuário")
        print("3 - Procurar Compras do Usuário")
        print("4 - Listar Usuários")
        print("5 - Voltar")
        print("_"*50)

        try:
            option = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida")
            continue

        match option:
            case 1:
                create_user(session)
            case 2:
                users = list_users(session)
                if users is None:
                    print("Não há usuários cadastrados")
                    continue
                user_id = input("Digite o ID do usuário que deseja editar: ")
                edit_user(session, user_id)
            case 3:
                users = list_users(session)
                if users is None:
                    print("Não há usuários cadastrados")
                    continue
                user_id = input("Digite o ID do usuário que deseja procurar: ")
                search_user(session, user_id)
            case 4:
                list_users(session)
            case 5:
                break
            case _:
                print("Opção inválida")
                continue