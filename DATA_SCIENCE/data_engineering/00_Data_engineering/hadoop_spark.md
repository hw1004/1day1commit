## Hadoop 실행
1. `jps`: 자바로 실행되는 java virtual machine process 보여줌 (프로세스 확인)
2. `service ssh start`: linux에서 ssh 서비스 시작
3. `service mysql start`: linux에서 mysql 시작
4. `start-all.sh`하고 `jps` 확인 (모든 Hadoop cluster의 HDFS 시작, 맵리듀스 모두 실행)
5. `pyspark`: pyspark는 python 환경에서 Apache Spark를 사용할 수 있는 interface (파이썬 API를 활용한 빅데이터 분산처리 플랫폼)
   ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbSFFjF%2Fbtrs9hNuWF1%2Fb6kBs3Kjpejd97UVz4mMC0%2Fimg.png)
6. `stop-all.sh`: HDFS, 맵리듀스 모두 중단

## Pyspark
> 파이썬 API를 활용한 빅데이터 분산처리 플랫폼

<기능 및 라이브러리>
- **PySparkSQL**: 대용량 정형 데이터 처리를 위해 SQL 인터페이스 지원하는 라이브러리
  - **데이터프레임**을 데이터 표현 형식으로 도입하여 RDBMS의 테이블과 유사한 2차원 구조임
- **Pandas API**: Pandas 기능
- **MLlib**: 머신러닝 라이브러리 (Classification, Regression, Clustering, Dimension Reduction, Optimization 등 다양한 머신러닝 알고리즘 제공)
- **GraphFrame**: 데이터프레임 기반 그래프 분석 지원하는 Spark package