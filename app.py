from fastapi import FastAPI

app = FastAPI()
#uvicorn app:app --reload

@app.get("/")
async def root():
    return {"message": "Hello World"}