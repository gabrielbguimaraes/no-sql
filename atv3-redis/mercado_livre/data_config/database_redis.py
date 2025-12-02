import redis

def createRedisDatabase():
    try:
        
        r = redis.Redis(
            host='redis-14494.c345.samerica-east1-1.gce.cloud.redislabs.com',
            port=14494,
            password='xp2ZfYNic75c2BFPGquRvFgPuaaTXeMZ'
        )
        
        r.ping()
        print('Conectado com sucesso ao Redis!')
        return r
    except redis.ConnectionError as e:
        print(f'Erro de conexão com o Redis: {e}')
        return None