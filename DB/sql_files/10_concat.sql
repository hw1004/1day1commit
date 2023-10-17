-- concat의 요소들을 합친다.
SELECT CONCAT('s', 'q', 'l');

SELECT CONCAT(author_fname, '!!!') FROM books;

SELECT CONCAT(author_fname, ' ', author_lname) AS full_name FROM books;

# seperator와 같이 CONCAT
SELECT CONCAT_WS(' ', 's', 'q', 'l');
SELECT CONCAT_WS('-', title, author_fname, author_lname) AS summary FROM books;

