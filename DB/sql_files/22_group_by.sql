SELECT author_lname FROM books;
SELECT author_lname FROM books GROUP BY author_lname;
SELECT DISTINCT author_lname FROM books;

-- 작가별 책이 많은 수
SELECT author_lname, COUNT(title) AS counter 
FROM books GROUP BY author_lname 
ORDER BY counter DESC;
-- full name으로 책의 개수 측정
SELECT author_lname, COUNT(*) FROM books
GROUP BY author_lname, author_fname;

SELECT author_lname, author_fname, COUNT(*) FROM books
GROUP BY author_lname, author_fname;

-- 가상의 column에서도 가능
SELECT CONCAT(author_lname, ' ', author_fname) AS fullname, COUNT(*)
FROM books
GROUP BY fullname;