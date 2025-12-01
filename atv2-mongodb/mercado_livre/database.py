from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import certifi

# Configuração da conexão com MongoDB Atlas
uri = "mongodb+srv://<Nome do Bando>:<senha>@cluster0.z5cpx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Criar um cliente e conectar ao servidor
client = MongoClient(uri, tls=True, server_api=ServerApi('1'), tlsCAFile=certifi.where())

# Verificar a conexão
try:
    client.admin.command('ping')
    print("Conectado com sucesso ao MongoDB!")
except Exception as e:
    print(f"Erro de conexão: {e}")

# Selecionar o banco de dados
database = client.MercadoLivre

# Selecionar as coleções do banco de dados
usuarios_collection = database['Usuario']
vendedores_collection = database['Vendedores']
produtos_collection = database['Produtos']
favoritos_collection = database['Favoritos']
compras_collection = database['Compras']