PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

INSERT INTO addresses (country, region, city, street, house_number,
 apartment_number, postcode)
VALUES ('Russia', 'Moscow region', 'Selenograd', 18, 12, 45, 456278);

INSERT INTO persons (name, surname, email, phone, id_address)
VALUES ('Ivan', 'Ivanov', 'ivanov@gmail.ru', 8916457485, 1);

INSERT INTO teachers (id_person, languages, courses_id, diplomas, salary)
VALUES (1, 'English', '1, 2', 'London diploma', 50000.56);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;