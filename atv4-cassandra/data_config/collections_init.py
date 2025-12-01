#criar coleções no Cassandra

def collections_init(session):
    try: 
        session.execute("USE mercadolivre")

        session.execute(
            """
            CREATE TABLE IF NOT EXISTS user (
                id UUID PRIMARY KEY,
                nome TEXT,
                senha TEXT,
                email TEXT,
                cpf TEXT,
                favoritos LIST<FROZEN<MAP<TEXT,TEXT>>>,
                enderecos LIST<FROZEN<MAP<TEXT,TEXT>>>,
                compras LIST<FROZEN<MAP<TEXT,TEXT>>>
            )
            """
        )

        session.execute(
            """
            CREATE TABLE IF NOT EXISTS seller (
                id UUID PRIMARY KEY,
                nome TEXT,
                email TEXT,
                cnpj TEXT,
                produtos LIST<FROZEN<MAP<TEXT,TEXT>>>,
                enderecos LIST<FROZEN<MAP<TEXT,TEXT>>>
            )
            """
        )

        session.execute(
            """
            CREATE TABLE IF NOT EXISTS purchase (
                id UUID PRIMARY KEY,
                user_id UUID,
                seller_id UUID,
                produtos LIST<FROZEN<MAP<TEXT,TEXT>>>,
                entrega_final FROZEN<MAP<TEXT,TEXT>>,
                data TIMESTAMP
            )
            """
        )

        session.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                id UUID PRIMARY KEY,
                nome TEXT,
                marca TEXT,
                preco DECIMAL,
                vendedor_id UUID,
                vendedor_nome TEXT,
                vendedor_email TEXT,
                cnpj_vendedor TEXT
            )
            """
        )

        print("Collections created successfully")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e