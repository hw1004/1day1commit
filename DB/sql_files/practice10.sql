-- 1. 1980년 이전(미만)에 출간된 모든 책의 수
SELECT COUNT(*) AS counter FROM books WHERE released_year < 1980;

-- 2. 작가 성이 Eggers이거나 Chabon인 모든 책 조회
SELECT id, title, author_fname, author_lname, released_year FROM books
WHERE author_lname = 'Eggers' OR author_lname = 'Chabon';

-- 3. 작가 성 Lahiri가 2000년 이후 출간한 모든 책 조회
SELECT id, title, author_fname, author_lname, released_year, stock_quantity, pages
FROM books
WHERE author_lname = 'Lahiri'
AND released_year >= 2000;

-- 4. 책 페이지가 100 이상 200 이하인 모든 책의 제목, 페이지 수 조회
SELECT title, pages
FROM books
WHERE pages BETWEEN 100 AND 200;

-- 5. 작가의 성이 'C'나 'S'로 시작하는 작가의 모든 책의 제목과 성 조회
SELECT title, author_lname
FROM books
WHERE author_lname LIKE 'C%'
OR
author_lname LIKE 'S%';

-- 6. 3개의 컬럼
-- a. title: 제목
-- b. stock_quantity: 재고 수
-- c. type: 다음 조건에 따라 결정
-- 제목에 stories가 들어가면 TYPE 'A'
-- 제목에 Kids나 Heartbreaking이 들어가면 TYPE 'B'
-- 그 외에는 C
SELECT title, stock_quantity, 
	CASE
		WHEN title LIKE '%stories%' THEN 'A'
        WHEN title LIKE '%Kids%' OR title LIKE '%Heartbreaking%' THEN 'B'
        ELSE 'C'
    END AS 'type'
FROM books;