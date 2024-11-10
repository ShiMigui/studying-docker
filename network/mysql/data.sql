DROP DATABASE IF EXISTS flaskAPI;
CREATE DATABASE flaskAPI;
USE flaskAPI;

CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

/*
Use "mariadb -u your_user -p < data.sql" to execute this file on mariadb
*/