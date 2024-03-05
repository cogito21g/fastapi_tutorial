# 01 Main Page

```python 
from fastapi import FastAPI, Request
import uvicorn
```
- 패키지 가져오기

```python
app = FastAPI()

@app.get("/")
def index_get(request: Request):
    return {"message": "Get Index"}

@app.post("/")
def index_post(request: Request):
    return {"message": "Post: Index"}

@app.put("/")
def index_put(request: Request):
    return {"message": "Put: Index"}

@app.delete("/")
def index_delete(request: Request):
    return {"message": "Delete: Index"}
```
- @app.get:    path는 "/"이고 GET 요청시 처리
- @app.post:   path는 "/"이고 POST 요청시 처리
- @app.put:    path는 "/"이고 PUT 요청시 처리
- @app.delete: path는 "/"이고 DELETE 요청시 처리

```python
uvicorn.run("app:app", host="0.0.0.0", port=8081, reload=True)
```
- "app:app": 앞쪽의 "app"은 app.py의 파일명, 뒤쪽의 "app"은 app=FastAPI()로 생성된 변수명
- host:      원하는 주소 입력("127.0.0.1"은 localhost, "0.0.0.0"은 모든 주소를 의미)
- port:      열려는 포트 입력(1~1024는 지정된 포트로 제외)
- reload:    True일 경우 서버에서 변경사항이 생기면 자동으로 재시작