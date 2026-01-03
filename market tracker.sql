CREATE DATABASE IF NOT EXISTS market_tracker;
USE market_tracker;

CREATE TABLE stock_prices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ticker VARCHAR(10) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    volume INT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM stock_prices;

