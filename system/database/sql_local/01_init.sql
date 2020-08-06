USE mysql;
SET NAMES UTF8;
CREATE DATABASE IF NOT EXISTS KishoCinema CHARACTER SET utf8 COLLATE utf8_bin;
CREATE USER IF NOT EXISTS 'kisho'@'localhost' IDENTIFIED BY 'KishoKurokawa';
GRANT ALL ON KishoCinema.* to 'kisho'@'localhost';
FLUSH PRIVILEGES;