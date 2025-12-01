from functions.product.create_product import create_product
from functions.product.search_product import search_product
from utils.utils_seller import list_sellers
from utils.utils_product import list_products
from uuid import UUID


def menu_product(session):

    
    while True:
        print("_"*50)
        print("1 - Registrar Produto")
        print("2 - Buscar Produto")
        print("3 - Listar Produtos")
        print("4 - Voltar")
        print("_"*50)

        try:
            opcao = int(input("Digite a opção desejada: "))
        except:
            print("Opção inválida!")
            continue

        match opcao:
            case 1:
                seller = list_sellers(session)
                if seller is None:
                    print("Nenhum vendedor cadastrado!")
                    return
                seller_id = input("Digite o ID do vendedor: ").strip()
                create_product(session, seller_id)
            case 2:
                products = list_products(session)
                if products is None:
                    print("Nenhum produto cadastrado!")
                    return
                product_id = input("Digite o ID do produto: ").strip()
                search_product(session, product_id)
            case 3:
                list_products(session)
            case 4:
                break
            case _:
                print("Opção inválida!")
                continue


