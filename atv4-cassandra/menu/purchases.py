from functions.purchases.create_purchases import create_purchase
from functions.purchases.delete_purchases import delete_purchase
from utils.utils_users import list_users
from utils.utils_purchase import list_purchases


def menu_purchase(session):

    while True:

        print("_"*50)
        print("1 - Comprar")
        print("2 - Listar Compras")
        print("3 - Deletar Compra")
        print("4 - Voltar")
        print("_"*50)

        try:
            option = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida")
            continue

        match option:
            case 1:
                users = list_users(session)
                if users is None:
                    print("Erro ao buscar usuários")
                    continue
                user_id = input("Digite o id do usuário: ")
                create_purchase(session, user_id)
            case 2:
                list_purchases(session)
            case 3:
                compras = list_purchases(session)
                if compras is None:
                    print("Erro ao buscar compras")
                    return
                purchase_id = input("Digite o id da compra: ")
                delete_purchase(session, purchase_id)
            case 4: 
                print("Voltando...")
                break
            case _:
                print("Opção inválida!")
                continue
