-- 2줄 쿼리
SELECT MAX(pages) FROM books;
SELECT title, pages FROM books
WHERE pages=634;

-- 1줄로
SELECT title, pages FROM books
WHERE pages = (SELECT MAX(pages) FROM books);

-- 가장 오래된 책은?
SELECT title, released_year FROM books
WHERE released_year = (SELECT MIN(released_year) FROM books);