-- SELECT INSERT(a, b, c, d)
-- 문자열 a에서 b번째 글자부터 c만큼의 글자를(띄어쓰기 포함) 원래 그 자리의 글자 대신 d를 삽입한다. 
SELECT INSERT('Hello justin', 6, 0, ' There');
SELECT INSERT('Hello justin', 6, 3, ' There');

-- 오른쪽과 왼쪽에서 특정 글자만큼 출력
SELECT LEFT('omglol!', 3);
SELECT RIGHT('omglol!', 4);
SELECT LEFT(author_lname, 1) FROM books;
SELECT SUBSTR(author_lname, 1, 1) FROM books;

-- 같은 글자 반복
SELECT REPEAT('ha', 5);

-- 필요없는 빈칸 삭제
SELECT TRIM('     wow   ');

