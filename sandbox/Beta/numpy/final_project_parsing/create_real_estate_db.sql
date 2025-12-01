CREATE DATABASE IF NOT EXISTS real_estate;

USE real_estate;

CREATE TABLE listings (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    title VARCHAR(255),                
    price DECIMAL(10, 2),              
    square VARCHAR(50),               
    floor VARCHAR(50),                
    url TEXT,                          
    city VARCHAR(100),                 
    rooms INT,                         
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

