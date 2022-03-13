## 실행 방법

### Prerequisite

1. pip install fastapi
2. pip install uvicorn[standard]
3. pip install sqlalchemy
4. Node.js

> 서버(infp에서) : $ uvicorn api-server.main:app --reload --host 0.0.0.0

host 0.0.0.0 해주어야 외부에서 접속 가능

> 웹(cd dashboard) : $ npm start
