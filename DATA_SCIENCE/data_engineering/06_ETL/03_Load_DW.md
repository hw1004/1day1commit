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
   - 