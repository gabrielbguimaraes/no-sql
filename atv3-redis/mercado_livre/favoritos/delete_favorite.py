from bson import ObjectId
from data_config.database_redis import createRedisDatabase
from utils.utils import list_products, find_product
from favoritos.list_favorites import list_favorites



def delete_favorite(produtos_collection, db_redis, user):
    list_favorites(db_redis, user)
    favorites_removed = []

    while True:
        product_id = input('Digite o Id do produto que deseja remover do favorito: ')
        product = find_product(product_id, produtos_collection)

        if product:
            product_info = {
                "_id":product["_id"],
                "nome": product["nome"],
            }
            favorites_removed.append(product_info) 
        else:
            print('Produto não encontrado!')

        proceed = input('Deseja remover mais algum? (S/N) ').lower()
        if proceed == 'n':
            break

    redis_key = f"user:{user['_id']}:favorites"

    for fav in favorites_removed:
        result = db_redis.srem(redis_key, str(fav))
        
        if result > 0:
            print(f"Produto removido dos favoritos com sucesso.")
        else:
            print(f"Produto {fav} não encontrado nos favoritos.")

    print("-=" * 20)