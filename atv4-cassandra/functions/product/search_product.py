from uuid import UUID
from utils.cassandra_conversor import convert_map_to_pydict
from utils.utils_product import get_product

def search_product(session, product_id):
    try:
        product = get_product(session, UUID(product_id))
        if product is None:
            print("Produto não encontrado!")
            return
        
        print("_" * 50)
        print("ID:", {product.id})
        print("Nome:", {product.nome})
        print("Marca:", {product.marca})
        print("Preço:", {product.preco})
        print("_" * 50)
        print("Nome Vendedor:", {product.vendedor_nome})
        print("Email Vendedor:", {product.vendedor_email})
        print("CNPJ Vendedor:", {product.cnpj_vendedor})
        print("_" * 50)
    
    except Exception as e:
        print(f"Erro ao buscar produto: {e}")
        return None


