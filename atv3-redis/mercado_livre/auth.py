# auth.py
from utils.utils import find_user

def login(usuarios_collection, db_redis, user_email, user_password):
    user = find_user(user_email, usuarios_collection)
    if user is None:
        print('Usuário não encontrado!')
        return None

    if user_password == user['senha']:
        user['_id'] = str(user['_id']) 
        db_redis.setex(f'user:{user_email}', 3600, user['_id'])
        print(f"Usuário {user_email} logado com sucesso por 1 hora!")
        return user
    else:
        print('Senha incorreta.')
        return None

def user_logged(db_redis, user_email):
    return bool(db_redis.get(f'user:{user_email}'))  # Retorna True se existir, False caso contrário

