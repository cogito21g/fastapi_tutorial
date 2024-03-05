# 03 Database

```python
from urllib.parse import quote
from sqlalchemy import create_engine
from sqlalchemy import text
```
- 패키지 가져오기

```python
user ="username"
pwd = "password"
host = "xx.xx.xxx.xxx"
port = 8080
database="database_name"
db_url = f"mysql+pymysql://{user}:{quote(pwd)}@{host}:{port}/{database}"

engine = create_engine(
    db_url, pool_size=5, max_overflow=5, echo=True
)

conn = engine.connect()
result = conn.execute(text("show databases"))
try:
    conn.execute(text("CREATE TABLE test_table (x int, y int)"))
except: 
    conn.close()
    exit()
conn.execute(text("INSERT INTO test_table (x, y) VALUES (:x, :y)"),
            [{"x": 1, "y":1}, {"x":2, "y":4}])
conn.commit()
print(result.all())
conn.close()
```
- db_url:                     연결할 db의 database 주소입력.
- create_engine:              database와 연결할 engine 설정
- engine.connect():           Connection 객체 반환. Connection 객체를 통해 database와 상호작용
- connect.execute(statement): statement에 MYSQL 문법을 이용해 database에 적용. 결과 반환
- conn.commit():              database에 반영
- conn.close():               연결 종료.

```bash
mysql -h xx.xx.xxx.xxx -u username -P 8080 -p password
show databases;
use databse_name;
show tables;
SELECT * FROM table_name;
```
- mysql -h xx.xx.xxx.xxx -u username -P 8080 -p password: mysql에 접속 명령어. -h는 호스트 주소. -u 유저명 -P 포트번호 -p 비밀번호
- show databases;                                       : database 목록 확인 
- use databse_name;                                     : database 선택
- show tables;                                          : database내 table 목록 확인
- SELECT * FROM table_name;                             : table내의 모든 데이버 확인
