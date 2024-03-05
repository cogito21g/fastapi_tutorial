from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.get("/")
def index(request: Request):
    return {"message": "Welcome to FastAPI"}


if __name__=="__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8081, reload=True)