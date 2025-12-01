def list_product(db_redis, user):
    user_purchase_key = f"user:{user['email']}:purchases"  
    
    purchase_keys = db_redis.lrange(user_purchase_key, 0, -1)
    
    for key in purchase_keys:
        product = db_redis.hgetall(key)
        
        product_id = key.decode('utf-8').split(':')[1]
        
        name = product.get(b'nome', b'').decode('utf-8')
        price = product.get(b'preco', b'').decode('utf-8')
        
        print(f"ID: {product_id}, Nome: {name}, Preço: {price}")
