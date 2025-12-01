from bson import ObjectId

def find_user(user_email, usuarios_collection):
    user = usuarios_collection.find_one({"email": user_email})
    if user:
        user['_id'] = str(user['_id']) 
    return user

def list_products(produto_collection):
    products = list(produto_collection.find().sort('nome'))
    products_list = [{'id': str(product['_id']), 'nome': product['nome']} for product in products]
    print("-=" * 20)
    for product in products_list:
        print(f"ID: {product['id']}, Nome: {product['nome']}")
    print("-=" * 20)

def find_product(product_id, produto_collection):
    product = produto_collection.find_one({"_id": ObjectId(product_id)})
    if product:
        return product
    return None

