USE book_shop;
-- Aggregate function 집계합수
SELECT COUNT(*) FROM books;
SELECT COUNT(id) FROM books;
SELECT COUNT(DISTINCT author_lname) FROM books;

SELECT COUNT(title) FROM books WHERE title LIKE '%the%';

-- Error(aggregated - non aggregated는 동시에 조회 불가)
-- SELECT COUNT(*), title FROM books WHERE title LIKE '%the%';

