from uuid import uuid4

def create_seller(session):
    try:
        seller_id = uuid4()

        print("_" * 50)
        print("Cadastro de Vendedor")
        print("_" * 50)

        nome_vendedor = input("Nome do Vendedor: ")
        email_vendedor = input("Email do Vendedor: ")
        cnpj_vendedor = input("CNPJ do Vendedor: ")
        print("_" * 50)

        enderecos = []

        while True:
            print("_" * 50)
            print("Cadastro de Endereço")
            rua = input("Rua: ")
            numero = input("Número: ")
            complemento = input("Complemento: ")
            cep = input("CEP: ")
            cidade = input("Cidade: ")
            estado = input("Estado: ")
            pais = input("País: ")
            print("_" * 50)

            enderecos.append({
                "rua": rua,
                "numero": numero,
                "complemento": complemento,
                "cep": cep,
                "cidade": cidade,
                "estado": estado,
                "pais": pais,
            })

            print("Endereço cadastrado com sucesso!")
            if input("Deseja adicionar outro endereço? (s/n): ").lower() == "n":
                break

        produtos = []

        script = """
            INSERT INTO seller (id, nome, email, cnpj, produtos, enderecos)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        session.execute(
            script,
            (
                seller_id,
                nome_vendedor,
                email_vendedor,
                cnpj_vendedor,
                produtos,
                enderecos,
            )
        )

        print("Vendedor cadastrado com sucesso!")
        print("ID do Vendedor:", seller_id)
        return
    except Exception as e:
        print(f"Erro ao registrar vendedor: {e}")
        return None

