import redis

def createRedisDatabase():
    try:
        r = redis.Redis(
        host='redis-18858.c44.us-east-1-2.ec2.redns.redis-cloud.com',
        port=18858,
        password='sGNE00pnLPiLRIEWJ8vYjsrUXLaNtVdv')
        r.ping()
        print('Conectado com sucesso ao Redis!')
        return r
    except redis.ConnectionError:
        print('Erro de conexão com o Redis!')
        return None