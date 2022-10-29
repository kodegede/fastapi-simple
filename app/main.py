from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#Add simple function to add 2 integers
@app.get("/add")
async def addition(x:int, y:int):
    return {
        "data": x - y,
        "message": "success",
    }
