USE mysql;
CREATE DATABASE IF NOT EXISTS KishoCinema;
CREATE USER IF NOT EXISTS 'kisho'@'localhost' IDENTIFIED BY 'KishoKurokawa';
GRANT ALL ON KishoCinema.* to 'kisho'@'localhost';
FLUSH PRIVILEGES;