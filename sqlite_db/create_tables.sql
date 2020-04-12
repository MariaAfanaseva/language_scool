PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS addresses;
CREATE TABLE addresses (id_address INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
country VARCHAR (32), region VARCHAR (32), city VARCHAR (32), street VARCHAR (32),
house_number VARCHAR (32), apartment_number VARCHAR (32), postcode VARCHAR (32));

DROP TABLE IF EXISTS persons;
CREATE TABLE persons (id_person INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
name VARCHAR (32), surname VARCHAR (32), email TEXT, phone INTEGER,
id_address TEXT);

DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (id_teacher INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
id_person INTEGER, languages TEXT, courses_id TEXT, diplomas TEXT, salary REAL,
FOREIGN KEY(id_person) REFERENCES persons(id_person));

DROP TABLE IF EXISTS students;
CREATE TABLE students (id_student INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
id_person INTEGER, language_level TEXT, courses_id TEXT, FOREIGN KEY(id_person) REFERENCES persons(id_person));

DROP TABLE IF EXISTS managers;
CREATE TABLE managers (id_manager INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
id_person INTEGER, school TEXT, salary REAL, FOREIGN KEY(id_person) REFERENCES persons(id_person));

DROP TABLE IF EXISTS courses;
CREATE TABLE courses (id_course INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
language TEXT, level TEXT, price REAL, teachers TEXT, students TEXT,
address TEXT, books TEXT);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;