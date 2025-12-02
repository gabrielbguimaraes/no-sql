from .menu_favorite import menu_favorite
from .menu_purchase import menu_purchase

def menu(db_redis, user, usuarios_collection, produtos_collection, compras_collection):
    while True:
        print("\nBem-vindo(a) ao Mercado Livre!")
        print("1. Gerenciar Favoritos")
        print("2. Gerenciar Compras")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_favorite(db_redis, user, produtos_collection, usuarios_collection)
        elif opcao == '2':
            menu_purchase(db_redis, user, usuarios_collection, produtos_collection, compras_collection)
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")