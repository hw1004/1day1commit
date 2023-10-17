-- 길이를 알려줌
SELECT CHAR_LENGTH('qwer');
SELECT LENGTH('qwer');

-- 영어가 아닌 다른 언어들 중에는 LENGTH가 다르게 나오는 경우가 있다.
-- 따라서 대체적으로 CHAR_LENGTH를 이용하여 길이를 출력해야 정확하게 나온다.
SELECT LENGTH('가나다');
SELECT CHAR_LENGTH('가나다');

SELECT CHAR_LENGTH(title) AS 'title length', title FROM books;
