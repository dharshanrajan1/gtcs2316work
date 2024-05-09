import pymysql
import getpass
from pprint import pprint
import csv
# No other imports allowed

'''
First, run the provided middle_earth.sql file to create the middle_earth database.
Download "middle_earth.csv".

For the following functions,
  - use the cursor, to execute SQL statements
  - call connection.commit() to save changes you make to the database
  - to examine the different table sin the database, make use of the sql script provided!

Reference the pymysql handout for more details on using pymysql
This assignment is due on Sunday, April 7th @ 11:59PM
'''

############################################################################
# THIS PART IS WRITTEN FOR YOU
############################################################################
def reset_database(cursor):

    d1 = "DROP TABLE IF EXISTS characters;"
    c1 = "CREATE TABLE characters ( \
                charID      VARCHAR (50) NOT NULL UNIQUE, \
                age         INTEGER (5) NOT NULL, \
                race        VARCHAR (50), \
                PRIMARY KEY (charID) \
            );"

    d2 = "DROP TABLE IF EXISTS location;"
    c2 = "CREATE TABLE location (\
                locID           VARCHAR (50) NOT NULL UNIQUE,\
                place           CHAR (50) NOT NULL UNIQUE,\
                PRIMARY KEY     (locID)\
            );"

    d3 = "DROP TABLE IF EXISTS items;"
    c3 = "CREATE TABLE items ( \
                itemID          VARCHAR (50) NOT NULL UNIQUE, \
                item_name       VARCHAR (50) NOT NULL, \
                creation_year   INTEGER (4)  NOT NULL, \
                charID          VARCHAR(50), \
                PRIMARY KEY     (itemID, item_name), \
                FOREIGN KEY     (charID) REFERENCES characters(charID) \
            );"

    d4 = "DROP TABLE IF EXISTS kingdoms"
    d5 = "DROP TABLE IF EXISTS second_age_summary"


    cursor.execute(d3) # items has to be dropped first because it has foreign keys
    cursor.execute(d2) # then drop location
    cursor.execute(d1) # and drop characters

    cursor.execute(d4) # drop first created table
    cursor.execute(d5) # drop second created table

    cursor.execute(c1) # create the first three tables
    cursor.execute(c2)
    cursor.execute(c3)


############################################################################
# ANSWER THE QUESTIONS BELOW. USE THE CURSOR TO EXECUTE YOUR QUERIES
############################################################################

def question1a(cursor):
    query = "Select * from characters;"
    cursor.execute(query)
    result = cursor.fetchall()
    return result
    '''
    Send a query to the middle_earth database and return all the rows in the characters table.

    # Test Case
    question1a(cursor)

    =========== Characters Table ===========
    (('Aragorn', 87, 'Human'),
     ('Arwen', 2778, 'Elf'),
     ('Bilbo Baggins', 129, 'Hobbit'),
     ('Boromir', 41, 'Human'),
     ('Elrond', 6516, 'Elf'),
     ('Eowyn', 24, 'Human'),
     ('Faramir', 36, 'Human'),
     ('Frodo Baggins', 50, 'Hobbit'),
     ('Galadriel', 7054, 'Elf'),
     ('Gandalf', 2019, 'Maia'),
     ('Gimli', 139, 'Dwarf'),
     ('Gollum', 589, 'Hobbit'),
     ('Legolas', 2931, 'Elf'),
     ('Pippin', 29, 'Hobbit'),
     ('Samwise Gamgee', 38, 'Hobbit'),
     ('Saruman', 3519, 'Maia'),
     ('Sauron', 6000, 'Maia'),
     ('Theoden', 71, 'Human'),
     ('Treebeard', 23912, 'Ent'))
    '''
    

def question1b(cursor):
    query = "Select item_name, age from characters natural join items Where creation_year<1900;"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

    '''
    Send a query to the middle_earth database and return the name of the item and the age of the owner of each item created before 1900.

    # Test Case
    question1b(cursor)

    =========== Filtered Items Table ===========
    (('Sting', 50),
     ('Vilya', 6516),
     ('Glamdring', 2019),
     ('The One Ring', 50),
     ('Nenya', 7054),
     ('Narya', 2019))
    '''
    

def question2a(cursor, name, age, race):
    query = "INSERT INTO characters (charID, age, race) VALUES (%s, %s, %s);" ## %s is placeholder recitation notes 
    cursor.execute(query, (name,age,race))
    # result = cursor.fetchall()
    # return result
    '''
    Insert a new character into the characters table. All values are given as parameters. 

    # Test Case
    question2a(cursor, 'Glorfindel', 7051, 'Elf')

    =========== Updated characters Table ===========
    ('Aragorn', 87, 'Human')
    ('Arwen', 2778, 'Elf')
    ('Bilbo Baggins', 129, 'Hobbit')
    ('Boromir', 41, 'Human')
    ('Elrond', 6516, 'Elf')
    ('Eowyn', 24, 'Human')
    ('Faramir', 36, 'Human')
    ('Frodo Baggins', 50, 'Hobbit')
    ('Galadriel', 7054, 'Elf')
    ('Gandalf', 2019, 'Maia')
    ('Gimli', 139, 'Dwarf')
    ('Glorfindel', 7051, 'Elf')
    ('Gollum', 589, 'Hobbit')
    ('Legolas', 2931, 'Elf')
    ('Pippin', 29, 'Hobbit')
    ('Samwise Gamgee', 38, 'Hobbit')
    ('Saruman', 3519, 'Maia')
    ('Sauron', 6000, 'Maia')
    ('Theoden', 71, 'Human')
    ('Treebeard', 23912, 'Ent')
    '''
    

def question2b(cursor, magic):
    query= "INSERT INTO items (itemID, item_name, creation_year,charID) VALUES (%s,%s ,%s, %s);"
    cursor.executemany(query, (magic))

    '''
    You want to add multiple magical items at one time. The parameter 'magic' is a list of tuples
    that contains values for itemID, item_name, creation_year, and charID. Insert these magical
    items into the items table.

    # Test Case
    magic = [(11, 'Two Lamps', 1900, 'Arwen'), (12, 'Palantir', 1050, 'Sauron'), (13, 'Walking Axe', 1050, 'Gimli')]
    question2b(cursor, magic)

    =========== Updated items Table ===========
    ('1', 'Sting', 510, 'Frodo Baggins')
    ('10', 'Vilya', 1590, 'Elrond')
    ('11', 'Two Lamps', 1900, 'Arwen')
    ('12', 'Palantir', 1050, 'Sauron')
    ('13', 'Walking Axe', 1050, 'Gimli')
    ('2', 'Glamdring', 510, 'Gandalf')
    ('3', 'Anduril', 3018, 'Aragorn')
    ('4', 'Mithril Coat', 2000, 'Frodo Baggins')
    ('5', 'Herugrim', 2480, 'Theoden')
    ('6', 'Horn of Gondor', 1998, 'Boromir')
    ('7', 'The One Ring', 1600, 'Frodo Baggins')
    ('8', 'Nenya', 1590, 'Galadriel')
    ('9', 'Narya', 1590, 'Gandalf')
    '''
    

def question3a(cursor):
    # Create TABLE kingdoms (
    # kingdom varchar(20) UNIQUE NOT NULL,
    # race ENUM('Man', 'Elf', 'Dwarf'),
    # first_capital varchar(20) NOT Null, 
    # second_capital varchar(20),
    # era_founded ENUM('First Age', 'Second Age', 'Third Age', 'Fourth Age', 'Year of the Trees'),
    # PRIMARY KEY (kingdom)
    # );
    query= "Create TABLE kingdoms (kingdom varchar(20) UNIQUE NOT NULL,race ENUM('Man', 'Elf', 'Dwarf'),first_capital varchar(20) NOT Null, second_capital varchar(20),era_founded ENUM('First Age', 'Second Age', 'Third Age', 'Fourth Age', 'Year of the Trees'),PRIMARY KEY (kingdom));"
    cursor.execute(query)
#     Create table second_age_summary (
# race ENUM('Man','Elf', 'Dwarf'),
# num_of_kingdoms int, 
# num_of_secondary_capitals int ,
# PRIMARY KEY (race)

# );
    secondtablequery="Create table second_age_summary (race ENUM('Man','Elf', 'Dwarf'),num_of_kingdoms int, num_of_secondary_capitals int ,PRIMARY KEY (race));"
    cursor.execute(secondtablequery)
    '''
    Create a two new tables in middle_earth database called kingdoms and second_age_summary.

    The table kingdoms will have five attributes:
    - kingdom               which is a unique, non-null string with maximum 20 characters. (Primary key of the table)
    - race                  which is a string from the set {'Man', 'Elf', 'Dwarf'}
    - first_capital         which is a non-null string with a maximum of 20 characters
    - second_capital        which is a string with a maximum of 20 characters
    - era_founded           which is a string from the set {'First Age', 'Second Age', 'Third Age', 'Fourth Age', 'Year of the Trees'}

    The table second_age_summary will have three attributes:
    - race                          which is a unique, non-null string from the set {'Man', 'Elf', 'Dwarf'}. (Primary key of the table)
    - num_of_kingdoms               which is an int
    - num_of_secondary_capitals     which is an int

    Make sure that you initialize the attributes with the right SQL datatypes.
    Hint: You should use ENUM for the race and era_founded attribute. Also, be careful with the quotations ...

    '''
    

def question3b(cursor, infile):
    with open('kingdoms.csv', 'r') as fin: 
        reader=csv.reader(fin)
        readerlist=[line for line in reader]

        for i in readerlist[1:]: ##header
            # print(i)
            query= "INSERT into kingdoms(kingdom,race,first_capital,second_capital,era_founded) VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(query,i)
    query2= "UPDATE kingdoms SET second_capital=NULL WHERE second_capital='';"
    cursor.execute(query2)
    '''

    In this question, you should populate the table kingdoms you created in question 3a by importing data from csv files.
    Use the provided kingdoms.csv files to retrieve relevant data and insert it into the tables using pymysql. Then, update
    all the empty-string values in the second_capital column with NULL values. You should use the csv module!

    # Test Case
    question3b(cursor, 'kingdoms.csv')

    =========== Updated kingdoms Table ===========
    ('Arnor', 'Man', 'Annuminas', 'Fornost Erain', 'Second Age')
    ('Dale', 'Man', 'Dale', None, 'Third Age')
    ('Doriath', 'Elf', 'Menegroth', None, 'Year of the Trees')
    ('Gondolin', 'Elf', 'Gondolin', None, 'First Age')
    ('Gondor', 'Man', 'Osgiliath', 'Minas Tirith', 'Second Age')
    ('Hithlum', 'Elf', 'Barad Eithel', None, 'Year of the Trees')
    ('Lindon', 'Elf', 'Grey Havens', None, 'Second Age')
    ('Lothlorien', 'Elf', 'Caras Galadhon', None, 'Year of the Trees')
    ('Numenor', 'Man', 'Armenelos', None, 'Second Age')
    ('Rohan', 'Man', 'Edoras', None, 'Third Age')
    ('Woodland Realm', 'Elf', 'Amon Lanc', 'Halls of Thranduil', 'Second Age')
    '''
    

def question3c(cursor):
    qeury=" INSERT into second_age_summary (race, num_of_kingdoms, num_of_secondary_capitals) select race, COUNT(*) as num_of_kingdoms, SUM(IF (second_capital is not NULL, 1, 0) ) as num_of_secondary_capitals from kingdoms where era_founded = 'Second Age' GROUP BY race;"
    # query="INSERT into second_age_summary ()"
    cursor.execute(qeury)
    
    '''
    Insert data into the second_age_summary table created in question 3a by writing a query that finds the race, total kingdoms per race, 
    and the number of kingdoms with second capitals for each race and kingdom founded in the Second Age.

    # Test Case
    question3c(cursor)

    =========== Updated second_age_summary Table ===========
    ('Man', 3, 2)
    ('Elf', 2, 1)
    '''
    

def question4a(cursor):
    query="UPDATE kingdoms SET second_capital = first_capital WHERE second_capital IS NULL;"
    cursor.execute(query)
    '''

    Fill-up the null values in second_capital column in the kingdoms table with their respective
    first capitals.

    # Test Case
    question4a(cursor)

    =========== Updated kingdoms Table ===========
    ('Arnor', 'Man', 'Annuminas', 'Fornost Erain', 'Second Age')
    ('Dale', 'Man', 'Dale', 'Dale', 'Third Age')
    ('Doriath', 'Elf', 'Menegroth', 'Menegroth', 'Year of the Trees')
    ('Gondolin', 'Elf', 'Gondolin', 'Gondolin', 'First Age')
    ('Gondor', 'Man', 'Osgiliath', 'Minas Tirith', 'Second Age')
    ('Hithlum', 'Elf', 'Barad Eithel', 'Barad Eithel', 'Year of the Trees')
    ('Lindon', 'Elf', 'Grey Havens', 'Grey Havens', 'Second Age')
    ('Lothlorien', 'Elf', 'Caras Galadhon', 'Caras Galadhon', 'Year of the Trees')
    ('Numenor', 'Man', 'Armenelos', 'Armenelos', 'Second Age')
    ('Rohan', 'Man', 'Edoras', 'Edoras', 'Third Age')
    ('Woodland Realm', 'Elf', 'Amon Lanc', 'Halls of Thranduil', 'Second Age')
    '''
    

def question4b(cursor):

    query= "SELECT Sum(distinct age)  FROM characters Natural join items WHERE race = 'Hobbit';"
    cursor.execute(query)
    quryresult=cursor.fetchall()
    # total_age=quryresult[0] 
    secondquery="UPDATE characters SET age = age + %s WHERE race = 'Hobbit';"
    cursor.executemany(secondquery,(quryresult))
    '''
    Update the characters table by setting the age of all hobbits to be their
    current age plus the sum of unique ages of all the hobbits in the items table.

    # Test Case
    question4b(cursor)

    =========== Updated characters Table ===========
    ('Aragorn', 87, 'Human')
    ('Arwen', 2778, 'Elf')
    ('Bilbo Baggins', 1419, 'Hobbit')
    ('Boromir', 41, 'Human')
    ('Elrond', 6516, 'Elf')
    ('Eowyn', 24, 'Human')
    ('Faramir', 36, 'Human')
    ('Frodo Baggins', 550, 'Hobbit')
    ('Galadriel', 7054, 'Elf')
    ('Gandalf', 2019, 'Maia')
    ('Gimli', 139, 'Dwarf')
    ('Gollum', 6479, 'Hobbit')
    ('Legolas', 2931, 'Elf')
    ('Pippin', 319, 'Hobbit')
    ('Samwise Gamgee', 418, 'Hobbit')
    ('Saruman', 3519, 'Maia')
    ('Sauron', 6000, 'Maia')
    ('Theoden', 71, 'Human')
    ('Treebeard', 23912, 'Ent')
    '''
    

def question5(cursor, name):
    query= "DELETE FROM items WHERE item_name = %s"
    cursor.execute(query,name)
    '''
    Delete an entry from the items table given the item name.

    # Test Case
    question5(cursor, 'Glamdring')

    =========== Updated items Table ===========
    ('1', 'Sting', 510, 'Frodo Baggins')
    ('10', 'Vilya', 1590, 'Elrond')
    ('11', 'Two Lamps', 1900, 'Arwen')
    ('12', 'Palantir', 1050, 'Sauron')
    ('13', 'Walking Axe', 1050, 'Gimli')
    ('3', 'Anduril', 3018, 'Aragorn')
    ('4', 'Mithril Coat', 2000, 'Frodo Baggins')
    ('5', 'Herugrim', 2480, 'Theoden')
    ('6', 'Horn of Gondor', 1998, 'Boromir')
    ('7', 'The One Ring', 1600, 'Frodo Baggins')
    ('8', 'Nenya', 1590, 'Galadriel')
    ('9', 'Narya', 1590, 'Gandalf')
    '''
    

############################################################################
# TESTING PORTION
############################################################################
def populate_database(cursor):
    #Populate the characters relation
    cursor.execute("INSERT INTO characters (charID, age, race) VALUES ('Frodo Baggins', 50, 'Hobbit');")
    cursor.execute("INSERT INTO characters (charID, age, race) VALUES ('Gandalf', 2019, 'Maia');")
    cursor.execute("INSERT INTO characters (charID, age, race) VALUES ('Aragorn', 87, 'Human');")
    cursor.execute("INSERT INTO characters (charID, age, race) VALUES ('Legolas', 2931, 'Elf');")
    cursor.execute("INSERT INTO characters (charID, age, race) VALUES ('Gimli', 139, 'Dwarf');")
    cursor.execute("INSERT INTO characters (charID, age, race) VALUES ('Bilbo Baggins', 129, 'Hobbit');")
    cursor.execute("INSERT INTO characters (charID, age, race) VALUES ('Samwise Gamgee', 38, 'Hobbit');")
    cursor.execute("INSERT INTO characters (charID, age, race) VALUES ('Arwen', 2778, 'Elf');")
    cursor.execute("INSERT INTO characters (charID, age, race) VALUES ('Galadriel', 7054, 'Elf');")
    cursor.execute("INSERT INTO characters (charID, age, race) VALUES ('Elrond', 6516, 'Elf');")
    cursor.execute("INSERT INTO characters (charID, age, race) VALUES ('Sauron', 6000, 'Maia');")
    cursor.execute("INSERT INTO characters (charID, age, race) VALUES ('Saruman', 3519, 'Maia');")
    cursor.execute("INSERT INTO characters (charID, age, race) VALUES ('Faramir', 36, 'Human');")
    cursor.execute("INSERT INTO characters (charID, age, race) VALUES ('Boromir', 41, 'Human');")
    cursor.execute("INSERT INTO characters (charID, age, race) VALUES ('Pippin', 29, 'Hobbit');")
    cursor.execute("INSERT INTO characters (charID, age, race) VALUES ('Eowyn', 24, 'Human');")
    cursor.execute("INSERT INTO characters (charID, age, race) VALUES ('Theoden', 71, 'Human');")
    cursor.execute("INSERT INTO characters (charID, age, race) VALUES ('Gollum', 589, 'Hobbit');")
    cursor.execute("INSERT INTO characters (charID, age, race) VALUES ('Treebeard', 23912, 'Ent');")

    #Populate the location relation
    cursor.execute("INSERT INTO location (locID, place) VALUES (1, 'The Shire');")
    cursor.execute("INSERT INTO location (locID, place) VALUES (2, 'Rivendell');")
    cursor.execute("INSERT INTO location (locID, place) VALUES (3, 'Moria');")
    cursor.execute("INSERT INTO location (locID, place) VALUES (4, 'Lothlórien');")
    cursor.execute("INSERT INTO location (locID, place) VALUES (5, 'Isengard');")
    cursor.execute("INSERT INTO location (locID, place) VALUES (6, 'Minas Tirith');")
    cursor.execute("INSERT INTO location (locID, place) VALUES (7, 'Mordor');")
    cursor.execute('INSERT INTO location (locID, place) VALUES (8, "Helm\'s Deep");')
    cursor.execute("INSERT INTO location (locID, place) VALUES (9, 'The Lonely Mountain');")
    cursor.execute("INSERT INTO location (locID, place) VALUES (10, 'Lake-town');")
    cursor.execute("INSERT INTO location (locID, place) VALUES (11, 'Erebor');")
    cursor.execute("INSERT INTO location (locID, place) VALUES (12, 'Fangorn Forest');")
    cursor.execute("INSERT INTO location (locID, place) VALUES (13, 'Barad-dûr');")
    cursor.execute("INSERT INTO location (locID, place) VALUES (14, 'Gondor');")
    cursor.execute("INSERT INTO location (locID, place) VALUES (15, 'Rohan');")
    cursor.execute("INSERT INTO location (locID, place) VALUES (16, 'The Misty Mountains');")
    cursor.execute("INSERT INTO location (locID, place) VALUES (17, 'The Prancing Pony');")
    cursor.execute("INSERT INTO location (locID, place) VALUES (18, 'The Dead Marshes');")
    cursor.execute("INSERT INTO location (locID, place) VALUES (19, 'Mount Doom');")
    cursor.execute("INSERT INTO location (locID, place) VALUES (20, 'Bag End');")
    cursor.execute("INSERT INTO location (locID, place) VALUES (21, 'Grey Havens');")
    cursor.execute("INSERT INTO location (locID, place) VALUES (22, 'Weathertop');")

    #Populate the items relation
    cursor.execute("INSERT INTO items (itemID, item_name, creation_year, charID) VALUES (1, 'Sting', 0510, 'Frodo Baggins');")
    cursor.execute("INSERT INTO items (itemID, item_name, creation_year, charID) VALUES (2, 'Glamdring', 0510, 'Gandalf');")
    cursor.execute("INSERT INTO items (itemID, item_name, creation_year, charID) VALUES (3, 'Anduril', 3018, 'Aragorn');")
    cursor.execute("INSERT INTO items (itemID, item_name, creation_year, charID) VALUES (4, 'Mithril Coat', 2000, 'Frodo Baggins');")
    cursor.execute("INSERT INTO items (itemID, item_name, creation_year, charID) VALUES (5, 'Herugrim', 2480, 'Theoden');")
    cursor.execute("INSERT INTO items (itemID, item_name, creation_year, charID) VALUES (6, 'Horn of Gondor', 1998, 'Boromir');")
    cursor.execute("INSERT INTO items (itemID, item_name, creation_year, charID) VALUES (7, 'The One Ring', 1600, 'Frodo Baggins');")
    cursor.execute("INSERT INTO items (itemID, item_name, creation_year, charID) VALUES (8, 'Nenya', 1590, 'Galadriel');")
    cursor.execute("INSERT INTO items (itemID, item_name, creation_year, charID) VALUES (9, 'Narya', 1590, 'Gandalf');")
    cursor.execute("INSERT INTO items (itemID, item_name, creation_year, charID) VALUES (10, 'Vilya', 1590, 'Elrond');")


def main():
    user_password = getpass.getpass('\n# Enter your MySQL Server password: ')

    connection = pymysql.connect(host = 'localhost',
                                 user = 'root',
                                 password = user_password,
                                 db = 'middle_earth',
                                 charset = "utf8mb4",
                                 cursorclass = pymysql.cursors.Cursor)

    # Always create the cursor
    cursor = connection.cursor()

    reset_database(cursor)
    populate_database(cursor)


    ############################################################################
    # TEST CASES BELOW.
    ############################################################################
    # WE RECOMMEND YOU RUN EACH OF THEM SEPARATELY
    # WE RECOMMEND YOU RUN EACH OF THEM SEPARATELY
    # WE RECOMMEND YOU RUN EACH OF THEM SEPARATELY
    # WE RECOMMEND YOU RUN EACH OF THEM SEPARATELY
    ############################################################################
    ############################################################################
    # IF YOU DO NOT TEST THEM SEPARATELY YOUR ANSWERS MAY DIFFER

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # QUESTION 1A TEST CASE
    # print('Question 1A')
    # print('=========== Characters Table ===========')
    # pprint(question1a(cursor))

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # # QUESTION 1B TEST CASE
    # print('Question 1B')
    # print('=========== Filtered Items Table ===========')
    # pprint(question1b(cursor))

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # # QUESTION 2A TEST CASE
    # print('Question 2A')
    # question2a(cursor, 'Glorfindel', 7051, 'Elf')
    # print('=========== Updated characters Table ===========')
    # cursor.execute("SELECT * FROM characters;")
    # for row in cursor.fetchall():
    #     print(row)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # # QUESTION 2B TEST CASE
    # print('Question 2B')
    # magic = [(11, 'Two Lamps', 1900, 'Arwen'), (12, 'Palantir', 1050, 'Sauron'), (13, 'Walking Axe', 1050, 'Gimli')]
    # question2b(cursor, magic)
    # print('=========== Updated items Table ===========')
    # cursor.execute("SELECT * FROM items;")
    # for row in cursor.fetchall():
    #     print(row)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # # QUESTION 3A TEST CASE
    question3a(cursor)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # # QUESTION 3B TEST CASE
    ##### Please uncomment 3A when running this question ######
    print('Question 3B')
    question3b(cursor, 'kingdoms.csv')
    print('=========== Updated kingdoms Table ===========')
    cursor.execute("SELECT * FROM kingdoms;")
    for row in cursor.fetchall():
        print(row)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # # Question 3C TEST CASE
    ##### Please uncomment 3A AND 3B when running this question ######
    # question3c(cursor)
    # print('Question 3C')
    # print('=========== Updated second_age_summary Table ===========')
    # cursor.execute("SELECT * FROM second_age_summary;")
    # for row in cursor.fetchall():
    #     print(row)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # # QUESTION 4A TEST CASE
    ##### Please uncomment 3A AND 3B when running this question ######
    # question4a(cursor)
    # print('Question 4A')
    # print('=========== Updated kingdoms Table ===========')
    # cursor.execute("SELECT * FROM kingdoms;")
    # for row in cursor.fetchall():
    #     print(row)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # # QUESTION 4B TEST CASE
    # question4b(cursor)
    # print('Question 4B')
    # print('=========== Updated characters Table ===========')
    # cursor.execute("SELECT * FROM characters")
    # for row in cursor.fetchall():
    #     print(row)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # # QUESTION 5 TEST CASE
    # question5(cursor, 'Glamdring')
    # print('Question 5')
    # print('=========== Updated items Table ===========')
    # cursor.execute("SELECT * FROM items;")
    # for row in cursor.fetchall():
    #     print(row)



    # Always commit the connection when you are done
    connection.commit()


if __name__ == "__main__":
    main()