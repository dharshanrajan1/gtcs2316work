import math
## Dharshan Karthick Thiyagarajan- Homework 1 
## NOTES:
# Your file must be named "HW01.py" for it to submit properly.
#Comment out all function calls used to test your code.
#Delete all pass statements.
#Do not submit your file with any syntax errors.

# CS 2316 - Spring 2023 - HW01 Python Fundamentals
# HW01: This homework is due by Sunday, January 21st @ 11:59PM through Gradescope
# HW00: Installation Verification is also due by Sunday, January 21st @ 11:59PM through Canvas

# You are required to complete the missing bodies of the functions below.
# Further instructions are provided in the comments ...
# A few tips:
#   - Make sure you return the right value and datatype
#   - Test your code for each function by uncommenting the respective test cases
#     in the if __name__ == '__main__' block
#   - Do not import modules within functions
#   - Do not leave any print statements within your functions
#   - Submit in Gradescope as HW01.py  - Your submission should be named exactly HW01.py

def welcome_class():
	print('Welcome to CS2316!')
	"""
	Question 0
	Print the exact string, "Welcome to CS2316!"

	NOTE: This must be done in one line

	>>> welcome_class()
	'Welcome to CS2316!'

	"""

	

def snake_text(message):
	return(message.replace('s', '').replace('S', ''))
	"""
	Question 1
	Your pet python just learned how to type! It's just sent you its first message, 
	but its tail must have been stuck on the S key, and now the message is a messss!
	Return the message with all of the S's removed.    

	For an extra challenge, try doing this in one line (Optional).

	Note: Fixed messages will not include the letter S.

	Args:
		message (str)
	Returns:
		str

	>>> snake_text("SSsssIs'sm shusSsngsrSyss.")
	'I'm hungry.'

	>>> snake_text("SCasnS wsse SoSrssdessr Stsaskessouts?")
	'Can we order takeout?'

	"""

	
def more_snakes(snakes):
    snakes_sorting= sorted(snakes, key=lambda s: s.split()[1])
    remove_snakes = [snake for snake in snakes_sorting if snake.split()[0] == "Python"]
    return(remove_snakes)
    """
    Question 2
    You are given a list of snakes to catalogue - each with their scientific genus
    and species separated by a space, and need to sort them alphabetically by
    species. However, some of the snakes on the list aren't part of the right genus.

    - First, sort the list alphabetically by species (second word).
    - Remove any members whose genus (first word) is not "Python".
    - Return the resulting list.

    For an extra challenge, try doing this in one line (Optional).

    Args:
        snakes (list)
    Returns:
        list

    >>> more_snakes(["Python molurus", "Simalia nauta", "Python sebae", "Liasis olivaceus", "Python regius"])
    ["Python molurus", "Python regius", "Python sebae"]
    """


def better_snake(snake1, snake2):
	if len(snake1)>len(snake2):
		return(f"Snake battle! {snake1} defeats {snake2}!")
	else: 
		return(f"Snake battle! {snake2} defeats {snake1}!")
	"""
	Question 3
	Two snakes are in a fight. The snake with the longer name has the longer body,
	giving it advantage. Given the names of two snakes, determine the winner and 
	return a string stating who wins:
	"Snake battle! 'winning snake' defeats 'losing snake'!"

	NOTE: You should use f-string to do this question.
	NOTE: Snake names will not have the same length.

	Args:
		snake1 (str), snake2 (str)
	Returns:
		str

	>>> better_snake("Python", "Rattlesnake")
	"Snake battle! Rattlesnake defeats Python!"

	"""

	

def birthday_snake(snake_list, fav_color):
	templist=[]
	for i in snake_list:
		if(i.split()[0]==fav_color):
			templist.append(i)
	return(templist)

	"""
	Question 4
	Your friend told you she wants a snake for her birthday. However, she has forgetten what
	the name of her favorite species is! Ultimately, she decided she doesn't care what snake 
	she gets, as long as it is her favorite color. When you get to the pet store, you're given 
	a list of snakes with their colors. Return a new list with only snakes in her favorite
	color included. 

	Args:
		snake_list (list), fav_color (str)
	Returns:
		list
	
	birthday_snake(['Green Vipor', 'Patterned Rattlesnake', 'Brown Copperhead', 'Green Rattlesnake', 'Yellow Viper'], 'Green')
	>>> ['Green Vipor', 'Green Rattlesnake']

	"""

	

def scary_snakes(adict):
	empty_set= set()
	for key,num in adict.items():
		if(int(num)>=122):
			empty_set.add(key)
	return(empty_set)
	"""
	Question 5
	You have a collection of snakes and want to scare your little sibling. Your sibling is four 
	feet tall, and you want a snake taller than them. Given a dictionary mapping a snake’s name 
	to its length in centimeters, write a function that returns a set of the names of the snakes 
	that are at least 122 cm long, your sibling’s height. 

	HINT: The numbers in the dictionary are formatted as strings.

	Args:
		adict (dict)
	Returns:
		set

	{"Cobra Kai": "152", "Monty Python": "108", "Slytherin": "95"}))
	>>> {"Cobra Kai"}

	"""

	

def snek_handler(snek_dict, bad_sneks):
	for i in snek_dict:
		if i in bad_sneks:
			snek_dict[i].append('poisonous')
		else:
			snek_dict[i].append('non-poisonous')

	for i in bad_sneks:
		if i not in snek_dict:
			snek_dict[i]= ['poisonous']
	return snek_dict
	"""
	Question 6
	You work as a snake handler at a local shelter. You have to keep records of which snakes are poisonous, 
	and which are harmless. Right now, the records indicate all snakes are harmless...that can't be right!!
	You tell your manager, and he gives you a list of which snakes are actually poisonous. Go in and update 
	the snake dictionary by adding either 'non-poisonous' or 'poisonous' to each snake's information list. 
	Return the updated dictionary of all snakes.

	Note: You CANNOT assume every snake in bad_sneks will also be in the given snek_dict. In this case,
	add the snake to the dictionary mapping it just to poisonous.

	Args:
		snek_dict: a dictionary containing each snake mapped to a list of information
		bad_sneks: a list of snake which are poisonous
	Returns:
		dict

	snek_dict = {"python": ["large", "Many habitats"],
				 "anaconda":["massive", "jungle", "can swim"], 
				 "pit-viper":["heat sensing"],
				 "rattlesnake":["rattles", "dry areas"]}
	bad_sneks = ["pit-viper","rattlesnake","black mamba", "boomslang"]

	snek_handler(snek_dict, bad_sneks)
	>>> {'python': ['large', 'Many habitats', 'non-poisonous'], 
		'anaconda': ['massive', 'jungle', 'can swim', 'non-poisonous'], 
		'pit-viper': ['heat sensing', 'poisonous'], 
		'rattlesnake': ['rattles', 'dry areas', 'poisonous'], 
		'black mamba': ['poisonous'], 
		'boomslang': ['poisonous']}

	"""

	

def snake_math(snake):
	return(int(len(snake)/math.sqrt(len(snake))))
	"""
	Question 7

	For this question you will need to use the imported Math Module.

	The snakes are getting out of hand!!! They are way too large! In order to solve this, you invent a potion
	that will shrink each snake to the square root of the length of its name, but without any decimals (truncate).
	Return the snake's new length.
	
	NOTE: This must be done in one line

	Args:
		snake (string)
	Returns:
		int

	>>> snake_math("anaconda")
	2
	"""
	
	

if __name__ == "__main__":


	# # Q0
	# welcome_class()
	# print('---')

	# # Q1
	#print(snake_text("SSsssIs'sm shusSsngsrSyss."))
	#print(snake_text("SCasnS wsse SoSrssdessr Stsaskessouts?"))
	#print('---')

	# # Q2
	#print(more_snakes(["Python molurus", "Simalia nauta", "Python sebae", "Liasis olivaceus", "Python regius"]))
	#print(more_snakes(["Python curtus", "Python natalenis", "Aspidites ramsayi", "Python anchietae", "Morelia azurea"]))
	#print("---")

	# # Q3
	 #print(better_snake("Python", "Rattlesnake"))
	 #print(better_snake("Black mamba", "Kingsnake"))
	 #print("---")

	# # Q4
	 #print(birthday_snake(['Green Viper', 'Patterned Rattlesnake', 'Brown Copperhead', 'Green Rattlesnake', 'Yellow Viper'], 'Green'))
	 #print(birthday_snake(['Red Diamond Rattlesnake', 'Grey Texas Coral Snake', 'Black Florida Cottonmouth', 'Green Boa'], 'Red'))
	 #print("---")

	# # Q5
	 #print(scary_snakes({"Cobra Kai": "152", "Monty Python": "108", "Slytherin": "95"}))
	 #print(scary_snakes({"Kaa": "122", "Nagini": "450", "Snow": "70"}))
	 #print("---")

	# # # Q6
	 snek_dict = {"python": ["large", "Many habitats"],"anaconda":["massive", "jungle", "can swim"], "pit-viper":["heat sensing"],"rattlesnake":["rattles", "dry areas"]}
	 bad_sneks = ["pit-viper","rattlesnake","black mamba", "boomslang"]
	 print(snek_handler(snek_dict, bad_sneks))
	 print("---")

	# # # Q7
	 #print(snake_math("anaconda"))
	 #print(snake_math("king cobra"))

	