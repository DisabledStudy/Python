import redis

conn = redis.Redis()
conn.keys('*')