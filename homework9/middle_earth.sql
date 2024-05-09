DROP DATABASE IF EXISTS middle_earth;
CREATE DATABASE IF NOT EXISTS middle_earth;
USE middle_earth;

#d1 important characters in middle earth
DROP TABLE IF EXISTS characters;
#c1
CREATE TABLE characters (
    charID      VARCHAR (50) NOT NULL UNIQUE,
    age         INTEGER (5) NOT NULL,
    race        VARCHAR (50),
    PRIMARY KEY (charID)
);
#populate characters relation
INSERT INTO characters (charID, age, race) VALUES ('Frodo Baggins', 50, 'Hobbit');
INSERT INTO characters (charID, age, race) VALUES ('Gandalf', 2019, 'Maia');
INSERT INTO characters (charID, age, race) VALUES ('Aragorn', 87, 'Human');
INSERT INTO characters (charID, age, race) VALUES ('Legolas', 2931, 'Elf');
INSERT INTO characters (charID, age, race) VALUES ('Gimli', 139, 'Dwarf');
INSERT INTO characters (charID, age, race) VALUES ('Bilbo Baggins', 129, 'Hobbit');
INSERT INTO characters (charID, age, race) VALUES ('Samwise Gamgee', 38, 'Hobbit');
INSERT INTO characters (charID, age, race) VALUES ('Arwen', 2778, 'Elf');
INSERT INTO characters (charID, age, race) VALUES ('Galadriel', 7054, 'Elf');
INSERT INTO characters (charID, age, race) VALUES ('Elrond', 6516, 'Elf');
INSERT INTO characters (charID, age, race) VALUES ('Sauron', 6000, 'Maia');
INSERT INTO characters (charID, age, race) VALUES ('Saruman', 3519, 'Maia');
INSERT INTO characters (charID, age, race) VALUES ('Faramir', 36, 'Human');
INSERT INTO characters (charID, age, race) VALUES ('Boromir', 41, 'Human');
INSERT INTO characters (charID, age, race) VALUES ('Pippin', 29, 'Hobbit');
INSERT INTO characters (charID, age, race) VALUES ('Eowyn', 24, 'Human');
INSERT INTO characters (charID, age, race) VALUES ('Theoden', 71, 'Human');
INSERT INTO characters (charID, age, race) VALUES ('Gollum', 589, 'Hobbit');
INSERT INTO characters (charID, age, race) VALUES ('Treebeard', 23912, 'Ent');
            
#d2 locations in middle earth
DROP TABLE IF EXISTS location;
#c2
CREATE TABLE location (
                locID           VARCHAR (50) NOT NULL UNIQUE,
                place           CHAR (50) NOT NULL UNIQUE,
                PRIMARY KEY     (locID)
            );
#populate location relation
INSERT INTO location (locID, place) VALUES (1, 'The Shire');
INSERT INTO location (locID, place) VALUES (2, 'Rivendell');
INSERT INTO location (locID, place) VALUES (3, 'Moria');
INSERT INTO location (locID, place) VALUES (4, 'Lothlórien');
INSERT INTO location (locID, place) VALUES (5, 'Isengard');
INSERT INTO location (locID, place) VALUES (6, 'Minas Tirith');
INSERT INTO location (locID, place) VALUES (7, 'Mordor');
INSERT INTO location (locID, place) VALUES (8, 'Helm\'s Deep');
INSERT INTO location (locID, place) VALUES (9, 'The Lonely Mountain');
INSERT INTO location (locID, place) VALUES (10, 'Lake-town');
INSERT INTO location (locID, place) VALUES (11, 'Erebor');
INSERT INTO location (locID, place) VALUES (12, 'Fangorn Forest');
INSERT INTO location (locID, place) VALUES (13, 'Barad-dûr');
INSERT INTO location (locID, place) VALUES (14, 'Gondor');
INSERT INTO location (locID, place) VALUES (15, 'Rohan');
INSERT INTO location (locID, place) VALUES (16, 'The Misty Mountains');
INSERT INTO location (locID, place) VALUES (17, 'The Prancing Pony');
INSERT INTO location (locID, place) VALUES (18, 'The Dead Marshes');
INSERT INTO location (locID, place) VALUES (19, 'Mount Doom');
INSERT INTO location (locID, place) VALUES (20, 'Bag End');
INSERT INTO location (locID, place) VALUES (21, 'Grey Havens');
INSERT INTO location (locID, place) VALUES (22, 'Weathertop');


            
#d3 magical items (swords, rings, etc)
DROP TABLE IF EXISTS items;
#c3
CREATE TABLE items (
                itemID       VARCHAR (50) NOT NULL UNIQUE,
                item_name	        VARCHAR (50) NOT NULL,
                creation_year           INTEGER (4)  NOT NULL, #year of creation
                charID           VARCHAR(50), #character associated with
                PRIMARY KEY     (itemID, item_name),
                FOREIGN KEY     (charID) REFERENCES characters(charID)
            );
#populate items relation
INSERT INTO items (itemID, item_name, creation_year, charID) VALUES (1, 'Sting', 0510, 'Frodo Baggins');
INSERT INTO items (itemID, item_name, creation_year, charID) VALUES (2, 'Glamdring', 0510, 'Gandalf');
INSERT INTO items (itemID, item_name, creation_year, charID) VALUES (3, 'Anduril', 3018, 'Aragorn');
INSERT INTO items (itemID, item_name, creation_year, charID) VALUES (4, 'Mithril Coat', 2000, 'Frodo Baggins');
INSERT INTO items (itemID, item_name, creation_year, charID) VALUES (5, 'Herugrim', 2480, 'Theoden');
INSERT INTO items (itemID, item_name, creation_year, charID) VALUES (6, 'Horn of Gondor', 1998, 'Boromir');
INSERT INTO items (itemID, item_name, creation_year, charID) VALUES (7, 'The One Ring', 1600, 'Frodo Baggins');
INSERT INTO items (itemID, item_name, creation_year, charID) VALUES (8, 'Nenya', 1590, 'Galadriel');
INSERT INTO items (itemID, item_name, creation_year, charID) VALUES (9, 'Narya', 1590, 'Gandalf');
INSERT INTO items (itemID, item_name, creation_year, charID) VALUES (10, 'Vilya', 1590, 'Elrond');
