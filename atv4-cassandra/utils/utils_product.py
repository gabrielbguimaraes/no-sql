def get_product(session, product_id):
    script = f"SELECT * FROM products WHERE id = %s"
    product = session.execute(script, (product_id,)).one()
    return product if product else None

def get_all_products(session):
    script = "SELECT * FROM products"
    products = session.execute(script).all()
    return list(products) # só pra confirmar que vai voltar lista

def list_products(session):
    products = get_all_products(session)
    if not products:
        print("Sem produtos cadastrados...")
        return None
    for product in products:
        print("_"*50)
        print(f"ID: {product.id}")
        print(f"Nome: {product.nome}")
        print(f"Marca: {product.marca}")
        print(f"Preço: {product.preco:.2f}")
        print(f"Vendedor: {product.vendedor_nome}")
        print("_"*50)
    return products

    