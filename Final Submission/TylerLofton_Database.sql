drop database if exists movies;
create database if not exists movies;
use movies;

CREATE TABLE Movies(
	title VARCHAR(60),
	year YEAR,
	director VARCHAR(30),
	genre VARCHAR(30),
	esrb VARCHAR(10),
	PRIMARY KEY(title, year)
);

CREATE TABLE Studio(
	studioName VARCHAR(30) primary key,
	yearFounded YEAR,
	location VARCHAR(60)
);

CREATE TABLE MovieReleases(
	title VARCHAR(60),
	year YEAR,
	studioName VARCHAR(30),
	releaseDate DATE,
	foreign key (title, year) references Movies(title, year) on delete cascade,
	foreign key (studioName) references Studio(studioName) on delete cascade,
	PRIMARY KEY (title, year, studioName)
);

INSERT INTO Movies VALUES
('Scott Pilgrim vs. the World', 2010, 'Edgar Wright', 'Action/Comedy', 'PG-13'),
('Spirited Away', 2001, 'Hayao Miyazaki', 'Fantasy/Adventure', 'PG'),
('Oppenheimer', 2023, 'Christopher Nolan', 'Thriller/Action', 'R'),
('Barbie', 2023, 'Greta Gerwig', 'Comedy/Fantasy', 'PG-13'),
('Little Man', 2006, 'Keenan Ivory Wayans', 'Comedy/Crime', 'PG-13'),
('Halloween', 1978, 'John Carpenter', 'Horror/Crime', 'R'),
('Halloween', 2007, 'Rob Zombie', 'Horror/Crime', 'R'),
('Halloween', 2018, 'David Gordon Green', 'Horror/Crime', 'R'),
('The Nightmare Before Christmas', 1993, 'Henry Selick', 'Musical/Fantasy', 'PG'),
('Beetle Juice', 1988, 'Tim Burton', 'Comedy/Horror', 'PG');

INSERT INTO Studio(studioName, yearFounded, location) VALUES
('Universal Pictures', 1912, 'Universal City, California'),
('Paramount Pictures', 1912, 'Hollywood, California'),
('Warner Bros.', 1923, 'Burbank, California'),
('Walt Disney Studios', 1923, 'Burbank, California'),
('A24', 2012, 'New York City, New York'),
('Lionsgate', 1997, 'Santa Monica, California'),
('Studio Ghibli', 1985, 'Tokyo, Japan');

INSERT INTO MovieReleases(title, year, studioName, releaseDate) VALUES
('Scott Pilgrim vs. the World', 2010, 'Universal Pictures', '2010-07-27'),
('Spirited Away', 2001, 'Studio Ghibli', '2001-07-20'),
('Oppenheimer', 2023, 'Universal Pictures', '2023-07-11'),
('Halloween', 2018, 'Universal Pictures', '2018-09-08');

select *
from Movies natural join moviereleases
where title = 'Scott Pilgrim vs. the World' and year = 2010;
