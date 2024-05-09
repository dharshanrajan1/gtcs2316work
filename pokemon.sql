DROP DATABASE IF EXISTS pokemon;
CREATE DATABASE IF NOT EXISTS pokemon;
USE pokemon;

#all gen1 pokemon
DROP TABLE IF EXISTS gen1_pokemon;
CREATE TABLE gen1_pokemon (
    ID INT NOT NULL UNIQUE,
    Name VARCHAR(50) NOT NULL,
    Type1 VARCHAR(20),
    Type2 VARCHAR(20),
    HP INT,
    Attack INT,
    Defense INT,
    SpAttack INT,
    SpDefense INT,
    Speed INT
);

INSERT INTO gen1_pokemon (ID, Name, Type1, Type2, HP, Attack, Defense, SpAttack, SpDefense, Speed)
VALUES
(1, 'Bulbasaur', 'Grass', 'Poison', 45, 49, 49, 65, 65, 45),
(2, 'Ivysaur', 'Grass', 'Poison', 60, 62, 63, 80, 80, 60),
(3, 'Venusaur', 'Grass', 'Poison', 80, 82, 83, 100, 100, 80),
(4, 'Charmander', 'Fire', NULL, 39, 52, 43, 60, 50, 65),
(5, 'Charmeleon', 'Fire', NULL, 58, 64, 58, 80, 65, 80),
(6, 'Charizard', 'Fire', 'Flying', 78, 84, 78, 109, 85, 100),
(7, 'Squirtle', 'Water', NULL, 44, 48, 65, 50, 64, 43),
(8, 'Wartortle', 'Water', NULL, 59, 63, 80, 65, 80, 58),
(9, 'Blastoise', 'Water', NULL, 79, 83, 100, 85, 105, 78),
(10, 'Caterpie', 'Bug', NULL, 45, 30, 35, 20, 20, 45),
(11, 'Metapod', 'Bug', NULL, 50, 20, 55, 25, 25, 30),
(12, 'Butterfree', 'Bug', 'Flying', 60, 45, 50, 90, 80, 70),
(13, 'Weedle', 'Bug', 'Poison', 40, 35, 30, 20, 20, 50),
(14, 'Kakuna', 'Bug', 'Poison', 45, 25, 50, 25, 25, 35),
(15, 'Beedrill', 'Bug', 'Poison', 65, 90, 40, 45, 80, 75),
(16, 'Pidgey', 'Normal', 'Flying', 40, 45, 40, 35, 35, 56),
(17, 'Pidgeotto', 'Normal', 'Flying', 63, 60, 55, 50, 50, 71),
(18, 'Pidgeot', 'Normal', 'Flying', 83, 80, 75, 70, 70, 101),
(19, 'Rattata', 'Normal', NULL, 30, 56, 35, 25, 35, 72),
(20, 'Raticate', 'Normal', NULL, 55, 81, 60, 50, 70, 97),
(21, 'Spearow', 'Normal', 'Flying', 40, 60, 30, 31, 31, 70),
(22, 'Fearow', 'Normal', 'Flying', 65, 90, 65, 61, 61, 100),
(23, 'Ekans', 'Poison', NULL, 35, 60, 44, 40, 54, 55),
(24, 'Arbok', 'Poison', NULL, 60, 85, 69, 65, 79, 80),
(25, 'Pikachu', 'Electric', NULL, 35, 55, 40, 50, 50, 90),
(26, 'Raichu', 'Electric', NULL, 60, 90, 55, 90, 80, 110),
(27, 'Sandshrew', 'Ground', NULL, 50, 75, 85, 20, 30, 40),
(28, 'Sandslash', 'Ground', NULL, 75, 100, 110, 45, 55, 65),
(29, 'Nidoran♀', 'Poison', NULL, 55, 47, 52, 40, 40, 41),
(30, 'Nidorina', 'Poison', NULL, 70, 62, 67, 55, 55, 56),
(31, 'Nidoqueen', 'Poison', 'Ground', 90, 82, 87, 75, 85, 76),
(32, 'Nidoran♂', 'Poison', NULL, 46, 57, 40, 40, 40, 50),
(33, 'Nidorino', 'Poison', NULL, 61, 72, 57, 55, 55, 65),
(34, 'Nidoking', 'Poison', 'Ground', 81, 102, 77, 85, 75, 85),
(35, 'Clefairy', 'Fairy', NULL, 70, 45, 48, 60, 65, 35),
(36, 'Clefable', 'Fairy', NULL, 95, 70, 73, 95, 90, 60),
(37, 'Vulpix', 'Fire', NULL, 38, 41, 40, 50, 65, 65),
(38, 'Ninetales', 'Fire', NULL, 73, 76, 75, 81, 100, 100),
(39, 'Jigglypuff', 'Normal', 'Fairy', 115, 45, 20, 45, 25, 20),
(40, 'Wigglytuff', 'Normal', 'Fairy', 140, 70, 45, 85, 50, 45),
(41, 'Zubat', 'Poison', 'Flying', 40, 45, 35, 30, 40, 55),
(42, 'Golbat', 'Poison', 'Flying', 75, 80, 70, 65, 75, 90),
(43, 'Oddish', 'Grass', 'Poison', 45, 50, 55, 75, 65, 30),
(44, 'Gloom', 'Grass', 'Poison', 60, 65, 70, 85, 75, 40),
(45, 'Vileplume', 'Grass', 'Poison', 75, 80, 85, 110, 90, 50),
(46, 'Paras', 'Bug', 'Grass', 35, 70, 55, 45, 55, 25),
(47, 'Parasect', 'Bug', 'Grass', 60, 95, 80, 60, 80, 30),
(48, 'Venonat', 'Bug', 'Poison', 60, 55, 50, 40, 55, 45),
(49, 'Venomoth', 'Bug', 'Poison', 70, 65, 60, 90, 75, 90),
(50, 'Diglett', 'Ground', NULL, 10, 55, 25, 35, 45, 95),
(51, 'Dugtrio', 'Ground', NULL, 35, 80, 50, 50, 70, 120),
(52, 'Meowth', 'Normal', NULL, 40, 45, 35, 40, 40, 90),
(53, 'Persian', 'Normal', NULL, 65, 70, 60, 65, 65, 115),
(54, 'Psyduck', 'Water', NULL, 50, 52, 48, 65, 50, 55),
(55, 'Golduck', 'Water', NULL, 80, 82, 78, 95, 80, 85),
(56, 'Mankey', 'Fighting', NULL, 40, 80, 35, 35, 45, 70),
(57, 'Primeape', 'Fighting', NULL, 65, 105, 60, 60, 70, 95),
(58, 'Growlithe', 'Fire', NULL, 55, 70, 45, 70, 50, 60),
(59, 'Arcanine', 'Fire', NULL, 90, 110, 80, 100, 80, 95),
(60, 'Poliwag', 'Water', NULL, 40, 50, 40, 40, 40, 90),
(61, 'Poliwhirl', 'Water', NULL, 65, 65, 65, 50, 50, 90),
(62, 'Poliwrath', 'Water', 'Fighting', 90, 95, 95, 70, 90, 70),
(63, 'Abra', 'Psychic', NULL, 25, 20, 15, 105, 55, 90),
(64, 'Kadabra', 'Psychic', NULL, 40, 35, 30, 120, 70, 105),
(65, 'Alakazam', 'Psychic', NULL, 55, 50, 45, 135, 95, 120),
(66, 'Machop', 'Fighting', NULL, 70, 80, 50, 35, 35, 35),
(67, 'Machoke', 'Fighting', NULL, 80, 100, 70, 50, 60, 45),
(68, 'Machamp', 'Fighting', NULL, 90, 130, 80, 65, 85, 55),
(69, 'Bellsprout', 'Grass', 'Poison', 50, 75, 35, 70, 30, 40),
(70, 'Weepinbell', 'Grass', 'Poison', 65, 90, 50, 85, 45, 55),
(71, 'Victreebel', 'Grass', 'Poison', 80, 105, 65, 100, 70, 70),
(72, 'Tentacool', 'Water', 'Poison', 40, 40, 35, 50, 100, 70),
(73, 'Tentacruel', 'Water', 'Poison', 80, 70, 65, 80, 120, 100),
(74, 'Geodude', 'Rock', 'Ground', 40, 80, 100, 30, 30, 20),
(75, 'Graveler', 'Rock', 'Ground', 55, 95, 115, 45, 45, 35),
(76, 'Golem', 'Rock', 'Ground', 80, 120, 130, 55, 65, 45),
(77, 'Ponyta', 'Fire', NULL, 50, 85, 55, 65, 65, 90),
(78, 'Rapidash', 'Fire', NULL, 65, 100, 70, 80, 80, 105),
(79, 'Slowpoke', 'Water', 'Psychic', 90, 65, 65, 40, 40, 15),
(80, 'Slowbro', 'Water', 'Psychic', 95, 75, 110, 100, 80, 30),
(81, 'Magnemite', 'Electric', 'Steel', 25, 35, 70, 95, 55, 45),
(82, 'Magneton', 'Electric', 'Steel', 50, 60, 95, 120, 70, 70),
(83, 'Farfetch\'d', 'Normal', 'Flying', 52, 65, 55, 58, 62, 60),
(84, 'Doduo', 'Normal', 'Flying', 35, 85, 45, 35, 35, 75),
(85, 'Dodrio', 'Normal', 'Flying', 60, 110, 70, 60, 60, 100),
(86, 'Seel', 'Water', NULL, 65, 45, 55, 45, 70, 45),
(87, 'Dewgong', 'Water', 'Ice', 90, 70, 80, 70, 95, 70),
(88, 'Grimer', 'Poison', NULL, 80, 80, 50, 40, 50, 25),
(89, 'Muk', 'Poison', NULL, 105, 105, 75, 65, 100, 50),
(90, 'Shellder', 'Water', NULL, 30, 65, 100, 45, 25, 40),
(91, 'Cloyster', 'Water', 'Ice', 50, 95, 180, 85, 45, 70),
(92, 'Gastly', 'Ghost', 'Poison', 30, 35, 30, 100, 35, 80),
(93, 'Haunter', 'Ghost', 'Poison', 45, 50, 45, 115, 55, 95),
(94, 'Gengar', 'Ghost', 'Poison', 60, 65, 60, 130, 75, 110),
(95, 'Onix', 'Rock', 'Ground', 35, 45, 160, 30, 45, 70),
(96, 'Drowzee', 'Psychic', NULL, 60, 48, 45, 43, 90, 42),
(97, 'Hypno', 'Psychic', NULL, 85, 73, 70, 73, 115, 67),
(98, 'Krabby', 'Water', NULL, 30, 105, 90, 25, 25, 50),
(99, 'Kingler', 'Water', NULL, 55, 130, 115, 50, 50, 75),
(100, 'Voltorb', 'Electric', NULL, 40, 30, 50, 55, 55, 100),
(101, 'Electrode', 'Electric', NULL, 60, 50, 70, 80, 80, 140),
(102, 'Exeggcute', 'Grass', 'Psychic', 60, 40, 80, 60, 45, 40),
(103, 'Exeggutor', 'Grass', 'Psychic', 95, 95, 85, 125, 65, 55),
(104, 'Cubone', 'Ground', NULL, 50, 50, 95, 40, 50, 35),
(105, 'Marowak', 'Ground', NULL, 60, 80, 110, 50, 80, 45),
(106, 'Hitmonlee', 'Fighting', NULL, 50, 120, 53, 35, 110, 87),
(107, 'Hitmonchan', 'Fighting', NULL, 50, 105, 79, 35, 110, 76),
(108, 'Lickitung', 'Normal', NULL, 90, 55, 75, 60, 75, 30),
(109, 'Koffing', 'Poison', NULL, 40, 65, 95, 60, 45, 35),
(110, 'Weezing', 'Poison', NULL, 65, 90, 120, 85, 70, 60),
(111, 'Rhyhorn', 'Ground', 'Rock', 80, 85, 95, 30, 30, 25),
(112, 'Rhydon', 'Ground', 'Rock', 105, 130, 120, 45, 45, 40),
(113, 'Chansey', 'Normal', NULL, 250, 5, 5, 35, 105, 50),
(114, 'Tangela', 'Grass', NULL, 65, 55, 115, 100, 40, 60),
(115, 'Kangaskhan', 'Normal', NULL, 105, 95, 80, 40, 80, 90),
(116, 'Horsea', 'Water', NULL, 30, 40, 70, 70, 25, 60),
(117, 'Seadra', 'Water', NULL, 55, 65, 95, 95, 45, 85),
(118, 'Goldeen', 'Water', NULL, 45, 67, 60, 35, 50, 63),
(119, 'Seaking', 'Water', NULL, 80, 92, 65, 65, 80, 68),
(120, 'Staryu', 'Water', NULL, 30, 45, 55, 70, 55, 85),
(121, 'Starmie', 'Water', 'Psychic', 60, 75, 85, 100, 85, 115),
(122, 'Mr. Mime', 'Psychic', 'Fairy', 40, 45, 65, 100, 120, 90),
(123, 'Scyther', 'Bug', 'Flying', 70, 110, 80, 55, 80, 105),
(124, 'Jynx', 'Ice', 'Psychic', 65, 50, 35, 115, 95, 95),
(125, 'Electabuzz', 'Electric', NULL, 65, 83, 57, 95, 85, 105),
(126, 'Magmar', 'Fire', NULL, 65, 95, 57, 100, 85, 93),
(127, 'Pinsir', 'Bug', NULL, 65, 125, 100, 55, 70, 85),
(128, 'Tauros', 'Normal', NULL, 75, 100, 95, 40, 70, 110),
(129, 'Magikarp', 'Water', NULL, 20, 10, 55, 15, 20, 80),
(130, 'Gyarados', 'Water', 'Flying', 95, 125, 79, 60, 100, 81),
(131, 'Lapras', 'Water', 'Ice', 130, 85, 80, 85, 95, 60),
(132, 'Ditto', 'Normal', NULL, 48, 48, 48, 48, 48, 48),
(133, 'Eevee', 'Normal', NULL, 55, 55, 50, 45, 65, 55),
(134, 'Vaporeon', 'Water', NULL, 130, 65, 60, 110, 95, 65),
(135, 'Jolteon', 'Electric', NULL, 65, 65, 60, 110, 95, 130),
(136, 'Flareon', 'Fire', NULL, 65, 130, 60, 95, 110, 65),
(137, 'Porygon', 'Normal', NULL, 65, 60, 70, 85, 75, 40),
(138, 'Omanyte', 'Rock', 'Water', 35, 40, 100, 90, 55, 35),
(139, 'Omastar', 'Rock', 'Water', 70, 60, 125, 115, 70, 55),
(140, 'Kabuto', 'Rock', 'Water', 30, 80, 90, 55, 45, 55),
(141, 'Kabutops', 'Rock', 'Water', 60, 115, 105, 65, 70, 80),
(142, 'Aerodactyl', 'Rock', 'Flying', 80, 105, 65, 60, 75, 130),
(143, 'Snorlax', 'Normal', NULL, 160, 110, 65, 65, 110, 30),
(144, 'Articuno', 'Ice', 'Flying', 90, 85, 100, 95, 125, 85),
(145, 'Zapdos', 'Electric', 'Flying', 90, 90, 85, 125, 90, 100),
(146, 'Moltres', 'Fire', 'Flying', 90, 100, 90, 125, 85, 90),
(147, 'Dratini', 'Dragon', NULL, 41, 64, 45, 50, 50, 50),
(148, 'Dragonair', 'Dragon', NULL, 61, 84, 65, 70, 70, 70),
(149, 'Dragonite', 'Dragon', 'Flying', 91, 134, 95, 100, 100, 80),
(150, 'Mewtwo', 'Psychic', NULL, 106, 110, 90, 154, 90, 130),
(151, 'Mew', 'Psychic', NULL, 100, 100, 100, 100, 100, 100);

#gen 1 trainers
DROP TABLE IF EXISTS trainers;
CREATE TABLE trainers (
    TrainerID INT NOT NULL UNIQUE,
    Name VARCHAR(100) NOT NULL,
    Age INT,
    Region VARCHAR(50),
    School VARCHAR(100),
    Pokemon VARCHAR(100)
);
INSERT INTO trainers (TrainerID, Name, Age, Region, School, Pokemon) 
VALUES 
    (1, 'Ash Ketchum', 10, 'Kanto', 'Pallet Town School', 'Pikachu'),
    (2, 'Misty Waterflower', 12, 'Kanto', 'Cerulean City School', 'Starmie'),
    (3, 'Brock Slate', 15, 'Kanto', 'Pewter City School', 'Onix'),
    (4, 'May Maple', 12, 'Hoenn', 'Petalburg City School', 'Torchic'),
    (5, 'Dawn Berlitz', 10, 'Sinnoh', 'Twinleaf Town School', 'Piplup'),
    (6, 'Gary Oak', 10, 'Kanto', 'Pallet Town School', 'Eevee'),
    (7, 'Serena Yvonne', 10, 'Kalos', 'Lumiose City School', 'Fennekin'),
    (8, 'Cynthia Shirona', 26, 'Sinnoh', 'Celestic Town School', 'Garchomp'),
    (9, 'Kiawe Hapu', 11, 'Alola', 'Wela Volcano School', 'Marowak'),
    (10, 'Giovanni Sakaki', 40, 'Kanto', 'Viridian City School', 'Persian'),
    (11, 'Lana Nohara', 12, 'Alola', 'Konikoni City School', 'Popplio'),
    (12, 'Erika Ayase', 16, 'Kanto', 'Celadon City School', 'Vileplume'),
    (13, 'Wallace Morimoto', 24, 'Hoenn', 'Sootopolis City School', 'Milotic'),
    (14, 'Clair Iris', 17, 'Johto', 'Blackthorn City School', 'Dragonair'),
    (15, 'Hau Kukui', 12, 'Alola', 'Iki Town School', 'Raichu'),
    (16, 'N', 17, 'Unova', 'Nuvema Town School', 'Zekrom'),
    (17, 'Steven Stone', 29, 'Hoenn', 'Mossdeep City School', 'Metagross'),
    (18, 'Marnie', 18, 'Galar', 'Spikemuth School', 'Morpeko'),
    (19, 'Raihan', 23, 'Galar', 'Hammerlocke School', 'Duraludon'),
    (20, 'Hilbert Touya', 16, 'Unova', 'Nuvema Town School', 'Snivy');

DROP TABLE IF EXISTS historicalevents;
CREATE TABLE historicalevents (
    EventID INT NOT NULL UNIQUE,
    Name VARCHAR(100) NOT NULL,
    Date DATE,
    Description TEXT,
    LocationID INT,
    Attendees INT,
    DurationInHours DECIMAL(5,2)
);
INSERT INTO historicalevents (EventID, Name, Date, Description, LocationID, Attendees, DurationInHours)
VALUES
    (1, 'Indigo League Championship', '1996-12-20', 'Annual tournament to determine the Pokémon Champion of the Indigo Plateau.', 1, 1000, 8),
    (2, 'Team Rocket Takeover', '1998-07-04', 'Team Rocket attempted to take over Silph Co. to steal rare Pokémon.', 2, 20, 2),
    (3, 'Battle of Prism Tower', '2014-10-12', 'A legendary battle between Ash Ketchum and Alain during the Kalos League.', 3, 2, 1.5),
    (4, 'Hoenn Grand Festival', '2004-05-15', 'Annual competition for Pokémon Coordinators held in Hoenn.', 4, 500, 10),
    (5, 'Lugia Rescue Mission', '2000-08-30', 'Trainers united to rescue Lugia and prevent the catastrophic weather.', 5, 30, 4),
    (6, 'Cerulean City Water Festival', '2001-06-25', 'Annual celebration in Cerulean City featuring Water-type Pokémon competitions.', 6, 300, 6),
    (7, 'Sinnoh Grand Festival', '2010-03-18', 'Major competition for Pokémon Coordinators held in Sinnoh.', 7, 700, 12),
    (8, 'Johto League Silver Conference', '2002-09-05', 'Tournament held in Johto to determine the Silver Conference Champion.', 8, 1200, 8),
    (9, 'Battle of the Titans', '2016-11-02', 'Legendary showdown between Red and Blue atop Mt. Silver.', 9, 2, 2),
    (10, 'Unova League', '2013-08-21', 'The pinnacle tournament for trainers in the Unova region.', 10, 800, 10),
    (11, 'Viridian Forest Research Symposium', '1999-04-14', 'Gathering of Pokémon researchers to discuss findings in Viridian Forest.', 11, 50, 4),
    (12, 'Galarian Gym Challenge', '2022-02-28', 'Annual competition where trainers challenge Galarian Gym Leaders.', 12, 500, 8),
    (13, 'Elite Four Induction Ceremony', '2003-12-10', 'Ceremony to induct new members into the Pokémon League Elite Four.', 13, 100, 3),
    (14, 'Alola Region Beauty Pageant', '2017-07-08', 'Event showcasing the beauty and grace of Alolan Pokémon.', 14, 400, 6),
    (15, 'Ancient Ruins Expedition', '2005-11-19', 'Exploration of ancient ruins to uncover Pokémon mysteries.', 15, 10, 5),
    (16, 'Mewtwo Encounter', '1998-02-06', 'Legendary encounter with Mewtwo at the Pokémon Mansion.', 16, 4, 1),
    (17, 'Sunyshore City Light Festival', '2009-12-25', 'Annual festival celebrating the lights of Sunyshore City.', 17, 200, 6),
    (18, 'Island Kahuna Battle Royale', '2016-06-30', 'Gathering of Island Kahuna for a battle royale in Alola.', 18, 8, 2),
    (19, 'Victory Road Challenge', '2007-03-03', 'Trainers attempt to conquer the challenging Victory Road.', 19, 300, 7),
    (20, 'Pokémon Research Symposium', '2014-09-14', 'Global gathering of Pokémon researchers to share discoveries.', 20, 1000, 12),
    (21, 'Battle of the Weather Trio', '2005-08-08', 'Epic clash between Kyogre, Groudon, and Rayquaza to restore balance.', 21, 3, 3),
    (22, 'Cinnabar Island Volcano Expedition', '1997-05-20', 'Scientific expedition to study the volcanic activity on Cinnabar Island.', 22, 15, 5),
    (23, 'Contest Spectacular Finals', '2018-04-02', 'Grand finale of the Pokémon Contest Spectacular held in Hoenn.', 23, 1000, 8),
    (24, 'Eterna City Historical Tour', '2008-10-11', 'Guided tour of the historical landmarks in Eterna City.', 24, 50, 4),
    (25, 'Pokémon World Championships', '2019-08-16', 'Annual competition where the best trainers in the world compete.', 25, 1500, 14),
    (26, 'Battle Frontier Grand Opening', '2006-06-30', 'Opening ceremony for the Battle Frontier facilities in Hoenn.', 26, 200, 6);
    
# table of items
DROP TABLE IF EXISTS items;
CREATE TABLE items (
    ItemID INT NOT NULL UNIQUE,
    Name VARCHAR(100) NOT NULL,
    Cost DECIMAL(10, 2),
    PokemonType VARCHAR(50)
);
INSERT INTO items (ItemID, Name, Cost, PokemonType)
VALUES
    (1, 'Rare Candy', 500, 'All'),
    (2, 'Protein', 100, 'Fighting'),
    (3, 'Iron', 100, 'Steel'),
    (4, 'Calcium', 100, 'Psychic'),
    (5, 'Zinc', 100, 'Bug'),
    (6, 'Carbos', 100, 'Flying'),
    (7, 'HP Up', 200, 'All'),
    (8, 'PP Up', 200, 'All'),
    (9, 'Power Band', 300, 'Fighting'),
    (10, 'Macho Brace', 300, 'All'),
    (11, 'White Herb', 400, 'All'),
    (12, 'X Attack', 200, 'All'),
    (13, 'X Defense', 200, 'All'),
    (14, 'X Sp. Atk', 200, 'All'),
    (15, 'X Sp. Def', 200, 'All'),
    (16, 'Black Belt', 300, 'Fighting'),
    (17, 'Metal Coat', 400, 'Steel'),
    (18, 'Twisted Spoon', 400, 'Psychic'),
    (19, 'Silver Powder', 400, 'Bug'),
    (20, 'Sharp Beak', 400, 'Flying'),
    (21, 'Choice Band', 600, 'Fighting'),
    (22, 'King\'s Rock', 500, 'All'),
    (23, 'Leftovers', 800, 'All'),
    (24, 'Focus Sash', 1000, 'All'),
    (25, 'Amulet Coin', 600, 'All'),
    (26, 'Black Glasses', 400, 'Dark'),
    (27, 'Magnet', 400, 'Electric'),
    (28, 'Soft Sand', 400, 'Ground'),
    (29, 'Miracle Seed', 400, 'Grass'),
    (30, 'Spell Tag', 400, 'Ghost');