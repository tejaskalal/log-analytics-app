import redis
import json
r = redis.Redis(host="redis", port=6379)
while True:
    _, data = r.brpop("logs")
    print("Processing:", data)
