from utils.cassandra_conversor import convert_row_pydict_seller

def get_seller(session, seller_id):
    script = f"SELECT * FROM seller WHERE id = %s"
    seller = session.execute(script, (seller_id,)).one()
    return seller if seller else None

def get_all_sellers(session):
    script = "SELECT * FROM seller"
    sellers = session.execute(script).all()
    return list(sellers)

def list_sellers(session):
    sellers = get_all_sellers(session)
    if not sellers:
        print("Sem vendedores cadastrados...")
        return None
    for seller in sellers:
        seller_pydict = convert_row_pydict_seller(seller)
        print("_"*50)
        print(f"ID: {seller_pydict['id']}")
        print(f"Nome: {seller_pydict['nome']}")
        print(f"Email: {seller_pydict['email']}")
        print(f"CNPJ: {seller_pydict['cnpj']}")
        print(f"Produtos: {seller_pydict['produtos']}")
        print(f"Endereços: {seller_pydict['enderecos']}")
        print("_"*50)
    return sellers
