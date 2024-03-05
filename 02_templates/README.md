# 02 Templates

```python
from fastapi.templating import Jinja2Templates
```
- 패키지 가져오기

```python
templates = Jinja2Templates(directory="templates")
```
- Jinja2Templates: directory로 기준 폴더 지정. 해당 폴더에서 html 탐색

```python
@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(request=request,name="index.html", context={"message": "Welcoe FastAPI"})
```
- TemplateResponse: Response 인스턴스 생성
  - name은 html 파일명
  - context에 name에 지정된 파일에 넘길 데이터 전달

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Template</title>
</head>
<body>
    <h1>Template Page</h1>

    <p>{{ message }}</p>
</body>
</html>
```
- Jinja Template 문법 사용
- {{ 변수명 }}: context에 넘겨준 dict의 key값을 변수명으로 사용 