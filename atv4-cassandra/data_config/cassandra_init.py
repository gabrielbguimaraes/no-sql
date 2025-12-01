from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from data_config.collections_init import collections_init

def connect_cassandra():
    try:
        cloud_config = {
            'secure_connect_bundle': 'data_config/secure-connect-mercadolivre.zip'
        }
        auth_provider = PlainTextAuthProvider(
            username='token', 
            password='SEU TOKEN'
        )
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        session = cluster.connect()
        print('CONNECTED TO CASSANDRA')
        collections_init(session)
        return session
    except Exception as e:
        print(f'Erro ao conectar ao canssandra ${e}')
        return None