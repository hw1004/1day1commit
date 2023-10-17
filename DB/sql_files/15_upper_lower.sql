-- 대소문자로 변환
SELECT UPPER('hello');
SELECT LOWER('WORLD');

SELECT UPPER(title) AS upper_title FROM books;
SELECT LOWER(title) AS upper_title FROM books;

-- 'I LOVE <BOOK_TITLE>!!!'
SELECT CONCAT('I LOVE ', UPPER(title), '!!!') AS 'I LOVE BOOK' FROM books;