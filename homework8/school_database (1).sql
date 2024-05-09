DROP DATABASE IF EXISTS school;
CREATE DATABASE IF NOT EXISTS school;
USE school;

DROP TABLE IF EXISTS students;
CREATE TABLE students (
  studentid 	INT(5) 		NOT NULL UNIQUE,
  fname 		VARCHAR(20) NOT NULL,
  lname         VARCHAR(20) NOT NULL,
  country       VARCHAR(20),
  major         VARCHAR(20),
  gpa           DOUBLE,
  num_classes   INT,
  PRIMARY KEY (studentid)
);

DROP TABLE IF EXISTS classes;
CREATE TABLE classes (
  crn 			INT(5),
  cname			VARCHAR(20) UNIQUE,
  ctype         VARCHAR(6),
  cnumber       INT(4),
  professor     VARCHAR(20),
  PRIMARY KEY (crn)
);

DROP TABLE IF EXISTS enrollment;
CREATE TABLE enrollment (
  studentid 	 INT(5),
  crn            INT(5),
  current_grade  DOUBLE,
  projected      DOUBLE,
  FOREIGN KEY (studentid) REFERENCES students(studentid),
  FOREIGN KEY (crn) REFERENCES classes(crn)
);

-- Populate the students relation
INSERT INTO students(studentid, fname, lname, country, major, gpa, num_classes) VALUES (12345, 'Kate', 'Austen', 'Australia', 'Civil', 3.2, NULL);
INSERT INTO students(studentid, fname, lname, country, major, gpa, num_classes) VALUES (23456, 'Tom', 'Sawyer', 'US', 'Literature', 3.0, NULL);
INSERT INTO students(studentid, fname, lname, country, major, gpa, num_classes) VALUES (34567, 'Charlotte', 'Lewis', 'UK', 'Civil', 2.0, NULL);
INSERT INTO students(studentid, fname, lname, country, major, gpa, num_classes) VALUES (45678, 'Mary', 'Shelley', 'UK', 'Literature', 4.0, NULL);
INSERT INTO students(studentid, fname, lname, country, major, gpa, num_classes) VALUES (56789, 'Benjamin', 'Linus', 'France', 'Aerospace', 3.7, NULL);
INSERT INTO students(studentid, fname, lname, country, major, gpa, num_classes) VALUES (22222, 'Desmond', 'Hume', 'France', 'Aerospace', 3.1, NULL);
INSERT INTO students(studentid, fname, lname, country, major, gpa, num_classes) VALUES (33333, 'Sayid', 'Jarrah', 'Iran', 'Electrical', 3.1, NULL);
INSERT INTO students(studentid, fname, lname, country, major, gpa, num_classes) VALUES (98765, 'Jorge', 'Garcia', 'Mexico', 'Industrial', 2.5, NULL);

-- Populate the classes relation
INSERT INTO classes(crn, cname, ctype, cnumber, professor) VALUES (31415, 'Intro to Physics', 'PHYS', 2211, 'Michael Faraday');
INSERT INTO classes(crn, cname, ctype, cnumber, professor) VALUES (22334, 'English 1', 'ENGL', 1101, 'James Joyce');
INSERT INTO classes(crn, cname, ctype, cnumber, professor) VALUES (11223, 'US History', 'HIST', 1101, 'Thomas Jefferson');
INSERT INTO classes(crn, cname, ctype, cnumber, professor) VALUES (44556, 'Advanced Physics', 'PHYS', 3344, 'Isaac Newton');
INSERT INTO classes(crn, cname, ctype, cnumber, professor) VALUES (55667, 'Calculus 2', 'MATH', 2000, 'Gottfried Leibniz');
INSERT INTO classes(crn, cname, ctype, cnumber, professor) VALUES (66778, 'Intro Psychology', 'PSYCH', 1000, 'Howard Michaels');
INSERT INTO classes(crn, cname, ctype, cnumber, professor) VALUES (98989, 'Computer Science 1', 'CS', 3303, 'Alan Turing');
INSERT INTO classes(crn, cname, ctype, cnumber, professor) VALUES (45454, 'Computer Science 2', 'CS', 3302, 'Denis Peters');

-- Populate the enrolled relation
INSERT INTO enrollment(studentid, crn, current_grade, projected) VALUES (12345, 31415, 88, 90);
INSERT INTO enrollment(studentid, crn, current_grade, projected) VALUES (12345, 22334, 87, 99);
INSERT INTO enrollment(studentid, crn, current_grade, projected) VALUES (23456, 55667, 50, 88);
INSERT INTO enrollment(studentid, crn, current_grade, projected) VALUES (23456, 98989, 70, 75);
INSERT INTO enrollment(studentid, crn, current_grade, projected) VALUES (34567, 22334, 50, 88);
INSERT INTO enrollment(studentid, crn, current_grade, projected) VALUES (45678, 98989, 70, 75);
INSERT INTO enrollment(studentid, crn, current_grade, projected) VALUES (22222, 45454, 50, 55);
INSERT INTO enrollment(studentid, crn, current_grade, projected) VALUES (45678, 45454, 100, 100);
