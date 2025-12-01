from utils.utils_users import get_user
from uuid import UUID

def edit_user(session, user_id):

    try:
        print("_" * 50)
        print("Edição de Usuário")
        print("_" * 50)

        user = get_user(session, UUID(user_id))

        if user is None:
            print("Usuário não encontrado")
            return
        
        nome = input(f"Nome do Usuário ({user.nome}): ")
        senha = input(f"Senha do Usuário ({user.senha}): ")
        email = input(f"Email do Usuário ({user.email}): ")
        cpf = input(f"CPF do Usuário ({user.cpf}): ")

        enderecos = user.enderecos if user.enderecos else []

        while True:
            print("_" * 50)
            print("1 - Adicionar Endereço")
            print("2 - Remover Endereço")
            print("3 - Sair")
            print("_" * 50)

            try :
                opcao = int(input("Escolha uma opção: "))
            except ValueError:
                print("Opção inválida")
                continue

            match opcao:
                case 1:
                    while True:
                        rua = input("Rua: ")
                        numero = input("Número: ")
                        complemento = input("Complemento: ")
                        cep = input("CEP: ")
                        cidade = input("Cidade: ")
                        estado = input("Estado: ")
                        pais = input("País: ")

                        enderecos.append
                        ({
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
                case 2:
                    if enderecos:
                        print("_" * 50)
                        print("Remoção de Endereço")
                        print("_" * 50)

                        for idx, endereco in enumerate(enderecos):
                            print(f"{idx} - {endereco['rua']} - {endereco['numero']}")

                        try:
                            idx_remove = int(input("Escolha o endereço que deseja remover: "))
                            if 0 <= idx_remove < len(enderecos):
                                enderecos.pop(idx_remove -1)
                                print("Endereço removido com sucesso!")
                            else:
                                print("Endereço não removido")
                        except ValueError:
                            print("Endereço não encontrado")
                    else:
                        print("Nenhum endereço cadastrado")

                case 3:
                    break
                case _:
                    print("Opção inválida")
                    continue
        script = """
            UPDATE user
            SET nome = %s, senha = %s, email = %s, cpf = %s, enderecos = %s
            WHERE id = %s
        """

        session.execute(script, (nome, senha, email, cpf, enderecos, user.id))

        print("Usuário editado com sucesso!")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e





        