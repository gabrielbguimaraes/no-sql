from favoritos.add_favoritos import favorite_product
from favoritos.delete_favorite import delete_favorite
from favoritos.list_favorites import list_favorites
from favoritos.sync_favoritos import sync_favorites

def menu_favorite(db_redis, user, produtos_collection, usuarios_collection):
    while True:
        print("\n1. Adicionar Favorito")
        print("2. Deletar Favorito")
        print("3. Listar Favoritos")
        print("4. Sincronizar Favoritos")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            favorite_product(produtos_collection, db_redis, user)
        elif opcao == '2':
            delete_favorite( produtos_collection, db_redis, user)
        elif opcao == '3':
            list_favorites(db_redis, user)
        elif opcao == '4':
            sync_favorites(db_redis,usuarios_collection,user)
        elif opcao == '5':
            print("Saindo...")
            break