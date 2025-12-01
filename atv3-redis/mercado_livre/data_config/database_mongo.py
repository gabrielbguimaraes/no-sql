from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi

def createMongoDatabase():
    uri = "mongodb+srv://MercadoLivre:1234@cluster0.z5cpx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri, tls=True, server_api=ServerApi('1'), tlsCAFile=certifi.where())
    try:
        client.admin.command('ping')
        print("Conectado com sucesso ao MongoDB!")
    except Exception as e:
        print(f"Erro de conexão: {e}")
        return None
    return client.MercadoLivre