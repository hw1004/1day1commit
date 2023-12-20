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
2. **Hadoop HDFS**: **분산저장 처리**를 위한 모듈 (여러개의 서버를 하나의 서버처럼 묶어서 데이터 저장)
   - namenode : metadata, datanode 관리 (데이터를 읽고 쓸 수 있음)
   - datanode : 파일 block 단위로 저장
3. **Hadoop YARN**: **병렬처리**를 위한 클러스터 자원관리, 스케줄링 담당
4. **Hadoop Mapreduce**: 분산되어 있는 데이터의 **병렬 처리**를 도와주는 **분산 처리 모듈**
5. Hadoop Ozone: object storage for Hadoop

![](https://media.geeksforgeeks.org/wp-content/uploads/had.jpg)

## Apache Spark
> 오픈 소스 클러스터 컴퓨팅 프레임워크 (SQL, 스트리밍, 머신러닝, 그래프 처리를 위한 모듈이 있는 데이터 처리용 분석 엔진)
>
> 높은 수준의 API를 제공하는 오픈소스 범용 **분산 처리 시스템**
>
> Apache Kafka가 실시간으로 생성한 데이터 스트림에 대한 데이터 처리 수행한다.

## Apache Kafka
> 실시간으로 발생하는 이벤트에 대한 오픈 소스 분산 **스트리밍** 플랫폼