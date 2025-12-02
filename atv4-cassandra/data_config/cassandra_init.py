from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from data_config.collections_init import collections_init

def connect_cassandra():
    try:
        cloud_config = {
            'secure_connect_bundle': 'data_config/secure-connect-fatec-db.zip'
        }
        auth_provider = PlainTextAuthProvider(
            username='token', 
            password='AstraCS:ujXhvNLQucxvEuBGpRIjkwEB:b18c13403d6f368f390376481997d4f62c38d94b942e828f0d2169d4e335568d'
        )
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        session = cluster.connect()
        print('CONNECTED TO CASSANDRA')
        collections_init(session)
        return session
    except Exception as e:
        print(f'Erro ao conectar ao canssandra ${e}')
        return None