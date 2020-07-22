--
-- Create model Movie
--
CREATE TABLE `cinema_movie` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `title` varchar(200) NOT NULL, `year` integer NULL);
--
-- Create model User
--
CREATE TABLE `cinema_user` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `username` varchar(100) NOT NULL, `password` varchar(50) NOT NULL, `register_at` date NOT NULL);
--
-- Create model MovieRating
--
CREATE TABLE `cinema_movierating` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `rating` double precision NOT NULL, `factor` double precision NOT NULL, `movie_id` integer NOT NULL, `user_id` integer NOT NULL);
ALTER TABLE `cinema_movierating` ADD CONSTRAINT `cinema_movierating_movie_id_1acf1dc8_fk_cinema_movie_id` FOREIGN KEY (`movie_id`) REFERENCES `cinema_movie` (`id`);
ALTER TABLE `cinema_movierating` ADD CONSTRAINT `cinema_movierating_user_id_faf17282_fk_cinema_user_id` FOREIGN KEY (`user_id`) REFERENCES `cinema_user` (`id`);
