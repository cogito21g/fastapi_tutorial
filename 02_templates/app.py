from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(request=request,name="index.html", context={"message": "Welcoe FastAPI"})

if __name__=="__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8081, reload=True)