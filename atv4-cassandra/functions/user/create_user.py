from uuid import uuid4

def create_user(session):
    try:
        user_id = uuid4()
        
        print("_" * 50)
        print("Cadastro de Usuário")
        print("_" * 50)

        nome = input("Nome: ")
        senha = input("Senha: ")
        email = input("Email: ")
        cpf = input("CPF: ")

        enderecos = []
        while True:

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

            if input("Deseja adicionar outro endereço? (s/n): ").lower() == "n":
                break

        favoritos = []
        compras = []

        script = """
            INSERT INTO user (id, nome, senha, email, cpf, favoritos, enderecos, compras)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        session.execute(
            script,
            (
                user_id,
                nome,
                senha,
                email,
                cpf,
                favoritos,
                enderecos,
                compras,
            )
        )

        print("Usuário cadastrado com sucesso!")
    except Exception as e:
        print("Erro ao cadastrar usuário:", e)
        return None

        