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

## 집계 함수 (Aggregated Function)
1. **COUNT**
> 개수를 세는 함수

- `SELECT count(title) FROM books WHERE title LIKE '%the%'`: the를 포함하는 title의 개수 count
- 집계함수와 집계 함수가 아닌 함수는 GROUP BY 없이 동시에 조회 불가

2. **GROUP BY**
> 특정 column을 기준으로 같은 값을 가지는 column 값들로 Group을 만드는 것

- `SELECT author_lname, COUNT(*) FROM books GROUP BY author_lname, author_fname;`: author_lname과 author_fname이 같은 것끼리 group을 지어서 author_lname과 특정 full name을 가지는 책의 개수 count
- 가상의 column (CONCAT)에서도 가능하다.

3. **MIN MAX**
> 최대, 최솟값

- `SELECT MIN(released_year) AS '최고'`: 가장 오래된 책 반환
- `SELECT MAX(released_year) AS '최소'`: 가장 최근의 책 반환

4. **SUBQUERY**
> WHERE절에 SELECT문이 들어가는 서브쿼리문으로 aggregated 함수를 사용할 때 유용하게 사용된다.

- `SELECT title, pages FROM books WHERE pages = (SELECT MAX(pages) FROM books);`: WHERE 구문에 SELECT문이 들어가는 subquery문을 사용하여 전체 데이터에서 가장 페이지 수가 많은 책의 제목과 페이지 수를 함께 반환할 수 있다.

5. **SUM**
> 특정 column듸 값들의 전체 합계

- `SELECT SUM(pages), SUM(stock_quantity) FROM books`: 모든 책의 페이지수와 재고 수의 합계를 반환한다.

6. **AVG**
> 특정 column의 값들에 대한 평균

- `SELECT AVG(pages) FROM books;`: 전체 책들의 평균 페이지 수 반환

## 논리 연산자 Operators
|operators|description|
|---|---|
|`+`|더하기|
|`-`|빼기|
|`*`|곱하기|
|`/`|나누기|
|`%`|나머지|
|`DIV`|몫|
|`POW(a, b)`|a의 b제곱|
|`IS NULL`|WHERE title IS NULL 하면 title이 NULL 이 아닌 값|
|`!=`|여집합|
|`>`, `<`|GT, LT ~보다 크다/~보다 작다|
|`>=`, `<=`|GTE, LTE ~보다 크거나 같다/~보다 작거나 같다|
|`AND`|여러개의 조건을 다 만족시켜야 할 때|
|`OR`|조건들 중 하나만 성립하여도 될 때|
|`BETWEEN A AND B`|특정 칼럼의 값이 특정한 범위 내에 존재해야 할 때|
|`NOT BETWEEN A AND B`|여집합|
|`IN`|여러개의 보기 중에 특정 column의 값이 존재하면 사용|

### CASE
```
SELECT title, stock_quantity, 
	CASE
		  WHEN stock_quantity <= 40 THEN '*'
        WHEN stock_quantity <= 70 THEN '**'
        WHEN stock_quantity <= 100 THEN '***'
        WHEN stock_quantity <= 140 THEN '****'
        ELSE '*****'
	END AS stars
FROM books
ORDER BY stars;
```

## 제약조건 (Constraints)
### UNIQUE
> table을 생성할 때 생성되는 COLUMN에 UNIQUE 조건이 있으면 중복을 허용하지 않는다.

```
CREATE TABLE contacts (
	name VARCHAR(100) NOT NULL,
	phone VARCHAR(15) NOT NULL UNIQUE
);
```

### CHECK
> 제약조건을 생성할 때 확인(체크) 해야할 조건식을 작성한다.
> 여러개의 column에 대한 제약조건이 걸릴 시 두번째 코드와 같이 나타날 수 있다.

```
CREATE TABLE palindrome2 (
  word VARCHAR(100) NOT NULL,
  CONSTRAINT word_must_be_palindrome CHECK(REVERSE(word) = word)
);
```
```
CREATE TABLE companies (
	name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    CONSTRAINT name_and_address_cannot_be_same UNIQUE (name, address)
);
```

## 수정 ALTER
1. `ALTER TABLE companies ADD COLUMN phone VARCHAR(20);`: COLUMN 추가
2. `ALTER TABLE companies DROP COLUMN phone;`: COLUMN 삭제
3. `ALTER TABLE companies RENAME COLUMN name TO company_name;`: COLUMN명 변경
4. `ALTER TABLE companies MODIFY company_name VARCHAR(100) DEFAULT '???';`: default 값을 추가로 주거나 데이터 타입의 범위 같은 것을 수정할 때
5. `ALTER TABLE companies CHANGE company_name name VARCHAR(255) DEFAULT '???' NOT NULL;`: COLUMN명 변경하고 DEFAULT나 NULL 조건 추가하거나 데이터 타입의 범위 같은 것 동시에 수정할 때
6. `ALTER TABLE companies ADD CONSTRAINT positive_buy_price CHECK (buy_price >= 0);`: 제약조건 추가할 때
7. `ALTER TABLE companies DROP CONSTRAINT positive_buy_price;`: 테이블에 부여된 제약조건을 취소할 때