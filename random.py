import redis
import random

redis1 = redis.Redis(host='redis-1', port=6379, db=0)
redis2 = redis.Redis(host='redis-2', port=6379, db=0)
redis3 = redis.Redis(host='redis-3', port=6379, db=0)
redis4 = redis.Redis(host='redis-4', port=6379, db=0)
redis5 = redis.Redis(host='redis-5', port=6379, db=0)
redis6 = redis.Redis(host='redis-6', port=6379, db=0)
redis7 = redis.Redis(host='redis-7', port=6379, db=0)
redis8 = redis.Redis(host='redis-8', port=6379, db=0)

A = 66666

for i in range(A):
    key = "key_" + str(i)
    value = str(random.randint(0, 66666))
    redis1.set(key, value)
    redis2.set(key, value)
    redis3.set(key, value)
    redis4.set(key, value)
    redis5.set(key, value)
    redis6.set(key, value)
    redis7.set(key, value)
    redis8.set(key, value)
