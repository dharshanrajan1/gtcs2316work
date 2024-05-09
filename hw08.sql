-- hw08 
use pokemon;
Select * from gen1_pokemon;
  -- '''
--     QUERY 8

--     The Pokemon trainers want to buff their Pokemon's secondary type with items in the store. However, since the store has items
--     that can boost only certain types of Pokemon, only some of the trainers will actually benefit from buying items from the store.

--     Create a query that will return the name of the trainer, the primary and secondary types of their pokemon, the name of the Pokemon,
--     the number of unique items the trainer can purchase from the store to buff their Pokemon's secondary type (renamed to "Number of Items",
--     and the total amount they would spend (renamed to "Total Spent", rounded to the nearest integer). Sort the trainers by their age.

--     Expected Output:
--     (('Misty Waterflower', 'Water', 'Psychic', 'Starmie', 2, Decimal('500')),
--     ('Brock Slate', 'Rock', 'Ground', 'Onix', 1, Decimal('400')))
--     '''

SELECT trainers.name, gen1_pokemon.Type1,gen1_pokemon.Type2, gen1_pokemon.name, count(Distinct items.name), sum(items.cost) from gen1_pokemon JOIN trainers ON gen1_pokemon.name = trainers.pokemon JOIN items ON gen1_pokemon.Type2 = items.PokemonType group by trainers.TrainerID, gen1_pokemon.ID;
SELECT trainers.name, gen1_pokemon.Type1,gen1_pokemon.Type2, gen1_pokemon.name,count(Distinct items.name) as 'Number of Items',sum(items.cost) as 'Total Spent' from (gen1_pokemon JOIN trainers ON gen1_pokemon.name = trainers.pokemon) JOIN items ON gen1_pokemon.Type2 = items.PokemonType GROUP by trainers.TrainerID ORDER BY age;




13:06:22	SELECT * from ((gen1_pokemon JOIN trainers ON gen1_pokemon.name = trainers.pokemon) JOIN items ON gen1_pokemon.Type2 = items.PokemonType) group by trainers.TrainerID, gen1_pokemon.ID LIMIT 0, 1000	Error Code: 1055. Expression #17 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'pokemon.items.ItemID' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by	0.0015 sec





















SELECT  pokemon FROM trainers WHERE Region='Sinnoh' UNION SELECT Name FROM gen1_pokemon WHERE Attack > 100 AND SPEED < 60 AND SpDefense > 85;


--  '''
--     QUERY 6

--     Write a query that returns:
--         - The Pokemon Type (renamed to "Type")
--         - The number of Pokemon for each Type (renamed to "Number of Pokemon")
--         - The number of unique items you can purchase that only work on that specific type of Pokemon (renamed to "Number of Items")
--         - The total cost of all the items you would have to buy if you bought one of each item for each of the Pokemon in the type 
--         (renamed to "Amount Spent")
--         - The highest and lowest HP for each type of Pokemon (renamed to "Max Health" and "Min Health" respectively)
--         - Average attack to defense ratio (renamed as "Average Attack to Defense" and rounded to 2 decimal points.)

--     Hint: When calculating the average attack to defense ratio, find the individual ratios first, then average them

--     Expected Output:
--     (('Bug', 12, 2, Decimal('6000.00'), 70, 35, Decimal('1.11')),
--     ('Electric', 9, 1, Decimal('3600.00'), 90, 25, Decimal('1.01')),
--     ('Fighting', 7, 4, Decimal('9100.00'), 90, 40, Decimal('1.75')),
--     ('Ghost', 3, 1, Decimal('1200.00'), 60, 30, Decimal('1.12')),
--     ('Grass', 12, 1, Decimal('4800.00'), 95, 45, Decimal('1.12')),
--     ('Ground', 8, 1, Decimal('3200.00'), 105, 10, Decimal('1.10')),
--     ('Psychic', 8, 2, Decimal('4000.00'), 106, 25, Decimal('1.08')))
--     '''    

-- join gen1 pokemon and items and groupby pokemon
--  SELECT TYPE1,count( items.name) FROM gen1_pokemon LEFT JOIN items group by Type1;
SELECT * from gen1_pokemon;
SELECT TYPE1 as 'Type', count(DISTINCT gen1_pokemon.name) as 'Number of Pokemon', count(DISTINCT items.name) as 'Number of Items' , sum(items.cost) as 'Amount Spent', max(HP) as 'Max Health', min(HP) as 'Min Health', round(avg(Attack/Defense), 2) as 'Average Attack to Defense' FROM gen1_pokemon JOIN items ON gen1_pokemon.Type1=items.PokemonType group by Type1;
-- SELECT Type1 as 'Type', count Distinct(gen1_pokemon.name)  FROM gen1_pokemon JOIN items group by Type1;
-- SELECT Type1 as 'Type', count('name') as 'Number of Pokemon',  ('itemID'), 















































-- SELECT * FROM historicalevents;

-- Select locationID,Name FROM  historicalevents WHERE date<'2004,01-01';

-- SELECT * From gen1_pokemon WHERE name='Nidorina';
-- SELECT name, HP, Attack, Defense FROM gen1_pokemon Where type1='Poison' AND speed>50 AND HP<70;
-- SELECT * from trainers;
-- SELECT name, age, region from trainers ORDER BY age DESC LIMIT 2 OFFSET 1; 
-- SELECT region,count(trainerID) from trainers GROUP BY region HAVING count(trainerID)>=3;
-- -- 15:10:40	SELECT region,count(trainerID)  from trainers GROUP BY region HAVING count(trainerID)>=3 LIMIT 0, 1000	Error Code: 1055. Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'pokemon.trainers.Name' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by	0.0010 sec
-- SELECT 
--     Type2 AS "Secondary Type",
--     COUNT(*) AS "Number of Strong Pokemon",
--     ROUND(AVG(HP), 2) AS "Average HP"
-- FROM 
--     gen1_pokemon
-- WHERE 
--     HP >= 50 
--     AND Type2 IN (SELECT DISTINCT Type1 FROM gen1_pokemon)
-- GROUP BY 
--     Type2
-- ORDER BY 
--     AVG(HP) ;
--     
-- SELECT p.Name
-- FROM gen1_pokemon AS p
-- JOIN trainers AS t ON p.Name = t.Pokemon
-- WHERE t.Region = 'Sinnoh'
--     OR (p.Attack > 100 AND p.Speed < 60 AND p.SpDefense > 85);


-- -- SELECT Type2 AS 'Secondary Type', COUNT(*) AS 'Number of Strong Pokemon', ROUND(AVG(HP), 2) AS 'Average HP' FROM gen1_pokemon WHERE HP >= 50 AND Type2 IN (SELECT DISTINCT Type1 FROM gen1_pokemon) GROUP BY Type2 ORDER BY AVG(HP);
-- -- SELECT Name
-- -- FROM trainers
-- -- WHERE region = 'Sinnoh'
-- --     OR (Attack > 100 AND Speed < 60 AND SpDefense > 85);

--     
--     -- SELECT DISTINCT <column_names> FROM <table_name>;
-- Select count(Type1) from gen1_pokemon join items;
-- -- not me below 
-- SELECT ISNULL(Type1, '') AS Type, COUNT(*) AS Num_Pokemon
-- FROM gen1_pokemon
-- join items
-- GROUP BY ISNULL(Type1, '')
-- ORDER BY Type;

-- SELECT gen1_pokemon.Name
-- FROM gen1_pokemon
-- JOIN trainers ON gen1_pokemon.Name = trainers.Pokemon
-- WHERE (trainers.Region = 'Sinnoh' 
--        OR gen1_pokemon.Attack > 100 
--        OR gen1_pokemon.Speed < 60 
--        OR gen1_pokemon.SpDefense > 85);
--        
-- SELECT * from gen1_pokemon,trainers;
-- SELECT * from gen1_pokemon,trainers WHERE Region='Sinnoh';
-- SELECT DISTINCT pokemon FROM trainers,gen1_pokemon WHERE Region='Sinnoh';

-- SELECT Name from gen1_pokemon WHERE Attack>100 AND SPEED<60 AND SpDefense>85; -- WHERE 

-- -- SELECT DISTINCT pokemon AS result FROM gen1_pokemon, trainers WHERE Region='Sinnoh' UNION SELECT Name AS result FROM gen1_pokemon WHERE Attack > 100 AND SPEED < 60 AND SpDefense > 85;
-- SELECT DISTINCT pokemon AS result FROM gen1_pokemon, trainers WHERE Region='Sinnoh' UNION SELECT Name AS result FROM gen1_pokemon WHERE Attack > 100 AND SPEED < 60 AND SpDefense > 85 ORDER BY result.;
-- Error Code: 1054. Unknown column 'Attack' in 'order clause'

-- SELECT * FROM gen1_pokemon WHERE Attack > 100 AND SPEED < 60 AND SpDefense > 85;
