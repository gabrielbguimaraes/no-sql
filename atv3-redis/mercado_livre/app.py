from data_config.database_mongo import createMongoDatabase
from data_config.database_redis import createRedisDatabase
from auth import login
from menu.menu import menu
import pprint

def main():
    
    db_mongo = createMongoDatabase()
    db_redis = createRedisDatabase()
    if db_mongo is None or db_redis is None:
        print("Erro ao conectar aos bancos de dados!")
        return
    
    usuarios_collection = db_mongo['Usuario']
    produtos_collection = db_mongo['Produtos']
    compras_collection = db_mongo['Compras']

    user_email = input("Digite o email do usuário: ")
    user_password = input("Digite a senha do usuário: ")

    user = login(usuarios_collection, db_redis, user_email, user_password)
    if not user:
        print("Erro: Não foi possível autenticar o usuário.")
        return

    print(f"DEBUG: Usuário autenticado -> {user}")

    print("Usuário autenticado com sucesso! Bem-Vindo!")
    
    menu(db_redis, user, usuarios_collection, produtos_collection, compras_collection)

if __name__ == "__main__":
    main()