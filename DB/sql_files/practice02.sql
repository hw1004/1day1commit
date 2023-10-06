-- practice02.sql

-- 1. practice db 사용
USE practice_db;
-- 2. 테이블 people 생성
CREATE TABLE people(
first_name VARCHAR(20),
last_name VARCHAR(20),
age INT
);
-- 3. first_name VARCHAR(20)
-- 4. last_name VARCHAR(20)
-- 5. age INT
-- 6. 테이블 확인
DESC people;
-- 7. 데이터 입력
INSERT INTO people (first_name, last_name, age)
VALUES
('혜원', '정',21),
('예솔', '박', 21),
('현아', '황', 21);
-- 8. people 테이블의 모든 데이터 조회
SELECT * FROM people;

