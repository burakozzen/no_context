import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        app="hello_world_app.hello_world_app:app",
        host="localhost",
        port=8000,
        reload=True

    )
