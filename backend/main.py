from fastapi import FastAPI
import redis
app = FastAPI()
r = redis.Redis(host="redis", port=6379)
@app.get("/")
def home():
    return {"message": "Backend running"}
