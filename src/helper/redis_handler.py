import redis

r = redis.Redis(host="192.168.10.152", port=6379)


def dump_data(ma_ddo, data):
    r.mset({ma_ddo: data})

def load_data(ma_ddo: str):
    return r.get(ma_ddo)
