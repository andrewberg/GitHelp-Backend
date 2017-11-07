create database githelp;
use githelp;

# Table for lesson to produce JSON
CREATE TABLE Lesson (
	id int primary key AUTO_INCREMENT,
	chapter int,
	lesson int,
	title blob,
	body blob
);

# Table for QuizQuestion to produce JSON
create TABLE QuizQuestion (
	id int primary key AUTO_INCREMENT,
	chapter int,
	questionText blob,
	questionID int,
	questionAnswer int
);

# Table for QuizChoices to produce QuizQuestions with answers
create TABLE QuizChoices (
	id int primary key AUTO_INCREMENT,
	text blob,
	questionID int
);