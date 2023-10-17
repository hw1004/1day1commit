SELECT book_id, author_fname, author_lname FROM books;
SELECT book_id, author_fname, author_lname FROM books ORDER BY author_fname;

-- 기본값 오름차순
SELECT book_id, author_fname, author_lname FROM books ORDER BY author_fname ASC;

-- 내림차순
SELECT book_id, author_fname, author_lname FROM books ORDER BY author_fname DESC;

SELECT * FROM books ORDER BY stock_quantity;
SELECT * FROM books ORDER BY stock_quantity DESC;

-- ORDER BY 기준이 되는 칼럼을 숫자로 지정(비추)
SELECT book_id, pages, author_fname, author_lname
FROM books ORDER BY 2 DESC;

-- 여러 컬럼으로 정렬
SELECT author_lname, released_year, title FROM books
order by author_lname;
-- 기준에 따라 정렬한 다음에는 id 순으로 자동정렬한다.
SELECT author_lname, released_year, title FROM books
order by author_lname, released_year;
-- 여러개의 컬럼 기준에 따른 정렬은 작성 순서대로 정렬한다.(우선순위)

SELECT author_lname, released_year, title FROM books
order by author_lname, released_year DESC;

-- 가상의 컬럼으로도 정렬 가능alter
SELECT book_id, CONCAT(author_fname, ' ', author_lname) AS author
FROM books ORDER BY author;