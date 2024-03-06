# 04 Single File Upload

```python
import os
from fastapi import FastAPI, Request, File, UploadFile
```
- 패키지 가져오기
- os:                 경로 설정을 위함.
- fastapi.File:       html의 form을 처리하기 위함. Form을 상속 
- fastapi.UploadFile: html의 form을 처리하기 위함. starlette의 UploadFile 상속

```python
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
upload_dir = os.path.join(BASE_DIR,'files/')
os.makedirs(upload_dir, exist_ok=True)
```
- __file__:          실행한 파일의 이름이나 경로
- os.path.abspath(): 파일이나 폴더의 절대 경로 반환
- os.path.dirname(): 입력한 파일이나 폴더의 경로까지 반환
- os.path.join():    두 문자열을 파일 경로 형식에 맞게 결합 
- os.makedir():      마지막에 적힌 폴더 하나 생성. exist_ok=True일 경우 해당 폴더 존재시 에러를 발생시키지 않음.
- os.makedirs():     경로의 모든 폴더를 생성. exist_ok=True일 경우 해당 경로 존재시 에러를 발생시키지 않음

```python
@app.post("/")
def index_post(request: Request, file: bytes=File(...)):
    msg = file
    with open(os.path.join(upload_dir, "test.png"), "wb") as f:
        f.write(msg)
    return templates.TemplateResponse(request=request, name="index.html", context={"message": msg})
```
- File: html의 form에서 넘어온 데이터 처리
  - form의 enctype="application/x-www-form-urlencoded"일 경우 파일명
  - form의 enctype="multipart/form-data"일 경우 Binary IO
- bytes 형태의 데이터는 메모리에 저장됨.

```python
@app.post("/")
async def index_post(request: Request, file: UploadFile):
    msg = file.filename
    data = file.file.read()
    with open(os.path.join(upload_dir, file.filename), "wb") as f:
        f.write(data)
    return templates.TemplateResponse(request=request, name="index.html", context={"message": msg})

```
- UploadFile:  html의 form에서 넘어온 데이터 처리.(enctype="multipart/form-data")
  - filename:  파일 이름
  - file.file: 파일 Binary IO. spooledTemporaryFile.
- 최대 크기 제한까지는 메모리에 저장후 디스크에 저장.

```html
<!-- <form action="/" method="post" enctype="application/x-www-form-urlencoded"> -->
<form action="/" method="post" enctype="multipart/form-data">
    <label for="file">File Upload: </label>
    <input type="file" id="file" name="file" >
    <button type="submit">Submit</button>
</form>
```
- form:                                  입력된 데이터를 서버로 전송. 
  - action:                              전송할 서버 경로 지정. 
  - method:                              전송 방식 지정(get, post)
  - enctype:                             폼 데이터가 서버로 제출시 데이터의 인코딩 방식 지정.
    - application/x-www-form-urlencoded: 모든 문자들은 서버로 보내기 전에 인코딩. 
    - multipart/form-data:               모든 문자를 인코딩하지 않음(파일이나 이미지를 서버로 전송시 사용).
    - text/plain:                        공백 문자는 "+"로 나머지 문자는 모두 인코딩되지 않음.
- label:                                 입력 요소의 라벨 지정
- input:                                 입력 컨트롤 정의.
  - name:                                input의 속성으로 서버에서 변수명으로 사용
  - value:                               input의 속성으로 기본값 지정.
  - type:                                입력 받을 형태 지정(text, email, password, file, ...)
- button:                                버튼 요소
  - type:                                사용할 타입 형태(submit, reset, button)
  - onclick:                             클릭시 동작할 javascript 함수 연결