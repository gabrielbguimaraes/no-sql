from data_config.database_redis import createRedisDatabase
from bson import ObjectId
from utils.utils import list_products, find_product

def favorite_product(produtos_collection, db_redis, user):
    list_products(produtos_collection)
    favorites = []

    while True:
        product_id = input('Digite o Id do produto que deseja favoritar: ').strip()
        product = find_product(product_id, produtos_collection)

        if product:
            product_info = {
                "_id":product["_id"],
                "nome": product["nome"]
                }
            favorites.append(product_info)
        else:
            print('Produto não encontrado!')

        proceed = input('Deseja favoritar mais algum? (S/N) ').lower()
        if proceed == 'n':
            break
    
    for fav in favorites:
        redis_key = f"user:{user['_id']}:favorites"
        db_redis.sadd(redis_key, str(fav))
        
    print("-="*20)
    print("Favorito adicionados com sucesso.")