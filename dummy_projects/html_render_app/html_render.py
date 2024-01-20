from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

template = Jinja2Templates(directory="templates")

@app.get("/")
def login(req:Request):
    return template.TemplateResponse(
        name="login.html",
        context={"request":req}
    )

if __name__ == "__main__":
    uvicorn.run("html_render:app")