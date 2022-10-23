from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/add")
async def addition(x: int, y: int):
    return {
        "data": x+y,
        "message": "success"
    }

@app.get("/ready")
async def readiness_probe():
    return {"message": "success"}
