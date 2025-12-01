from bson import ObjectId

def sync_produtos(db_redis, compras_collection):
    keys = db_redis.keys('compra:*')
    for key in keys:
        compra = db_redis.hgetall(key)
        
        # Decodificar os valores do Redis (se necessário)
        compra_decoded = {k.decode('utf-8'): v.decode('utf-8') for k, v in compra.items()}
        
        compras_collection.insert_one(compra_decoded)
        
        db_redis.delete(key)
    print("Sincronização concluída com sucesso!")
