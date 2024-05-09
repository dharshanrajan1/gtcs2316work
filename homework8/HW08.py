import pymysql
from pprint import pprint
import getpass

## NOTES:

# CS 2316 - Spring 2024 - HW08 OOP and Comprehensions
# HW07: This homework is due by Wednesday, March 31st @ 11:59PM.

# You are required to complete the missing bodies of the functions below.
# Further instructions are provided in the comments ...
# A few tips:
#   - Make sure you return the right value and datatype if a return is required
#   - Test your code for each function by uncommenting the respective test cases
#     in the if __name__ == '__main__' block
#   - Do not import modules within functions
#   - Do not leave any print statements within your functions
#   - Submit in Gradescope as HW08.py - Your submission should be named exactly HW08.py
#   - Print your variables as you code in order to see what values they have
#   - Make sure the table names are lowercase in your query

def create_cursor(host_name, user_name, pw, db_name):
    try:
        connection = pymysql.connect(host = host_name, user = user_name, password = pw, db = db_name, \
                                    charset = "utf8mb4", cursorclass = pymysql.cursors.Cursor)
        cursor = connection.cursor()
        return cursor
    except Exception as e:
        print(e)
        print(f"Couldn't log in to MySQL server using this password: {pw}.\n")

def ancient_history(cursor):
    '''
    QUERY 1

    You are curious about historical events, especially ones that happened before your very generic birthday
    of January 1st, 2004.

    Create a query that will return the event ID and name of the events that occurred before 2004, January 1st.

    Expected Output:
    ((1, 'Indigo League Championship'),
    (2, 'Team Rocket Takeover'),
    (5, 'Lugia Rescue Mission'),
    (6, 'Cerulean City Water Festival'),
    (8, 'Johto League Silver Conference'),
    (11, 'Viridian Forest Research Symposium'),
    (13, 'Elite Four Induction Ceremony'),
    (16, 'Mewtwo Encounter'),
    (22, 'Cinnabar Island Volcano Expedition'))
    '''

    query = "Select locationID,Name FROM  historicalevents WHERE date<'2004,01-01';"

    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def p_is_for_poison_and_purple(cursor):
    '''
    QUERY 2

    You are looking to collect more poison type Pokemon because you like the color purple. Since there are A LOT of
    poison type Pokemon, however, you are only looking for Pokemon that satisy certain criteria.

    Create a query that will return the name, hp, attack, and defense for Pokemon that have poison as their primary type, 
    a speed higher than 50, but less than 70 HP.

    Expected Output:
    (('Ekans', 35, 60, 44),
    ('Arbok', 60, 85, 69),
    ('Nidorino', 61, 72, 57),
    ('Zubat', 40, 45, 35),
    ('Weezing', 65, 90, 120))
    '''

    query = "SELECT name, HP, Attack, Defense FROM gen1_pokemon Where type1='Poison' AND speed>50 AND HP<70;"

    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def the_elderly(cursor):
    '''
    QUERY 3

    You want to befriend some of the older trainers so you can learn all of their tips and tricks, but you're bad
    at talking to people that are substantially older than you

    Create a query that will return the name, age, and region of the second and third oldest in descending age order.

    Expected Output:
    (('Steven Stone', 29, 'Hoenn'), 
    ('Cynthia Shirona', 26, 'Sinnoh'))
    '''

    query = "SELECT name, age, region from trainers ORDER BY age DESC LIMIT 2 OFFSET 1;"

    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def populated_places(cursor):
    '''
    QUERY 4

    You are debating where to move as you want to go somewhere with a good amount of Pokemon trainers your age.

    Create a query that will return the region, and the number of trainers in the region for regions with at least
    3 trainers.

    Expected Output:
    (('Kanto', 6), ('Hoenn', 3), ('Alola', 3))
    '''

    query = "SELECT region,count(trainerID) from trainers GROUP BY region HAVING count(trainerID)>=3;"

    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def strong_secondaries(cursor):
    '''
    QUERY 5

    You're looking in the Pokedex for non-monotype Pokemon, so Pokemon that have a secondary type (Type2) 
    that can also be a primary type (Type1). That is, you want pokemon whose secondary type is a subset 
    of all the primary types. Additionally, these pokemon should be strong, so their HP should be at least 50. 
 
    Create a query that will return the correct secondary types (renamed as "Secondary Type"), 
    the number of Pokemon with at least 50 HP (renamed as "Number of Strong Pokemon"), and the average HP, rounded to 2 decimal places, 
    of the Pokemon that meet these requirements (renamed as "Average HP") ordered by the average HP.

    Expected Output:
    (('Grass', 1, Decimal('60.00')),
    ('Water', 2, Decimal('65.00')),
    ('Poison', 12, Decimal('67.08')),
    ('Ground', 4, Decimal('76.50')),
    ('Psychic', 6, Decimal('77.50')),
    ('Fighting', 1, Decimal('90.00')),
    ('Ice', 3, Decimal('90.00')),
    ('Rock', 2, Decimal('92.50')),
    ('Fairy', 2, Decimal('127.50')))
    '''

    query = "SELECT Type2 AS 'Secondary Type', COUNT(*) AS 'Number of Strong Pokemon', ROUND(AVG(HP), 2) AS 'Average HP' FROM gen1_pokemon WHERE HP >= 50 AND Type2 IN (SELECT DISTINCT Type1 FROM gen1_pokemon) GROUP BY Type2 ORDER BY AVG(HP);"


    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def attack_defense(cursor):
    '''
    QUERY 6

    Write a query that returns:
        - The Pokemon Type (renamed to "Type")
        - The number of Pokemon for each Type (renamed to "Number of Pokemon")
        - The number of unique items you can purchase that only work on that specific type of Pokemon (renamed to "Number of Items")
        - The total cost of all the items you would have to buy if you bought one of each item for each of the Pokemon in the type 
        (renamed to "Amount Spent")
        - The highest and lowest HP for each type of Pokemon (renamed to "Max Health" and "Min Health" respectively)
        - Average attack to defense ratio (renamed as "Average Attack to Defense" and rounded to 2 decimal points.)

    Hint: When calculating the average attack to defense ratio, find the individual ratios first, then average them

    Expected Output:
    (('Bug', 12, 2, Decimal('6000.00'), 70, 35, Decimal('1.11')),
    ('Electric', 9, 1, Decimal('3600.00'), 90, 25, Decimal('1.01')),
    ('Fighting', 7, 4, Decimal('9100.00'), 90, 40, Decimal('1.75')),
    ('Ghost', 3, 1, Decimal('1200.00'), 60, 30, Decimal('1.12')),
    ('Grass', 12, 1, Decimal('4800.00'), 95, 45, Decimal('1.12')),
    ('Ground', 8, 1, Decimal('3200.00'), 105, 10, Decimal('1.10')),
    ('Psychic', 8, 2, Decimal('4000.00'), 106, 25, Decimal('1.08')))
    '''    


    query = "SELECT TYPE1 as 'Type', count(DISTINCT gen1_pokemon.name) as 'Number of Pokemon', count(DISTINCT items.name) as 'Number of Items' , sum(items.cost) as 'Amount Spent', max(HP) as 'Max Health', min(HP) as 'Min Health', round(avg(Attack/Defense), 2) as 'Average Attack to Defense' FROM gen1_pokemon JOIN items ON gen1_pokemon.Type1=items.PokemonType group by Type1;"

    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def grain_of_salt(cursor):
    '''
    QUERY 7

    You've decided that you should look at specific Pokemon instead of types of Pokemon. You have some friends in the Sinnoh
    region, so you ask them first. That being said, you're going to take what they say with a grain of salt and also look around
    at other types of Pokemon that fall under the specs you like.

    Write a query that returns the Pokemon belonging to trainers from the Sinnoh region, or Pokemon that have an attack stat 
    above 100, speed under 60, and a Special Defense (SpDefense) stat above 85.

    Expected Output:
    (('Piplup',), ('Garchomp',), ('Muk',), ('Snorlax',))
    '''

    query = "SELECT  pokemon FROM trainers WHERE Region='Sinnoh' UNION SELECT Name FROM gen1_pokemon WHERE Attack > 100 AND SPEED < 60 AND SpDefense > 85;"

    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def secondary_buff(cursor):
    '''
    QUERY 8

    The Pokemon trainers want to buff their Pokemon's secondary type with items in the store. However, since the store has items
    that can boost only certain types of Pokemon, only some of the trainers will actually benefit from buying items from the store.

    Create a query that will return the name of the trainer, the primary and secondary types of their pokemon, the name of the Pokemon,
    the number of unique items the trainer can purchase from the store to buff their Pokemon's secondary type (renamed to "Number of Items",
    and the total amount they would spend (renamed to "Total Spent", rounded to the nearest integer). Sort the trainers by their age.

    Expected Output:
    (('Misty Waterflower', 'Water', 'Psychic', 'Starmie', 2, Decimal('500')),
    ('Brock Slate', 'Rock', 'Ground', 'Onix', 1, Decimal('400')))
    '''

    query = "SELECT trainers.name, gen1_pokemon.Type1,gen1_pokemon.Type2, gen1_pokemon.name, count(Distinct items.name), sum(items.cost) from gen1_pokemon JOIN trainers ON gen1_pokemon.name = trainers.pokemon JOIN items ON gen1_pokemon.Type2 = items.PokemonType group by trainers.TrainerID, gen1_pokemon.ID;"

    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def main():

    ######################## Insert MySQL Server password if applicable ########################

    user_password = getpass.getpass('\n# Enter your MySQL Server password: ')
    cursor = create_cursor('localhost', 'root', user_password, 'pokemon')

    # If you do not want to enter your password every time, you can replace
    # user_password with your password (as a string) and comment out
    # this line of code: user_password = getpass.getpass('\n# Enter your MySQL Server password: ')
    # We recommend resetting this before uploading your HW.

    ########################### Test Cases ###########################

    # # Query 1
    # print(">>> ancient_history(cursor)")
    # pprint(ancient_history(cursor))

    # # Query 2
    print(">>> p_is_for_poison_and_purple(cursor)")
    pprint(p_is_for_poison_and_purple(cursor))

    # # Query 3
    # print(">>> the_elderly(cursor)")
    # pprint(the_elderly(cursor))

    # # Query 4
    # print(">>> populated_places(cursor)")
    # pprint(populated_places(cursor))

    # # Query 5
    # print(">>> strong_secondaries(cursor)")
    # pprint(strong_secondaries(cursor))

    # # Query 6
    # print(">>> attack_defense(cursor)")
    # pprint(attack_defense(cursor))

    # # Query 7
    # print(">>> grain_of_salt(cursor)")
    # pprint(grain_of_salt(cursor))

    # # Query 8
    # print(">>> secondary_buff(cursor)")
    # pprint(secondary_buff(cursor))


if __name__ == '__main__':
    main()
