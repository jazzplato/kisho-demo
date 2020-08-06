-- use KishoCinema
USE KishoCinema;
-- load movie table
LOAD DATA LOCAL INFILE '../data/movies.csv' 
INTO TABLE cinema_movie 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS;
-- load user table
LOAD DATA LOCAL INFILE '../data/users.csv' 
INTO TABLE auth_user 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(id, username, password, date_joined, is_active, is_staff, is_superuser);