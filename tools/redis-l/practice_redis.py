import redis

r = redis.Redis(host='localhost', port=6379, db=0)  # give redis connection object

print(r.ping()) # returns true if connected to redis server

