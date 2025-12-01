from cassandra.util import OrderedMapSerializedKey

def convert_map_to_pydict(map):
    if isinstance(map, OrderedMapSerializedKey):
        return dict(map)
    return map

def convert_row_pydict_user(row):
    user_pydict = {
        "id": str(row.id),
        "nome": row.nome,
        "senha": row.senha,
        "email": row.email,
        "cpf": row.cpf,
        "favoritos": row.favoritos,
        "enderecos": [convert_map_to_pydict(endereco) for endereco in row.enderecos],
        "compras": row.compras
    }
    return user_pydict

def convert_row_pydict_seller(row):
    seller_pydict = {
        "id": str(row.id),
        "nome": row.nome,
        "email": row.email,
        "cnpj": row.cnpj,
        "produtos": [convert_map_to_pydict(produto) for produto in row.produtos] if row.produtos else [],
        "enderecos": [convert_map_to_pydict(endereco) for endereco in row.enderecos] if row.enderecos else []
    }
    return seller_pydict

def convert_row_pydict_purchase(row):
    purchase_pydict = {
        "id": str(row.id),
        "id_usuario": str(row.user_id),
        "id_vendedor": str(row.seller_id),
        "produtos": [convert_map_to_pydict(produto) for produto in row.produtos],
        "data": row.data,
    }
    return purchase_pydict