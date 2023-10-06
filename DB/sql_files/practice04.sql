-- practice04.sql

USE pet_shop;

SELECT id FROM cats;
SELECT name, breed FROM cats;
SELECT name, age FROM cats WHERE breed = 'Tabby';
SELECT id, age FROM cats WHERE id = age;

SELECT id AS '번호', age AS '나이'
FROM cats WHERE id = age;

