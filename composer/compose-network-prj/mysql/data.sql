CREATE DATABASE IF NOT EXISTS flaskAPI;
USE flaskAPI;

CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);
