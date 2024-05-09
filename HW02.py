# ## NOTES:
import re



# CS 2316 - Spring 2024 - HW02 
# HW02: This homework is due by February 4th @ 11:59PM through Gradescope
# Dharshan Karthick Thiyagarajan- HW02

# This homework is divided into three sections.
# Questions 1 and 2 MUST BE DONE IN ONE LINE
# Questions 3 and 4 require you to download the "cheese_text.txt" file as they are linked questions. Please comment out Q3 when you run Q4# Questions 5 and 6 require you to download the "cheese.csv" file 

# You are required to complete the missing bodies of the functions below.
# Further instructions are provided in the comments ...
# A few tips:
#   - Make sure you return the right value and datatype
#   - Test your code for each function by uncommenting the respective test cases
#     in the if __name__ == '__main__' block
#   - Do not import modules within functions
#   - Do not leave any print statements within your functions
#   - Submit in Gradescope as HW02.py  - Your submission should be named exactly HW02.py

# cheese_text.txt and cheese.csv must be located in the same folder as HW02.py in order for your
# code to run properly

import json, csv
from pprint import pprint

def brie_enthusiasts(cheese_list):
	#tempcheese=[]
	#f#inallist=[]
	#cheese_list=set(cheese_list)
	#for i in cheese_list:
		#if 'Brie' in i:
			#tempcheese.append(i)
	#tempcheese.sort()
	#f#or i in tempcheese:
		#i=i.split(',')[0]
		#finallist.append(i)
	#return finallist

	return sorted([x for x in set(cheese_list) if 'Brie' in x])

	"""
	Question 1
	You are given a list of cheeses that your friendly TAs like to eat.
	Imagine you are trying to pick the TAs that, like you, are a Brie enthusiast, from the list.
	To do so ...

	- THIS MUST BE DONE IN ONE LINE
	- First, remove the duplicate TAs in the list provided
	- Then, remove the TAs that do not like Brie
	- Finally, sort the list of cheeses by the first name of the TA that likes the cheese
	- Don't forget to return the resulting list of names!

	Args:
		cheese_list (list)
	Returns:
		list

	>>> brie_enthusiasts(["Christine Ling, Brie", "Jacob Schroeder, Butterkase", "Brandone Vo, Cheddar", "Sam Walls, Brie", "Hannah Cass, Mozarella"]))
	['Christine Ling, Brie', 'Sam Walls, Brie']

	>>> brie_enthusiasts(["Athena Malek, Brie", "Athena Malek, Brie", "Anna Zhao, Gouda", "Jeremy Thomas, Brie", "Jacob Schroeder, Brie"]))
	['Athena Malek, Brie', 'Jacob Scroeder, Brie', 'Jeremy Thomas, Brie']
		
	"""
	
		
def cheese_dict(ta_dict):
	return {x: sorted(y,key= lambda z: (z[-1],z[0])) for x,y in ta_dict.items()}
	#return(ta:)
	"""
	Question 2
	- Given a dictionary that maps a cheese to a list of TAs that want to eat the cheese, return a dictionary with
	the value being the list sorted by the last letter in each TA's last name.
	- If two TAs have the same last letter of their last name, sort by the first letter of their first name.
	- THIS MUST BE DONE IN ONE LINE

	Args:
		ta_dict (dict)
	Returns:
		dict

	>>> cheese_dict({"Brie": ["Sam Walls", "Brandone Vo", "Christine Ling", "Jacob Schroeder", "Anna Zhao"], "Gouda": ["Athena Malek", "Jeremy Thomas", "Anna Zhao"]})
	{'Brie': ['Christine Ling', 'Anna Zhao', 'Brandone Vo', 'Jacob Schroeder', 'Sam Walls'], 'Gouda': ['Athena Malek', 'Anna Zhao', 'Jeremy Thomas']}

	>>> cheese_dict({"Butterkase": ["Sam Walls", "Jeremy Thomas", "Hannah Cass"], "Cheddar": ["Anna Zhao", "Brandone Vo", "Athena Malek"]})
	{'Butterkase': ['Hannah Cass', 'Jeremy Thomas', 'Sam Walls'], 'Cheddar': ['Athena Malek', 'Anna Zhao', 'Brandone Vo']}

	"""
	

def convert_txt_to_csv(input_txt_file):
	templist=[]
	templist2=[]
	with open(input_txt_file, "r", encoding="latin1") as f:
		reader=csv.reader(f, delimiter="\t")
		readerList=[line for line in reader ]
	
	
	for alist in readerList:
		if '3' not in alist[5]:
			templist.append([alist[0]] + [alist[2]] + [alist[4]] + [alist[3]] + [alist[5]]+ [alist[6]])
		
	with open("cheese_out.csv", "w", encoding='UTF-8') as outputfile:
		writer=csv.writer(outputfile)
		writer.writerows(templist)
	
	return templist
	'''
	Question 3
   	- cheese_text.txt contains information about different types of cheese and their various characteristics.
   	- Read the cheese_text.txt with FILE I/O.
   	- Encoding might be required
   	- These are TAB separated values
   	- Use a list of lists to create a CSV file with the appropriate data WITHOUT WHITESPACE (remove \t) named "cheese_out.csv".
   	- Exclude the "type" column
   	- Flip the texture and the flavor columns 
   	- Remove rows that contain the number 3 in the aging column
   	- Return the list of lists.
   	- Please use latin1 encoding!

	Args:
		input_file (cheese.txt)
	Returns:
		List of lists

	Output:
	[['Name', 'Origin', 'Texture', 'Flavor', 'Aging', 'Recommended Pairing'],
	 ['Cheddar',
		'England',
		'Smooth',
		'Sharp',
		'6 months to several years',
		'Apple slices and crusty bread'],
	 ['Brie',
		'France',
		'Creamy',
		'Mild',
		'2 weeks to 2 months',
		'Fresh fruits and baguette'],
	 ...
		['Emmental',
		'Switzerland',
		'Nutty',
		'Mild',
		'4 to 14 months',
		'Dark bread and pickles'],
		['Mascarpone', 'Italy', 'Creamy', 'Mild', 'Fresh', 'Espresso and berries']]

	length: 11
	'''
	


def write_to_json(alist):
	tempdict={}
	for i in sorted(alist[::2]):
		if i[3] in tempdict:
			tempdict[i[3]].append(i[0])
		else: 
			tempdict[i[3]]=[i[0]]
	json.dump(tempdict,open("cheese.json", "w"))
	return tempdict


	'''
	Question 4
	- Using the list of lists from question 3, create a dictionary of lists where each key in the dictionary is a flavor type
	- Only use information from EVEN lines. Skip all odd lines.
	- Each value should be a DISTINCT LIST of the coressponding cheeses that the flavor can have sorted alphabetically
	- Write the dictionary to a JSON file with the name of "cheese.json"
	- Return the dictionary of lists

	Args:
		alist (list of lists from Q3)
	Returns:
		dictionary of lists
		
	Output:
	{'Flavor': ['Name'],
	'Mild': ['Monterey Jack', 'Brie', 'Mascarpone'],
	'Nutty': ['Gruyère'],
	'Strong': ['Blue Cheese']}
	'''
	


def csv_cleaner(input_file):
	cleanlist=[]
	with open(input_file) as inputy:
		reader=csv.reader(inputy)
		csvList=[line for line in reader]
	tempheader=csvList[0]
	# print(tempheader)
	actualdata=csvList[1:]
	# for i in actualdata:
	# 	print(i)
	for i in actualdata:
		templist=[]
		for k in i:
			if "." in k or k.isdigit():
				k=round(float(k), 2)
				templist.append(k)
			else: 
				templist.append(k)

		cleanlist.append(templist)	

	#print(tempheader)
	for i in cleanlist:
		if i[7]==0.0:
			i[7]='None'
	for i in range(len(cleanlist)):
		if cleanlist[i][0][0:12] == 'past process':
			cleanlist[i][0]= cleanlist[i][0][13:] + ", past process"
	for i in range(len(cleanlist)):
		cleanlist[i][0]=cleanlist[i][0].replace(",w/di na po4", "").replace(",wo/di na po4", "") 
	cleanlist.sort(key=lambda x:x[3],reverse=True)
	with open("clean_cheese.csv", 'w') as outputy:
		writer=csv.writer(outputy)
		writer.writerows([tempheader]+cleanlist)
	






	return ([tempheader]+cleanlist)
	
	
		
	'''
	Question 5

	You have been given a csv file with more information about cheese! So exciting! You need to make a nested list of the cheeses and their
	corresponding nutritional information (including the header)!
	You need to clean some things about it first though:

	1. Round all numbers to 2 decimals places (even if they were integers before).

	2. Replace all zeros in the Fiber category as None

	3. Some cheeses are labelled past process at the front instead of the end like "past process, gouda".
	Change these cheeses to have the cheese label first like "gouda, past process".
	Make sure that past process is moved to the end REGARDLESS of other qualities that have been listed.

	4. Some cheeses are categorized by sodium phosphate using with NaPo4 ("w/di na po4") and without ("wo/di na po4"), these are 
	hard to read, so take these out of names entirely

	5. At the end, sort your cheeses with the most amount of Mono-Saturated Fats first.

	6. Write your nested list into a new csv file named "clean_cheese"

	>>> pprint(csv_cleaner('cheese.csv'))
	[['type',
		'sat_fat',
		'polysat_fat',
		'monosat_fat',
		'protein',
		'carb',
		'chol',
		'fiber',
		'kcal'],
	 ['gruyere', 18.91, 1.73, 10.04, 29.81, 0.36, 110.0, 'None', 413.0],
	 ['cheddar', 21.09, 0.94, 9.39, 24.9, 1.28, 105.0, 'None', 403.0],
	 ['port de salut', 16.69, 0.73, 9.34, 23.78, 0.57, 123.0, 'None', 352.0],
	 ['colby', 20.22, 0.95, 9.28, 23.76, 2.57, 95.0, 'None', 394.0],
	 ...
	 ['mozzarella,non-fat', 0.0, 0.0, 0.0, 31.7, 3.5, 18.0, 1.8, 149.0]]


	'''
	

def monosat_cheese(input_file):
	"""
	Question 6
	
	Using your "clean_cheese" csv file from the last question, we want to take a closer look into cheese's nutritional contents.
	Create a dictionary that categorizes the cheeses into keys of Zero MonoSat Fat, Below Avg MonoSat Fat, Average MonoSat Fat, 
	and Above Avg MonoSat Fat. 

	A cheese that falls into the Average MonoSat Fat category is + or - 1 away from the overall MonoSat Fat average.

	The values should be an inner dictionary of the count of low fat cheeses vs normal cheese in each of these 4 categories.

	NOTE: Low fat is indicated within the name of the cheese- they are spelled lowfat, low fat, and lofat.
	Make sure to include ALL of these as low fat!

	>>> pprint(monosat_cheese('clean_cheese.csv'))
	{'Above Avg MonoSat Fat': {'normal': 40},
	 'Average MonoSat Fat': {'low fat': 2, 'normal': 7},
	 'Below Avg MonoSat Fat': {'low fat': 10, 'normal': 13},
	 'Zero MonoSat Fat': {'normal': 1}}

	"""
	newdict={}
	with open(input_file) as inputy:
		newreader=csv.DictReader(inputy)
		newcsvList=[line for line in newreader]
	running_avg=0
	templatedict={'Zero MonoSat Fat': {'low fat':0, 'normal': 0},'Below Avg MonoSat Fat': {'low fat': 0, 'normal':0}, 'Average MonoSat Fat': {'low fat':0, 'normal':0}, 'Above Avg MonoSat Fat': {'low fat': 0, 'normal':0}}
	for i in newcsvList:
		running_avg+=float(i['monosat_fat'])
	finalavg=running_avg/len(newcsvList)
	# print(finalavg)
	for i in newcsvList:
		fat=float(i['monosat_fat'])
		actualcheese=i['type']
		if "lowfat" in actualcheese or  "lofat" in actualcheese or "low fat" in actualcheese:
			cheesetype='low fat'
		else:
			cheesetype='normal'
		if fat==0:
			templatedict['Zero MonoSat Fat'][cheesetype]=templatedict['Zero MonoSat Fat'][cheesetype]+1
		elif fat>finalavg+1:
			templatedict['Above Avg MonoSat Fat'][cheesetype]=templatedict['Above Avg MonoSat Fat'][cheesetype]+1
		elif fat<finalavg-1:
			templatedict['Below Avg MonoSat Fat'][cheesetype]=templatedict['Below Avg MonoSat Fat'][cheesetype]+1
		else: 
			templatedict['Average MonoSat Fat'][cheesetype]=templatedict['Average MonoSat Fat'][cheesetype]+1
	finaldict={}
	for i,k in templatedict.items():
		tempinnerdict={}
		for p,j in k.items():
			if j!=0:
				tempinnerdict[p]=j
		finaldict[i]=tempinnerdict

	return finaldict


   # for i in newcsvList:
   #  	print('hi')
   #  	running_avg+=float(i['monosat_fat'])
   #  finalavg=running_avg/len(newcsvList)

	# print(newcsvList)
	# for i in newcsvList:
	# 	print(i)
	# 	print("-------------")


	

# if __name__ == "__main__":
	## Question 1
	##print(brie_enthusiasts(["Christine Ling, Brie", "Jacob Schroeder, Butterkase", "Brandone Vo, Cheddar", "Sam Walls, Brie", "Hannah Cass, Mozarella"]))
	##print(brie_enthusiasts(["Athena Malek, Brie", "Athena Malek, Brie", "Anna Zhao, Gouda", "Jeremy Thomas, Brie", "Jacob Schroeder, Brie"]))

	## Question 2
	#print(cheese_dict({"Brie": ["Sam Walls", "Brandone Vo", "Christine Ling", "Jacob Schroeder", "Anna Zhao"], "Gouda": ["Athena Malek", "Jeremy Thomas", "Anna Zhao"]}))
	#print(cheese_dict({"Butterkase": ["Sam Walls", "Jeremy Thomas", "Hannah Cass"], "Cheddar": ["Anna Zhao", "Brandone Vo", "Athena Malek"]}))
		
	## Question 3
	# pprint(convert_txt_to_csv('cheese_text.txt'))
		 
	## Question 4
	## When running Q4, please comment out Q3!
	# filtered_list = convert_txt_to_csv('cheese_text.txt')
	# pprint(write_to_json(filtered_list))
		
	## Question 5
	# pprint(csv_cleaner('cheese.csv'))
		
	## Question 6
	# pprint(monosat_cheese('clean_cheese.csv'))

	
	