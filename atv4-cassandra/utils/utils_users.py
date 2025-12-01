from utils.cassandra_conversor import convert_row_pydict_user

def get_user(session, user_id):
    script = f"SELECT * FROM user WHERE id = %s"
    user = session.execute(script, (user_id,)).one()
    return user if user else None

def get_all_users(session):
    script = "SELECT * FROM user"
    users = session.execute(script).all()
    return list(users)

def list_users(session):
    users = get_all_users(session)
    if not users:
        print("Sem usuários cadastrados...")
        return None
    for user in users:
        user_pydict = convert_row_pydict_user(user)
        print("_"*50)
        print(f"ID: {user_pydict['id']}")
        print(f"Nome: {user_pydict['nome']}")
        print(f"Email: {user_pydict['email']}")
        print(f"CPF: {user_pydict['cpf']}")
        print("_"*50)
    return users