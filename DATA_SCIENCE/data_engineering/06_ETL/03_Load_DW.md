# Load DataWarehouse
> datawarehouse database account
```
# mysql에서 진행
## 새로 user 생성 후 접속해야 함
mysql> create user bigMysql@'%' identified by 'bigMysql1234@';
mysql> grant all privileges on *.* to bigMysql@'%' with grant option;
## 사용할 database 생성
mysql> create database etlmysql;
```
> JDBC(Java Database Connectivity) DICT
>
> 자바 프로그램과 데이터베이스가 연결되어서 데이터를 주고 받을 수 있게 해주는 프로그래밍 인터페이스(응용 프로그램과 DBMS 간에 translate 역할을 함)
```
JDBC = {
      'url':'jdbc:mysql://localhost:3306/etlmysql?characterEncoding=utf8&serverTimezone=Asia/Seoul'
     ,'props':{
      'user':'bigMysql',
      'password':'bigMysql1234@'   
      }
}

```

1. LOC 테이블 저장
   - hdfs에 csv 파일로 저장해 놓은 파일을 호출해서 **필요한 columns** 추출하고 db table에 저장한다.
   - `csvfile = spark.read.csv(경로, encoding='CP949', header=True)`
   - 필요한 컬럼만 저장
   - `necessary_cols = csvfile.join(othercsv, on='loc')`: loc 컬럼 기준으로 csvfile, othercsv 파일 조인
   - `necessary_cols.select(col('loc').alias('LOC'), col('area').alias('AREA'))`
2. spark.dataframe을 dbms의 table에 저장
   - `necessary_cols.write.mode('overwrite').jdbc(url=JDBC['url'], table='LOC', properties=JDBC['props'])`
   - db 주소, 테이블명, 계정 연결 정보 입력
   - overwrite: 기존 테이블이 있으면 해당 테이블에 새로 저장되는 레코드로 덮어쓴다.