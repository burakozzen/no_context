from fastapi import FastAPI, Path

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
