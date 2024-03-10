import os

from fastapi import FastAPI, Request, File, UploadFile
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
upload_dir = os.path.join(BASE_DIR,'files/')
os.makedirs(upload_dir, exist_ok=True)


@app.get("/")
def index_get(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"message": "Single File"})

# @app.post("/")
# def index_post(request: Request, file: bytes=File(...)):
#     msg = file
#     with open(os.path.join(upload_dir, "test.png"), "wb") as f:
#         f.write(msg)
#     return templates.TemplateResponse(request=request, name="index.html", context={"message": msg})

@app.post("/")
async def index_post(request: Request, file: UploadFile):
    msg = file.filename
    real = 0
    for chunk in file.file:
        real = real + len(chunk)
        if real > 2 * 1024 * 1024:
            return templates.TemplateResponse(request=request, name="index.html", context={"message": "Too Much Size"})
    data = file.file.read()
    with open(os.path.join(upload_dir, file.filename), "wb") as f:
        f.write(data)
    return templates.TemplateResponse(request=request, name="index.html", context={"message": msg})


if __name__=="__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8081, reload=True)


