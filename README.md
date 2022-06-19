
## 결과(Slack api 호출)
<img src="[https://user-images.githubusercontent.com/52682603/138834243-fb74d81e-e90d-4c6a-8793-05df588f59ab.png](https://user-images.githubusercontent.com/50035753/173994748-d0f9832a-18fa-41e3-b61d-35623d2f4bbc.png)" alt="slack_capture" width=50%>

슬랙 api 호출 결과입니다. 실시간 카드 사용 내역을 슬랙 bot이 전달합니다.

## 과정
<img src="[https://user-images.githubusercontent.com/52682603/138834262-a7af2293-e398-416d-8dd3-ff5fab8cb80d.png](https://user-images.githubusercontent.com/50035753/174471284-c93dbfab-da4a-4ddd-a91c-c6e5d73abf42.jpg)" alt="description" width=50%>

Before & After 비교입니다. 기존에는 카드사에서 알림 내역을 다이롂트로 SMS 문자로 전달 받았습니다.
제가 구축한 프로젝트는 알림 내역을 카드사 앱 알림으로 받아서, 안드로이드 push notification forward 앱을 통해 FastAPI로 구축된 서버로 보냅니다.(post 요청)

그런 다음 Sqlite DB에 사용 시간, 내역 등을 파싱하여 저장하고 및 슬랙 Webhook을 보내어 가계부 입력을 자동화 시킵니다.

## 실행 방법

### Prerequisite

1. pip install fastapi
2. pip install uvicorn[standard]
3. pip install sqlalchemy
4. Node.js

> 서버(infp에서) : $ uvicorn api-server.main:app --reload --host 0.0.0.0

host 0.0.0.0 해주어야 외부에서 접속 가능

> 웹(준비 중...) : $ npm start
