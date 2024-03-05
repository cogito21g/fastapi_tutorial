# Multi File Upload

```python
@app.post("/")
async def files_post(request: Request, files: list[bytes]):
    for file in files:
        msg = file.decode()
    return templates.TemplateResponse(request=request, name="index.html", context={"message": msg})
```
- 인코딩/디코딩시 문제 발생(사용하지말 것)

```python
@app.post("/")
async def files_post(request: Request, files: list[UploadFile]):
    msg = []
    for file in files:
        msg.append(file.filename)
        data = file.file.read()
        with open(os.path.join(upload_dir, file.filename), "wb") as f:
            f.write(data)
    return templates.TemplateResponse(request=request, name="index.html", context={"message": msg})
```
- list\[UploadFile\]:  html의 form에서 넘어온 데이터를 리스트로 처리.(enctype="multipart/form-data")
  - filename:          파일 이름
  - file.file:         파일 Binary IO
- **files 변수명은 html의 input의 name과 동일해야함**.

```html
<form action="/" method="post" enctype="multipart/form-data">
    <label for="file">Multi File Upload: </label>
    <input type="file" id="file" name="files" multiple>
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
  - type:                                입력 받을 형태 지정(text, email, password, file, ...)
  - multiple:                            여러 파일 선택 허용
- button:                                버튼 요소
  - type:                                사용할 타입 형태(submit, reset, button)
