-- practice01.sql

-- 1. practice db 생성
-- 2. practice db로 이동
-- 3. 테이블 people 생성
	-- 1. first_name => 글자 20
    -- 2. last_name => 글자 20
    -- 3. age => 정수 
-- 4. 테이블 정보 확인
-- 5. 테이블 삭제

CREATE DATABASE practice_db;

SHOW DATABASES;

USE practice_db;

CREATE TABLE people (
first_name VARCHAR(20),
last_name VARCHAR(20),
age INT
);

DESCRIBE people;

DROP TABLE people;

SHOW TABLES;