from fastapi import FastAPI, Path
import uvicorn
from core.logger.api_logger import apiLogger
from core.logger.mid_logger.MiddlewareLogger import log_middleware
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()
app.add_middleware(middleware_class=BaseHTTPMiddleware, dispatch=log_middleware)

apiLogger.info("api starting.")


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
        app="hello_world_app:app",
        host="0.0.0.0",
        port=8000,
        reload=True

    )
