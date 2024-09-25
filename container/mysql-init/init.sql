-- Create the customers table
CREATE TABLE IF NOT EXISTS customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the transactions table
CREATE TABLE IF NOT EXISTS transaction (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    amount DECIMAL(10, 2),
    currency VARCHAR(3),
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description VARCHAR(255),
    FOREIGN KEY (customer_id) REFERENCES customer(id)
);
-- Insert 200 customers
DELIMITER $$

CREATE PROCEDURE GenerateCustomers()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 200 DO
        INSERT INTO customer (name, email, created_at)
        VALUES (CONCAT('Customer ', i), CONCAT('customer', i, '@example.com'), NOW());
        SET i = i + 1;
    END WHILE;
END $$

DELIMITER ;

CALL GenerateCustomers();

-- Insert 100 transactions for each customer with random dates in August 2024
DELIMITER $$

CREATE PROCEDURE GenerateTransactions()
BEGIN
    DECLARE customer_id INT DEFAULT 1;
    DECLARE txn INT;
    DECLARE random_date DATE;
    
    WHILE customer_id <= 200 DO
        SET txn = 1;
        WHILE txn <= 100 DO
            -- Generate a random date in August 2024
            SET random_date = DATE_ADD('2024-08-01', INTERVAL FLOOR(RAND() * 31) DAY);
            
            INSERT INTO transaction (customer_id, amount, currency, transaction_date, description)
            VALUES (
                customer_id, 
                ROUND(RAND() * 1000, 2), 
                'USD', 
                random_date,  -- Use the random date generated
                ELT(FLOOR(1 + RAND() * 5), 
                    'Grocery Shopping', 
                    'Electronics Purchase', 
                    'Restaurant', 
                    'Clothing', 
                    'Fuel Purchase')
            );
            
            SET txn = txn + 1;
        END WHILE;
        SET customer_id = customer_id + 1;
    END WHILE;
END $$

DELIMITER ;

CALL GenerateTransactions();