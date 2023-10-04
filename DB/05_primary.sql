-- 05_primary.sql

INSERT INTO dogs4()
VALUES (), (), (), ();

SELECT * FROM dogs4;

CREATE TABLE dogs5 (
	ID INT NOT NULL PRIMARY KEY,
	name VARCHAR(20) NOT NULL DEFAULT 'No Name',
    age INT NOT NULL DEFAULT '0'
);

-- Primary Key는 중복되면 안되는 값이다.

INSERT INTO dogs5 (ID, name, age)
VALUES
	(1, '골드', 3),
    (2, '실버', 3);
    
SELECT * FROM dogs5;

INSERT INTO dogs5(id, name, age)
VALUES(100, '브론즈', 3);

CREATE TABLE uniq_dogs (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL DEFAULT '멍멍이',
    age INT NOT NULL DEFAULT '0'
);

DESC uniq_dogs;

INSERT INTO uniq_dogs (name, age)
VALUES
	('골드', 3),
    ('실버', 4),
    ('브론즈', 5);

INSERT INTO uniq_dogs ()
VALUES (), (), (), ();

SELECT * FROM uniq_dogs;