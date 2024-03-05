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
async def files_get(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"message": "Welcome Multi File"})

# @app.post("/")
# async def files_post(request: Request, files: list[bytes]):
#     for file in files:
#         msg = file.decode()
#     return templates.TemplateResponse(request=request, name="index.html", context={"message": msg})

@app.post("/")
async def files_post(request: Request, files: list[UploadFile]):
    msg = []
    for file in files:
        msg.append(file.filename)
        data = file.file.read()
        with open(os.path.join(upload_dir, file.filename), "wb") as f:
            f.write(data)
    return templates.TemplateResponse(request=request, name="index.html", context={"message": msg})


if __name__=="__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8081, reload=True)


