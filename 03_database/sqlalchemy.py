from urllib.parse import quote
from sqlalchemy import create_engine
from sqlalchemy import text


# mysql -h xx.xx.xxx.xxx -u username -P 8080 -p password
# show databases; user databse_name;
# show tables;

# dababase와 연동하기 위한 정보
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