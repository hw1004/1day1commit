-- 1. 책 제목의 공백을 ->로 바꿔서 출력
SELECT replace(title, ' ', '->') AS 'title' FROM books;

-- 2. 작가의 성(lname)을 제대로/거꾸로 출력
SELECT author_lname AS 'forwards',
	   reverse(author_lname) AS 'backwards' 
       FROM books;
       
-- 3. 풀네임을 모두 대문자로 출력
SELECT UPPER(CONCAT(author_fname, ' ', author_lname)) AS 'full name in caps' FROM books;

-- 4. 책 제목과 출간 연도를 조합하여 문장으로 출력
SELECT CONCAT(title, ' was released in ', released_year) AS 'summary' FROM books;

-- 5. 책 제목과 제목 글자수를 출력
SELECT title, CHAR_LENGTH(title) AS 'character count' FROM books;

-- 6. 3개의 컬럼
-- a. 짧은 제목(10글자...)
-- b. 작가 이름 성, 이름alter
-- c. 재고를 12 in stock와 같이 표현
SELECT CONCAT(SUBSTR(title, 1, 10),'...') AS 'short title',
	   CONCAT(author_lname, ', ', author_fname) AS author,
       CONCAT(stock_quantity, ' in stock') AS quantity 
       FROM books;