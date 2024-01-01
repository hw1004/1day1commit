# logger 사용
- log를 기록해주는 객체(관련 패키지: logging)
- 사용자 정의 log 사용의 필요성: 외부 연결 시 오류상태 확인하기 위해서
- restapi는 외부 서버 연결 -> log 기록됨

### 로그 관련 디렉터리 생성하고 로그 기록
1. `import logging`: 로그 관련 패키지 import
2. `loggig.getLogger('corona_api')`: 로그 관리 객체 logger 생성한다.
3. `f_handler = logging.FileHandler('./log/rest_api' + cal_std_day(0) + '.log')`: 로그 파일 핸들러 생성한다.
4. `logger.addHandler(f_handler)`: logger에 위에 만들어 둔 로그 파일 핸들러를 추가한다.