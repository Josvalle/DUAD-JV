CREATE TABLE products (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	code CHAR(8) NOT NULL,
	name VARCHAR(25) NOT NULL,
	price INT DEFAULT 0,
	available_stock INT DEFAULT 0 
);

CREATE TABLE users (
	id INTEGER PRIMARY KEY AUTOINCREMENT
	first_name VARCHAR(25) NOT NULL,
	last_name VARCHAR(25) NOT NULL,
	user_email CHAR(40) NOT NULL,
	user_address VARCHAR(150) NOT NULL
);

CREATE TABLE invoices (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	invoice_number CHAR(10) NOT NULL,
	user_id INT REFERENCES users(id),
	product_id INT REFERENCES products(id),
	total_amount INT DEFAULT 0,
	status CHAR(10) NOT NULL
);


BEGIN TRANSACTION;


IF EXISTS (
  SELECT 1
  FROM products
  WHERE code = '40304015'
    AND available_stock < 0
) THEN
  RETURN; 
END IF;

IF EXISTS (
  SELECT 1
  FROM users
  WHERE id = '1'
) THEN
  RETURN; 
END IF;

SAVEPOINT information_check

INSERT INTO invoices ( invoice_number, user_id, product_id, total_amount, status)
VALUES ('order0005', 1 , 5, 500, 'Pay')

UPDATE products
SET available_stock = available_stock - 1
WHERE code = '40304015'

COMMIT



BEGIN TRANSACTION;


IF EXISTS (
  SELECT 1
  FROM invoices
  WHERE invoice_number = 'order0005'
) THEN
  RETURN; 
END IF;

UPDATE products
SET available_stock = available_stock + 1
WHERE code = '40304015'


UPDATE invoices
SET status = 'Return'
WHERE invoice_number = 'order0005'

COMMIT
