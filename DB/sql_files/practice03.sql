-- practice03.sql

-- practice db에서 진행
USE practice_db;
-- 테이블 이름 employees
-- 컬럼
-- id (숫자, pk, 자동오름)
-- last_name (문자, 필수)
-- first_name (문자, 필수)
-- middle_name (문자, 필수 아님)
-- age (숫자, 필수)
-- status (문자, 필수, 기본 값 working)
CREATE TABLE employees (
	id INT AUTO_INCREMENT PRIMARY KEY,
    last_name VARCHAR(20) NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    middle_name VARCHAR(20),
    age INT NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'working'
);

DESC employees;
-- test insert
INSERT INTO employees(first_name, last_name, age)
VALUES ('Dora', 'Smith', 58);

SELECT * FROM employees;