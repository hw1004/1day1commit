## Data Lake vs Data WareHouse vs DataMart
![](https://panoply.io/uploads/versions/diagram8-1---x----750-376x---.jpg)
1. Data Lake: 원시/비정형 정보를 보관하는 데이터 저장소 (텍스트 문서, 이미지, 비디오, 오디오 등 다양한 유형의 정보 저장)
2. Data WareHouse: 전체 비즈니스에 대한 정보를 저장하는 광범위한 데이터 시스템 (원시 정보 수집 -> 테이블 형식의 정형데이터로 저장)
3. Data Mart: 최종 업무에 활용하는 데이터를 포함하는 데이터 저장소 시스템

## Apache Hadoop
> **분산** 응용 프로그램을 지원하는 자바 소프트웨어 프레임워크
>
> 적당한 성능의 컴퓨터 여러대를 **클러스터화**하고, 큰 크기의 데이터를 클러스터에서 병렬로 동시에 처리해서 처리 속도를 높이는 것을 목적으로 함
>
> ETL(Extract Transform Loading) 작업을 Hadoop을 이용해서 진행하고 Data Mart로 넘어간다.

### Hadoop 주요 모듈(프로세스)
1. Hadoop Common: common component module
2. **Hadoop HDFS (파일 시스템)**: **분산저장 처리**를 위한 모듈 (여러개의 서버를 하나의 서버처럼 묶어서 데이터 저장)
   - namenode : metadata, datanode 관리 (데이터를 읽고 쓸 수 있음)
   - datanode : 파일 block 단위로 저장
3. **Hadoop YARN (리소스 관리)**: **병렬처리**를 위한 클러스터 자원관리, 스케줄링 담당
4. **Hadoop Mapreduce (연산 엔진)**: 분산되어 있는 데이터의 **병렬 처리**를 도와주는 **분산 처리 모듈**
5. Hadoop Ozone: object storage for Hadoop

![](https://media.geeksforgeeks.org/wp-content/uploads/had.jpg)

## Apache Spark (연산 엔진)
> 오픈 소스 클러스터 컴퓨팅 프레임워크 (SQL, 스트리밍, 머신러닝, 그래프 처리를 위한 모듈이 있는 데이터 처리용 분석 엔진)
>
> 높은 수준의 API를 제공하는 오픈소스 범용 **분산 처리 시스템**
>
> Apache Kafka가 실시간으로 생성한 데이터 스트림에 대한 데이터 처리 수행한다.

- 데이터를 여러개로 분리해서 여러 노드의 메모리에서 동시에 처리한다.

### **RDD (Resilient Distributed Dataset)** 
- spark가 사용하는 핵심 데이터 모델로 다수의 서버에 걸쳐 분산 방식으로 저장된 데이터 요소들의 집합이다.
  - 여러 분산 노드에 걸쳐 저장
  - 변경 불가능
  - 여러 개의 파티션으로 분리
  - 처리할 때는 동시에 병렬로 처리할 수 있음
  - **데이터 추상화**: 데이터는 클러스터에 흩어져 있지만 하나의 파일인 것처럼 사용한다.
  - 결과가 필요할 때까지 연산하지 않음(**지연연산**)
    - Transformation: 결과값으로 새로운 rdd 반환 (결과값 필요할 때까지 연산법만 기억)
    - Action (ex. collect()): 즉시 실행
    - ![](https://miro.medium.com/v2/resize:fit:726/1*BaQ7kuuENGOWbV7JII0gEA.png)

- **Key와 Value 쌍을 가지고 있을 수 있음 (pair RDD)**
  - `reduceByKey()`: 키 값 기준 연산 처리
  - `groupByKey()`: 키 값 기준으로 value group by 진행
  - `sortByKey()`: 키 값 기준으로 정렬
1. Data-parallel: 데이터를 여러개로 쪼개서 작업하고 결과값을 반환 받아 합침
   - `sc.parallelize()`: 파이썬 객체를 spark cluster로 가져옴
   - `getNumPartitions()`: partition 개수 반환
   - `collect()`: 데이터 반환
2. Data-Distributed: 데이터를 여러개로 쪼개서 여러 노드로 보내고 독립적으로 작업한 후 결과값을 반환 받아 합침

## Apache Kafka
> 실시간으로 발생하는 이벤트에 대한 오픈 소스 분산 **스트리밍** 플랫폼