from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.get("/")
def index(request: Request):
    return {"message": "Welcome to FastAPI"}

@app.post("/")
def index_post(request: Request):
    return {"message": "Post: Index"}

@app.put("/")
def index_put(request: Request):
    return {"message": "Put: Index"}

@app.delete("/")
def index_delete(request: Request):
    return {"message": "Delete: Index"}

if __name__=="__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8081, reload=True)