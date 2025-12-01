from produtos.createProduto import criar_produto
from produtos.listProduto import listar_produtos
from produtos.editProduto import atualizar_produto
from produtos.deleteProduto import deletar_produto
from vendedor.createVendedor import criar_vendedor
from vendedor.listVendedor import listar_vendedores
from vendedor.editVendedor import atualizar_vendedor
from vendedor.deleteVendedor import deletar_vendedor
from usuarios.createUser import criar_usuario
from usuarios.listUser import listar_usuarios
from usuarios.editUser import atualizar_usuario
from usuarios.deleteUser import deletar_usuario
from favoritos.addFavoritos import favoritar_produto
from compras.compras import comprar_produto
from favoritos.deleteFavoritos import deletar_favorito

def menu():
    while True:
        print("\n1. Gerenciar Usuários")
        print("2. Gerenciar Vendedores")
        print("3. Gerenciar Produtos")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_usuarios()
        elif opcao == '2':
            menu_vendedores()
        elif opcao == '3':
            menu_produtos()
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

def menu_usuarios():
    while True:
        print("\n--- Menu Usuários ---")
        print("1. Criar Usuário")
        print("2. Listar Usuários")
        print("3. Atualizar Usuário")
        print("4. Excluir Usuário")
        print("5. Favoritar Produto")
        print("6. Desfavoritar Produto")
        print("7. Comprar Produto")
        print("8. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_usuario()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            atualizar_usuario()
        elif opcao == '4':
            deletar_usuario()
        elif opcao == '5':
            favoritar_produto()
        elif opcao == '6':
            deletar_favorito()
        elif opcao == '7':
            comprar_produto()
        elif opcao == '8':
            break
        else:
            print("Opção inválida! Tente novamente.")

def menu_vendedores():
    while True:
        print("\n--- Menu Vendedores ---")
        print("1. Criar Vendedor")
        print("2. Listar Vendedores")
        print("3. Atualizar Vendedor")
        print("4. Excluir Vendedor")
        print("5. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_vendedor()
        elif opcao == '2':
            listar_vendedores()
        elif opcao == '3':
            atualizar_vendedor()
        elif opcao == '4':
            deletar_vendedor()
        elif opcao == '5':
            break
        else:
            print("Opção inválida! Tente novamente.")

def menu_produtos():
    while True:
        print("\n--- Menu Produtos ---")
        print("1. Criar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Excluir Produto")
        print("5. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            atualizar_produto()
        elif opcao == '4':
            deletar_produto()
        elif opcao == '5':
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == '__main__':
    menu()