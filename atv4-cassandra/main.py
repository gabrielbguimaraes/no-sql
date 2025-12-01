from data_config.cassandra_init import connect_cassandra
from menu.products import menu_product
from menu.user import menu_user
from menu.seller import menu_seller
from menu.purchases import menu_purchase

def main():
    cluster = connect_cassandra()
    if cluster is None:
        print("Erro ao conectar ao Cassandra")
        return
    
    while True:
        print("_"*50)
        print("Bem-vindo ao Mercado Livre")
        print("_"*50)
        print("1 - Menu do Usuário")
        print("2 - Menu do Vendedor")
        print("3 - Menu de Compras")
        print("4 - Menu do Produto")
        print("5 - Sair")
        print("_"*50)

        try:
            option = int(input("Escolha uma opção: "))
        except:
            print("Opção inválida")
            continue

        match option:
            case 1:
                menu_user(cluster)
            case 2:
                menu_seller(cluster)
            case 3:
                menu_purchase(cluster)
            case 4:
                menu_product(cluster)
            case 5:
                print("Saindo...")
                break
            case _:
                print("Opção inválida!")
                continue

if __name__ == "__main__":
    main()