USE middle_earth;
SELECT * FROM characters; 
SELECT * from characters Natural join items; 
Select item_name, age from characters natural join items Where creation_year<1900;
INSERT INTO characters (charID, age, race) VALUES ('Frodo Baggins', 50, 'Hobbit');
Create TABLE kingdoms (
	kingdom varchar(20) UNIQUE NOT NULL,
    race ENUM('Man', 'Elf', 'Dwarf'),
    first_capital varchar(20) NOT Null, 
    second_capital varchar(20),
    era_founded ENUM('First Age', 'Second Age', 'Third Age', 'Fourth Age', 'Year of the Trees'),
    PRIMARY KEY (kingdom)
    );
CREATE TABLE kingdoms (kingdom VARCHAR(20) UNIQUE NOT NULL, race ENUM('Man', 'Elf', 'Dwarf'), first_capital VARCHAR(20) NOT NULL, second_capital VARCHAR(20), era_founded ENUM('First Age', 'Second Age', 'Third Age', 'Fourth Age', 'Year of the Trees'), PRIMARY KEY (kingdom));

Create table second_age_summary (
race ENUM('Man','Elf', 'Dwarf'),
num_of_kingdoms int, 
num_of_secondary_capitals int ,
PRIMARY KEY (race)

);
INSERT INTO second_age_summary (race, num_of_kingdoms, num_of_secondary_capitals)
SELECT race,
       COUNT(*) AS num_of_kingdoms,
       SUM(CASE WHEN has_secondary_capital = 1 THEN 1 ELSE 0 END) AS num_of_secondary_capitals
FROM (
    SELECT c.race,
           l.locID,
           COUNT(DISTINCT l.place) AS num_of_places,
           MAX(CASE WHEN l.locID != 0 THEN 1 ELSE 0 END) AS has_secondary_capital
    FROM characters c
    JOIN location l ON c.charID = l.locID
    WHERE c.age BETWEEN 1 AND 3441  -- Second Age range
    GROUP BY c.race, l.locID
) AS subquery
GROUP BY race;



Select * from second_age_summary; 

UPDATE characters
SET age = age + (
    SELECT SUM(DISTINCT age)
    FROM items
    NATURAL JOIN characters
);
UPDATE characters
SET age = age + COALESCE(
    (SELECT SUM(DISTINCT age) FROM items WHERE race = 'hobbit'),
    0
)
WHERE race = 'hobbit';

Select * from characters; 
UPDATE characters
SET characters.age = characters.age + (
    SELECT SUM(DISTINCT age)
    FROM items
)
WHERE characters.race = 'Hobbit';

SELECT SUM(age) FROM items WHERE race = 'Hobbit' GROUP BY age;

SELECT Sum(distinct age)  FROM characters Natural join items WHERE race = 'Hobbit';
-- UPDATE characters SET age = age + (SELECT SUM(age) FROM items WHERE race = 'Hobbit' GROUP BY age) WHERE race = 'Hobbit'; 
-- Select * from characters;
-- (SELECT SUM(age), characters.charid FROM items,characters WHERE race = 'Hobbit' GROUP BY age);
-- SELECT SUM(age) FROM items GROUP BY age;

-- Select * from characters WHERE race= 'Hobbit';
-- UPDATE characters 
-- SET
-- age
-- age + (SELECT SUM(age)
-- FROM
-- items
-- WHERE
-- race =
-- 'Hobbit'
-- GROUP BY age)
-- WHERE
-- race =


15:44:49	UPDATE characters SET age = age + (     SELECT SUM(DISTINCT age)     FROM characters     NATURAL JOIN items )	Error Code: 1093. You can't specify target table 'characters' for update in FROM clause	0.0058 sec
