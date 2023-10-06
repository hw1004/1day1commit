-- 03_Null.sql

USE pet_shop;

INSERT INTO dogs1 (name, breed)
VALUES ('멍뭉이', '시고르');

INSERT INTO dogs1() VALUES();

SELECT * FROM dogs1;
-- New Table
CREATE TABLE dogs2(
	name VARCHAR(20) NOT NULL,
    age INT NOT NULL
);

DESC dogs2;

INSERT INTO dogs2(name) VALUES ('doggy');  # NULL 허용해주지 않음
INSERT INTO dogs2(name, age) VALUES ('dog', 10);
SELECT * FROM dogs2;
