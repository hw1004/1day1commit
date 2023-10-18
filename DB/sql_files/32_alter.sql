DESC houses;

ALTER TABLE companies
ADD COLUMN phone VARCHAR(20);

-- 논리적 오류 (명시적이지 않음)
-- default 준 적 없는데 Null에 대해 0을 자동으로 부여함
ALTER TABLE companies
ADD COLUMN employee_count INT NOT NULL;

ALTER TABLE companies
ADD COLUMN income INT NOT NULL DEFAULT 1;

-- Delete Column
ALTER TABLE companies
DROP COLUMN phone;

-- Rename Table
RENAME TABLE companies TO suppliers;
ALTER TABLE suppliers RENAME TO companies;

-- Rename Column
ALTER TABLE companies
RENAME COLUMN name TO company_name;

-- Update Column
ALTER TABLE companies
MODIFY company_name VARCHAR(100) DEFAULT '???';

-- Rename & Update Column
ALTER TABLE companies
CHANGE company_name name VARCHAR(255) DEFAULT '???' NOT NULL;

-- Update Constraint
ALTER TABLE houses
ADD CONSTRAINT positive_buy_price CHECK (buy_price >= 0);

-- Error (constraint 안 지켜짐)
INSERT INTO houses(buy_price, sell_price) VALUES (-1, -2);

ALTER TABLE houses DROP CONSTRAINT positive_buy_price;