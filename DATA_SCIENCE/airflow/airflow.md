# airflow
## airflow 구성
1. 웹서버: 스케줄러에서 분석한 Dag를 시각화하고 DAG 실행과 결과를 확인할 수 있는 interface 제공
2. 스케줄러: DAG를 분석하고 현재 시점에서 Dag의 스케줄이 지난 경우 airflow worker에 DAG의 테스크를 예약함
3. Worker: 예약된 테스크를 실제로 실행시키는 것
4. Metastore: 에어플로에 있는 Dag, Task 등의 메타데이터 관리
5. Executor: 태스크가 어떻게 실해되는지 정의
## DAG(Directed Acyclic Graph)
- airflow에서 실행할 작업들을 **순서에 맞게** 구성한 workflow
- DAG를 구성하는 각 작업들을 task라고 함

## Data Pipeline
1. 수집 후 DL(hdfs)에 저장하는 프로그램 (corona_extract.py)
   - api 또는 page 크롤링 후 data hdfs에 저장
2. DL(HDFS)에 저장된 파일을 DW DB에 변환 저장하는 프로그램 (corona_transform_dw.py)
3. DW에 저장된 파일을 dm db에 변환 저장하는 프로그램 (corona_transform_dm.py)
   - dw db 테이블 data를 가공 처리하여 dm db에 저장한다.

> 위 작업 pipline을 airflow task로 구성하여 연결한다.