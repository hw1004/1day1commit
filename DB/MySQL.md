# MySQL
## CRUD
### Database 생성과 Table 생성

1. **Database**
   1. `SHOW DATABASES;` : 데이터베이스의 목록을 보여줌
   2. `CREATE DATABASE database_name;` : DB 생성
   3. `DROP DATABASE database_name;` : DB 제거
   4. `USE database_name;` : Table을 생성하는 것과 같은 일을 수행할 데이터베이스를 선택한다.
2. **Table**
   1. ```
      CREATE TABLE table_name (
        name VARCHAR(20),
        age INT
      );
      ```
      Table의 이름과 칼럼명 생성
   2. `SHOW TABLES;` : 테이블의 목록을 보여줌
   3. `DESC table_name;` : 특정한 테이블을 분석해줌.
   4. `DROP TABLE table_name` : 테이블 제거
   5. `INSERT INTO table_name (name, age) VALUES (val1, val2);` : 테이블의 row 값들 삽입
   6. `SELECT * FRROM table_name;` : 특정한 테이블의 모든 row 출력
3. **NULL**
    -  ```
        CREATE TABLE table_name(
          name VARCHAR(20) NOT NULL,
          age INT NOT NULL
        );
       ```
      `NOT NULL`을 특정 칼럼에 설정해 줄 수 있음. 그러면 NULL 값을 허용해주지 않아 특정 칼럼은 **필수**적으로 insert되어야 할 칼럼임을 명시해줌.
4. **DEFAULT**
    - table을 생성할 때 `name VARCHAR(20) DEFAULT 'No name'`으로 기본값을 설정해줄 수 있음. 
5. **Primary Key**
   1. table을 생성할 때 `id INT NOT NULL PRIMARY KEY`로 작성하면 id가 primary key로 지정이 되고 중복을 허용하지 않는 id값이 된다.
   2. `id INT NOT NULL AUTO_INCREMENT PRIMARY KEY`로 지정하면 id 값이 1부터 순차적으로 저절로 늘어나는 primary key가 된다.

### Table 조회와 수정, 삭제
1. Read 조회
   - `SELECT * FROM <table>`로 table을 조회할 수 있다. 
   - `*` 대신에 `name, age`와 같은 요소들을 삽입하여 특정 칼럼들만 조회할 수 있다.
   - `SELECT * FROM <table> WHERE <condition>` 에서 조건을 설정하여 조건을 만족하는 row들만 조회할 수 있다.
   - `SELECT name AS '이름'`을 통해 조회되는 Table의 칼럼명을 지정할 수 있다.
2. Update 수정
   - `UPDATE <table> SET <col>=<val> WHERE <condition>` : 조건을 만족하는 칼럼들의 값을 `<val>`로 수정한다. 
3. Delete 삭제
   - `DELETE FROM <table> WHERE <condition>` : 조건을 만족하는 row를 삭제할 수 있다.
   - `DELETE FROM <table>`을 통해 전체 테이블의 데이터를 삭제할 수 있다. Table의 구조를 지우는 것은 아니며 Table 전체를 없애고 싶을 때는 `DROP TABLE <table>`을 사용한다.


## 문자열 함수 다루기
1. **CONCAT**
> 요소들을 하나로 합치는 SQL문

- `SELECT CONCAT('S', 'Q', 'L')`의 결과값은 SQL
- `SELECT CONCAT_WS('-', title, author_fname) AS summary FROM books`: books라는 테이블에서 title과 author_fname을 '-'로 연결하고 그것을 summary라는 column으로 출력함. (`CONCAT_WS`는 seperator로 요소를 합치는 SQL문이다.)

2. **SUBSTR**
> 요소의 특정 범위를 불러오는 SQL문

- `SELECT SUBSTR('HELLO, WORLD', 2, 4)`: 두번째 글자부터 4개의 글자를 출력함
- `SELECT SUBSTR('HELLO, WORLD', 8)`: 시작점 지정(8번째 글자부터 끝까지)

3. **REPLACE**
> 요소의 특정 부분을 다른 요소로 바꾸어 출력한다.

- `SELECT REPLACE('HELLO WORLD', 'HELL', '****')`: HELLO WORLD의 HELL 부분을 `****`로 바꾸어 ****O world가 된다.

4. **REVERSE**
> 역순으로 출력한다.

- `SELECT REVERSE('APPLE')`: ELPPA를 출력한다.

5. **CHAR LENGTH**
> 길이를 출력한다.

- `LENGTH`로도 길이가 출력되지만 영어 이외의 언어들 중 `LENGTH`와 `CHAR_LENGTH`의 결과가 다르게 나오는 언어들이 있기 때문에 `CHAR_LENGTH`를 사용한다.

6. **UPPER LOWER**
> 대소문자 변환

- `UPPER()`은 요소의 모든 글자를 대문자로 반환한다.
- `LOWER()`은 요소의 모든 글자를 소문자로 반환한다.

7. **INSERT**
> 요소의 특정 범위에 원래 그 범위에 있던 글자들을 다른 글자들로 삽입한다.

```
SELECT INSERT('Hello justin', 6, 0, ' There');
# Hello There justin으로 6번째인 빈칸 앞에 ' There'을 삽입

SELECT INSERT('Hello justin', 6, 3, ' There');
# Hello Therestin으로 6번째 글자부터 3글자인 ' ju' 부분 대신에 ' There'을 삽입
```

8. **LEFT RIGHT**
> 오른쪽과 왼쪽에서 특정 글자만큼 출력

- `LEFT('HELLO', 3)`은 왼쪽부터 3글자인 'HEL'을 반환
- `RIGHT('HELLO', 3)`은 오른쪽부터 3글자인 'LLO'를 반환

9. **REPEAT**
> 같은 글자 반복

- `SELECT REPEAT('HA', 5)`: 'HA'를 5번 반복하여 'HAHAHAHAHA'를 반환

10. **TRIM**
> 필요없는 빈칸 삭제

- `SELECT TRIM('   WOW  ')`: 필요없는 빈칸을 제거하고 'WOW'만 반환


## 선택사항 정교화
1. **DISTINCT**
> 고유한/중복 없이 데이터 반환

- `SELECT DISTINCT author_fname, author_lname FROM books`: 한 개 이상의 요소들의 중복을 체크하여 중복 없이 반환한다. 위의 경우 author_fname과 author_lname 두 값이 모두 중복되는 값을 제거하고 반환한다.

2. **ORDER BY**
> 정렬

- `SELECT * FROM books` 뒤에 오며 `ORDER BY author_lname` 처럼 정렬 기준을 설정한다.
- 오름차순 `ASC`가 기본값이며 내림차순은 `DESC`를 통해 설정해준다.
- 여러개의 칼럼 및 CONCAT 칼럼이 포함되었을 때도 정렬 가능하다.

3. **LIMIT**
> 출력하고자 하는 요소의 수를 제한한다.

- `SELECT * FROM books`, `ORDER BY` 뒤에 오며 `LIMIT 5`로 출력되는 요소의 수를 제한한다.
- `LIMIT 5`: 앞의 5개만 출력한다.
- `LIMIT 5, 5`: 앞의 5개는 건너뛰고 6번째부터 5개의 요소만 출력한다.

4. **LIKE**
> 특정 요소가 포함되어 있는 데이터들을 출력한다.

- 완전히 조건과 동일한 요소 출력
  - `SELECT * FROM books WHERE author_fname = 'Dave';`
- 패턴 탐색
  - `LIKE` 사용하여 유사성 확인
  - `%`: 0~N 개 뭐라도 올 수 있음
  - `_`: 정확히 한 글자만 올 수 있음
  - `SELECT * FROM books WHERE author_fname LIKE '%da%'`
