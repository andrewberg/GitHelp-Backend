create database githelp;
use githelp;

create table LessonPage (
    uid int primary key,
    title blob,
    body blob,
    nextPage int,
    foreign key (nextPage) references LessonPage(uid)
);

create table Chapter (
    uid int primary key,
    title blob,
    nextChapter int,
    foreign key (nextChapter) references Chapter(uid),
    firstPage int,
    foreign key (firstPage) references LessonPage(uid),

    quiz int #foreign key (quiz) references Quiz(uid)
);

create table QuizQuestion (
    uid int primary key,
    text blob,
    nextQuestion int,
    foreign key (nextQuestion) references QuizQuestion(uid),
    answer int #foreign key (answer) references QuizChoice(uid)

);

create table Quiz (
    uid int primary key,
    chapter int not null,
    firstQuestion int,
    foreign key (firstQuestion) references QuizQuestion(uid),
    foreign key (chapter) references Chapter(uid)
);

create table QuizChoice (
    uid int primary key,
    question int,
    foreign key (question) references QuizQuestion(uid),
    text blob
);

alter table Chapter
    add foreign key (quiz) references Quiz(uid);

alter table QuizQuestion
    add foreign key (answer) references QuizChoice(uid);
