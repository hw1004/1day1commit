-- 첫번째 원소에서 두번째 원소를 세번째 원소로 바꾸어 적용한다.
SELECT REPLACE('HELLO WORLD', 'HELL', '****');
SELECT REPLACE('apple', 'p', 'P');

SELECT REPLACE(title, ' ', '-') AS 'new title' FROM books;