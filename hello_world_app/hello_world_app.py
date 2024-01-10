from fastapi import FastAPI, Path
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return "Hello World Burak !"


inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular"
    }
}


@app.get("/get_item/{item_id}")
def get_item(
        item_id: int = Path(default_factory=None, description="The ID of the item you'd like to view.", gt=0, lt=2)):
    return inventory[item_id]


if __name__ == "__main__":
    uvicorn.run(
        app="hello_world_app.hello_world_app:app",
        host="0.0.0.0",
        port=8000,
        reload=True

    )
