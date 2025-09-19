from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI in App Runner"}

@app.get("/ping")
async def ping():
    return {"pong": True}
