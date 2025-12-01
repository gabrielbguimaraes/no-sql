from functions.seller.create_seller import create_seller
from functions.seller.search_seller import search_seller
from utils.utils_seller import list_sellers


def menu_seller(session):
    
    while True:   
        print("_"*50)
        print("1 - Cadastrar Vendendor")
        print("2 - Procurar Vendedor")
        print("3 - Listar Vendendores")
        print("4 - Sair")
        print("_"*50)

        try:
            option = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida")
            continue

        match option:
            case 1:
                create_seller(session)
            case 2:
                sellers = list_sellers(session)
                if sellers is None:
                    print("Nenhum vendedor encontrado")
                    break
                seller_id = input("Digite o ID do vendedor: ")
                search_seller(session, seller_id)
            case 3:
                list_sellers(session)
            case 4:
                print("Saindo...")
                break
            case _:
                print("Opção inválida!")
                continue
