-- GROUP BY 없이 사용
SELECT MIN(released_year) FROM books;
SELECT MAX(pages) FROM books;
-- 문자열은 알파벳 순으로 min, max
SELECT MIN(author_lname), MAX(author_lname) FROM books;

-- GROUP BY 함께 사용
-- 작가별 출판한 책 수, 가장 오래된 책, 책 출판 년도, 가장 최근 책 출판년도
-- SELECT 뒤에 1) aggregate, 2) grouped col 나올 수 있음
SELECT author_lname AS '성',
author_fname AS '이름',
COUNT(title) AS '책 수',
MIN(released_year) AS '최고',
MAX(released_year) AS '최신'
FROM books
GROUP BY author_lname, author_fname;

-- 가장 페이지가 긴 책의 제목
SELECT title, pages FROM books ORDER BY pages DESC LIMIT 1;
-- 같은 페이지가 여러개 일 때 정확한 답이 안 나옴(중복을 못 잡음)

-- 2줄 쿼리
SELECT MAX(pages) FROM books;
SELECT title, pages FROM books
WHERE pages=634;

