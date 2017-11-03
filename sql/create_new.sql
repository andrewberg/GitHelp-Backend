create database githelp;
use githelp;

# Table for lesson to produce JSON
CREATE TABLE Lesson (
	uid int primary key,
	chapter int,
	lesson int,
	title blob,
	body blob
);

# Table for QuizQuestion to produce JSON
create TABLE QuizQuestion (
	uid int primary key,
	chapter int,
	questionText blob,
	questionID int,
	questionAnswer int
);

# Table for QuizChoices to produce QuizQuestions with answers
create TABLE QuizChoices (
	uid int primary key,
	text blob,
	questionID int
);