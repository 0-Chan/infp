
## 결과
<img src="https://user-images.githubusercontent.com/50035753/173994748-d0f9832a-18fa-41e3-b61d-35623d2f4bbc.png" alt="slack_capture" width=35%>

슬랙 api 호출 결과입니다. 실시간 카드 사용 내역을 슬랙 bot이 전달합니다.

## 과정
- Before & After <br>
<img src="https://user-images.githubusercontent.com/50035753/174471284-c93dbfab-da4a-4ddd-a91c-c6e5d73abf42.jpg" alt="description" width=70%>


Before : 기존에는 카드사에서 알림 내역을 다이렉트로 SMS 문자로 전달 받았습니다.  
<br>
After : 제가 구축한 프로젝트는 다음과 같은 과정을 거칩니다.
1. 알림 내역을 카드사 앱 알림으로 받습니다.
2. 안드로이드 push notification forward 앱을 통해
3. FastAPI로 구축된 서버로 보냅니다.(post 요청)

해당 서버에서 Sqlite DB에 사용 시간, 내역 등을 파싱하여 저장하고 및 슬랙 Webhook을 보내어 가계부 입력을 자동화합니다.

## 실행 방법

### Prerequisite

1. pip install fastapi
2. pip install uvicorn[standard]
3. pip install sqlalchemy
4. Node.js(ver 14.xx ↑)

> 서버(infp에서) : $ uvicorn api-server.main:app --reload --host 0.0.0.0

host 0.0.0.0 해주어야 외부에서 접속 가능

> 웹(준비 중...) : $ npm start
