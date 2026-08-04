CREATE DATABASE IF NOT EXISTS college;

USE college;

DROP TABLE IF EXISTS student;

CREATE TABLE student(
    rollno INT,
    name VARCHAR(30),
    marks INT
);

INSERT INTO student
VALUES
(101,'Pritish',95),
(102,'Shanku',96);

SELECT * FROM student;