create database githelp;
use githelp;

CREATE TABLE Lesson (
	uid int primary key,
	int chapter,
	title blob,
	body blob
);

create TABLE QuizQuestion (
	uid int primary key,
	chapter int,
	questionText blob,
	questionID int auto_increment,
	questionAnswer int
);

create TABLE QuizChoices (
	uid int primary key,
	text blob,
	questionID int
);