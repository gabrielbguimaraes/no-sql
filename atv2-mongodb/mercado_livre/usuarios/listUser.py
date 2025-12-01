from database import usuarios_collection

def listar_usuarios():
    usuarios = list(usuarios_collection.find())
    if not usuarios:
        print("Nenhum usuário encontrado.")
        return
    print("Usuários cadastrados:")
    for usuario in usuarios:
        usuario_id = usuario.get('_id', 'ID não encontrado')
        nome = usuario.get('nome', 'Nome não disponível')
        email = usuario.get('email', 'Email não disponível')
        favoritos = usuario.get('favoritos', [])
        
        print(f"ID: {usuario_id}, Nome: {nome}, Email: {email}, Favoritos: {favoritos}")