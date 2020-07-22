-- use KishoCinema
USE KishoCinema;
-- load movie table
LOAD DATA LOCAL INFILE '../../data/movies.csv' INTO TABLE cinema_movie FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;