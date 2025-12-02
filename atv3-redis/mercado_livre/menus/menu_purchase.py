from compras.buy_product import buy_product
from compras.list_product import list_product
from compras.sync_product import sync_produtos
from auth import user_logged

def menu_purchase(db_redis, user, usuarios_collection, produtos_collection, compras_collection):
    print(f"DEBUG: User recebido -> {user}")
    if not user or 'email' not in user or not user_logged(db_redis, user['email']):
        print("Erro: Usuário não autenticado.")
        return

    while True:
        print("\n1. Comprar")
        print("2. Listar Produtos")
        print("3. Sincronizar Compras")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            buy_product(produtos_collection, db_redis, user, compras_collection)
        elif opcao == '2':
            list_product(db_redis, user)
        elif opcao == '3':
            sync_produtos(db_redis, compras_collection)
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
