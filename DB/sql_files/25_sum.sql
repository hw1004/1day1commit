-- GROUP BY 없을 경우
SELECT SUM(pages), SUM(stock_quantity) FROM books;

-- GROUP BY 있을 경우
-- 작가 별 재고 수의 총 합
SELECT 
	author_fname,
    author_lname,
    SUM(stock_quantity)
FROM books
GROUP BY author_fname, author_lname;

