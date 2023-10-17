-- SELECT SUBSTR(<str>, <start>, <length>)
-- SELECT SUBSTR(<str>, <start>)

-- 시작점부터 N개
SELECT SUBSTR('HELLO, WORLD', 2, 4);
SELECT SUBSTR('HELLO, WORLD', 1, 4);

-- 시작점 지정
SELECT SUBSTR('HELLO, WORLD', 8);
SELECT SUBSTR('HELLO, WORLD', -5);
SELECT SUBSTR('HELLO, WORLD', -5, 2);

SELECT CONCAT(SUBSTR(title, 1, 10), '...') AS 'short title',
	   CONCAT(SUBSTR(author_lname,1, 1), '. ', author_fname) AS 'name' 
       FROM books;