def login(usuarios_collection, db_redis, email, password):
    user = usuarios_collection.find_one({'email': email})
    
    if user:

        senha_banco = user.get('senha') 
        
        if senha_banco is None:
            print(f"Aviso: O usuário {email} não tem senha cadastrada no banco.")
            if password == "":
                 pass 
            else:
                 print("Erro: Senha incorreta (ou usuário sem senha definida).")
                 return None
        elif senha_banco != password:
            print("Senha incorreta!")
            return None
            
        print(f"Login bem-sucedido para {user['nome']}")
        # Adiciona usuário logado no Redis com TTL de 1 hora (3600s)
        db_redis.setex(f"session:{email}", 3600, str(user['_id']))
        return user
    else:
        print("Usuário não encontrado!")
        return None

def logout(db_redis, email):
    db_redis.delete(f"session:{email}")
    print("Logout realizado com sucesso!")

def user_logged(db_redis, email):
    return db_redis.exists(f"session:{email}")