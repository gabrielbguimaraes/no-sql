from utils.cassandra_conversor import convert_row_pydict_purchase

def get_purchase(session, purchase_id):
    script = f"SELECT * FROM purchase WHERE id = %s"
    purchase = session.execute(script, (purchase_id,)).one()
    return purchase if purchase else None

def get_all_purchases(session):
    script = "SELECT * FROM purchase"
    purchases = session.execute(script).all()
    return list(purchases)

def list_purchases(session):
    purchases = get_all_purchases(session)
    if not purchases:
        print("Sem compras cadastradas...")
        return None
    for purchase in purchases:
        purchase_pydict = convert_row_pydict_purchase(purchase)
        print("_"*50)
        print(f"ID: {purchase_pydict['id']}")
        print(f"ID Usuário: {purchase_pydict['id_usuario']}")
        print(f"ID Vendedor: {purchase_pydict['id_vendedor']}")
        print(f"Produtos: {purchase_pydict['produtos']}")
        print(f"Data: {purchase_pydict['data']}")
        print("_"*50)
    return purchases