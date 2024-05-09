## Notes:

# CS 2316 - Spring 2024 - HW04 Numpy
# HW04: This homework is due by February 25th @ 11:59PM.

# You are required to complete the missing bodies of the functions below.
# Further instructions are provided in the comments ...
# A few tips:
#   - Make sure you return the right value and datatype
#   - Test your code for each function by uncommenting the respective test cases
#     in the if __name__ == '__main__' block
#   - Do not import modules within functions
#   - Do not leave any print statements within your functions
#   - Submit in Gradescope as HW04.py  - Your submission should be named exactly HW04.py

import numpy as np

def heisting(percentage_profit, total_profit):
		# totalamt=np.sum(total_profit)
	# adjs=totalamt-50
	# addist=(percentage_profit*adjs)/100
	# return addist
	return ((np.sum(total_profit)-50)*percentage_profit)/100
	"""
	QUESTION 1
	- A heist has taken place in several banks
	- The amount in millions stolen at each bank is given in the array total_profit
	- The total amount should be distributed amongst all the participants with the values 
	  representing the percentage of the profit they should recieve
	- Oopise, they forgot to lock the truck holding the money and lost 50 million dollars
	  so now everyone gets a little bit less :(
	- return an array of the amount in millions that each indiviual will now recieve
	- THIS MUST BE DONE IN ONE LINE

	Args:
		total_profit (np.array)
		percentage_profit (np.array)
	Returns:
		np.array

	>>  total_profit = np.array([68, 51, 27, 39, 40, 59, 68, 99])
		percentage_profit = np.array([55, 15, 5, 20, 5])

	>> print(heisting(percentage_profit, total_profit))
	[220.55  60.15  20.05  80.2   20.05]

	"""
	


def cayman_islands(num_banks):
	return np.linspace(1,100,num_banks)
	"""
	QUESTION 2
	- You have a lot of money and you want to put it all in various banks in the Cayman Islands.
	- You want the banks to think you have a lot of money, so you will spread out your money across various,
	  evenly spaced banks.
	- The serial numbers of the banks start from 1 and go up to 100 (inclusive).
	- Given the number of banks you want to can afford to put money in, return a 1D numpy array of the 
	  serial numbers for the banks.
	- THIS MUST BE DONE IN ONE LINE

	Args:
		num_banks (int)
	Returns:
		np.array

	>> serial_numbers(10)
	array([1. 12. 23. 34. 45. 56. 67. 78. 89. 100.])

	>> serial_numbers(12)
	array([1. 10. 19. 28. 37. 46. 55. 64. 73. 82. 91. 100.])

	"""
	

def second_heist(Total_profit, percentage_profit):

	## so what do i need to do: 
	# i need to take the existing percentage prodict and redistribute the percentages properly 
	# 
	return round(Total_profit*(percentage_profit/(100-percentage_profit[0]))[1],2)
	'''
	QUESTION 3
	- The last heist is almost complete, but the individual who was suppose to get greatest proportion 
	  of the profit just got caught
	- Now you all do not need to share the total profit with them (Re-distribute this according to everyone else's 
	  current percentages to account for this)
	- Calcuate the amount the second highest earner will make from the NEW GROUP 
	  (the new group contains everyone besides the person who got caught)
	- Round your answer to 2 decimal places

	Args:
		Total_profit(int)
		percantage_profit(np.array)

	Return:
		float64

	>>> Total_profit= 112
		percentage_profit = np.array([55, 15, 7, 20, 3])

	>>> second_heist(Total_profit, percentage_profit)
	37.33
	'''
	

def jewel_thief(jewel_amounts, num_jewels):
	'''
	QUESTION 4
	- You want to steal jewels from different exhibits in a museum. You have a target value
	  you want to steal from each exhibit listed in a 1D array called jewel_amounts.
	- You know you will be stealing a specific number of jewels from each exhibit, num_jewels, 
	  which is also a 1D array.
	- The resale price of each jewels is 20% less than the original amount that the jewels are worth.
	- Calculate the average amount you will get from reselling the jewels from each exhibit
	- Return an array of how much you can earn per jewel from each exhibit rounded to one decimal point
	- THIS MUST BE DONE IN ONE LINE

	Args:
		jewel_amounts (np.array)
		num_jewels (np.array)
	Returns:
		np.array

	>>  jewel_amounts = np.array([4349, 5088, 3423, 7027, 8239, 3206, 4592, 39405, 4935, 7849])
		num_jewels = np.array([8, 17, 9, 1, 4, 3, 25, 17, 9, 32])

	>> print(jewel_thief(jewel_amounts, num_jewels))
	[434.9, 239.4, 304.3, 5621.6, 1647.8, 854.9, 146.9, 1854.4, 438.7, 196.2]

	'''
	return np.round((jewel_amounts/num_jewels) * 0.8,1)
	


def need_bars(vaults, value, metal):
	'''
	Question 5
	You and your team are setting up for a bank vault heist! We want to help them calculate their total 
	takeaway, here's what to keep in mind:

	We want to return the sum of all the vaults that you can have.
	- Since Gold is heavily guarded, everything besides Silver isn't worth stealing
	- You can take open vaults and crack open locked vaults, not sealed ones
	- We can only calculate the sum of the values (10 values) we KNOW, you have more 
		vaults and metal information than you need.
	- THIS MUST BE DONE IN ONE LINE

	>>> vaults = np.array(["Open", "Locked", "Sealed", "Locked", "Locked", "Sealed", "Locked", "Sealed", "Open", "Sealed", "Locked", "Sealed"])
	value = np.array([200, 500, 750, 400, 900, 200, 350, 700, 240, 400])
	metal = np.array(["Iron", "Silver", "Gold", "Silver", "Bronze", "Silver", "Silver", "Silver", "Bronze", "Gold", "Iron", "Silver"])
	print(need_bars(vaults, value, metal))
	>>> 1250

	>>> vaults = np.array(["Sealed", "Open", "Open", "Locked", "Locked", "Open", "Locked", "Sealed", "Open", "Locked", "Sealed", "Sealed"])
	value = np.array([150, 600, 250, 500, 650, 200, 300, 750, 300, 500])
	metal = np.array(["Silver", "Gold", "Iron", "Silver", "Bronze", "Iron", "Silver", "Bronze", "Silver", "Gold", "Iron", "Gold"])
	print(need_bars(vaults, value, metal))
	>>> 1100
	'''
	return np.sum(value[(vaults[0:10] != "Sealed") & (metal[0:10] == "Silver")])
def accProfit(heists1, heists2, heists3, starting, stopping):
	## what do i need to, i need to first combine the heists together first 
	total_array=np.concatenate((heists1,heists2,heists3))
	# print(total_array)
	# print(" i got here")
	# print(total_array)
	valuesneeded=total_array[3:7]
	# print(valuesneeded)
	finalarray=np.linspace(total_array[0],total_array[-1],len(total_array))
	finalarrayvaluesneeded=finalarray[3:7]
	total_array[3:7]=finalarrayvaluesneeded
	return (total_array[3:7])

	# totaldays=stopping-starting+1
	# finaltable=np.linspace(startingindex,stoppingindex,totaldays)
	# total_array[starting:stopping]=finaltable[1:-1]
	# print(total_array)
	# # print(finaltable)


	'''
	QUESTION 6
	- after each heist your group adds the new accumulate profit into a heist array
	- you all split the heists into 3 main sections heists1, heists2, heists3
	- Danny unforunately cannot count correctly so all of his accumulated profit values are wrong
	- luckily you know the days Danny counted and that the accumlated profit keeps a linearly increasing trend 
	- return a new array of ints with a more accurate possible accumulated profit.

	hint: use concatenate and linspace
	*** also you know the first and last values are correct, so use these 
		when trying to find the other values that follow the linear trend ***

	Args:
		heists1(np.array)
		heists2(np.array)
		heists3(np.array)
		starting(int)
		stopping(int)

	Return:
		np.array

	>>> heists1 = np.array([100, 151, 208])
	>>> heists2 = np.array([100, 102, 101])
	>>> heists3 = np.array([100, 448, 500])
	>>> starting = 3
	>>> stopping = 6

	>> accProfit(heists1, heists2, heists3, starting, stopping)
	[250 300 350 400]
	'''
	

def monthly_exhibit(value):
	# return np.where()
	return np.where(value[:,1].astype(float) / value[:,2].astype(float) > 5.5, 'Too Risky', np.where(value[:,1].astype(float) / value[:,2].astype(float) >= 4, 'Worth It', 'Not Worth It'))
	"""
	QUESTION 7
	- You're trying to determine which of a museum's monthly special exhibits are worth the risk of prison. 
	  The museum has exhibits valuing anywhere between $500 and $1000 million.
	- You need to determine the average price of each piece in the monthly exhibit, making each exhibit 
	  too risky, worth stealing from, or not worth stealing from.
	- Value is a numpy array containing the last day of the month (when the exhibits are being removed), 
	  total value of the exhibition in question, and total number of pieces in each exhibit.
	- Too Risky: average cost of each piece in the monthly exhibit > 5.5
	- Worth It: 5.5 >= average cost of each piece in the monthly exhibit >= 4
	- Not Worth It: average cost of each piece in the monthly exhibit < 4
	- Return a numpy array with "Too Risky", "Worth It" and "Not Worth It" for the average cost of each piece in the 
	  monthly exhibit
	- THIS MUST BE DONE IN ONE LINE
	HINT: use np.where() and convert the type of each column to float

	Args:
		value (np.array)
	Returns:
		np.array

	>> value = np.array([['01-31-2022', 672.01, 174],
		['02-28-2022', 504.37, 87],
		['03-31-2022', 900.77, 230],
		['04-30-2022', 843.81, 123],
		['05-31-2022', 575.72, 95],
		['06-30-2022', 781.43, 235],
		['07-31-2022', 702.21, 104],
		['08-31-2022', 624.57, 128],
		['09-30-2022', 888.02, 111],
		['10-31-2022', 998.67, 394],
		['11-30-2022', 956.27, 234],
		['12-31-2022', 523.18, 99]], dtype = object)

	>> monthly_exhibit(value)
		['Not Worth It' 'Too Risky' 'Not Worth It' 'Too Risky' 'Too Risky' 'Not Worth It' 'Too Risky'
		'Worth It' 'Too Risky' 'Not Worth It' 'Worth It' 'Worth It']

	"""
	

def get_replaced(art):

	## np.random 
	# print("igothere")
	## i need to generate random numbers for the amoount of nan values 

	
	"""
	Question 8

	You just stole paintings from an unnamed art gallery with random glass pyramids no one has ever heard for.
	You have left the gallery with a couple of blank saces on the wall and you want to replace them.
	Every piece has a 6 digit number with each number 0-9, so we make sure you recatalogue some random art IDs
	in the place of the blank pieces

	>>> art = np.array([165123, 564580, np.nan, 438470, np.nan, 743451, 263701, 403512, np.nan, 407124])
	>>> [165123. 564580. 214177. 438470. 214177. 743451. 263701. 403512. 214177.
	407124.]

	"""
	
	#DO NOT REMOVE#
	np.random.seed(1)
	##############
	art[np.isnan(art)]=np.random.randint(000000, 999999)
	return art 

if __name__ == "__main__":
	# Question 1
	#total_profit = np.array([68, 51, 27, 39, 40, 59, 68, 99])
	#percentage_profit = np.array([55, 15, 5, 20, 5])
	#print(heisting(percentage_profit, total_profit))
	print('---')

	## Question 2
	# print(cayman_islands(10))
	# print(cayman_islands(12))
	# print('---')

	# Question 3
	# Total_profit= 112
	# percentage_profit = np.array([55, 15, 7, 20, 3])
	# print(second_heist(Total_profit, percentage_profit))
	# print('---')

	## Question 4
	# jewel_amounts = np.array([4349, 5088, 3423, 7027, 8239, 3206, 4592, 39405, 4935, 7849])
	# num_jewels = np.array([8, 17, 9, 1, 4, 3, 25, 17, 9, 32])
	# print(jewel_thief(jewel_amounts, num_jewels))
	
	#jewel_amounts = np.array([934, 73, 940, 305, 206, 1948, 840, 384, 24, 3839, 2375, 293, 320, 295])
	#num_jewels = np.array([3, 2, 4, 18, 8, 2, 1, 45, 1, 88, 23, 45, 71, 25])
	#print(jewel_thief(jewel_amounts, num_jewels))
	print('---')

	# Question 5
	# vaults = np.array(["Open", "Locked", "Sealed", "Locked", "Locked", "Sealed", "Locked", "Sealed", "Open", "Sealed", "Locked", "Sealed"])
	# value = np.array([200, 500, 750, 400, 900, 200, 350, 700, 240, 400])
	# metal = np.array(["Iron", "Silver", "Gold", "Silver", "Bronze", "Silver", "Silver", "Silver", "Bronze", "Gold", "Iron", "Silver"])
	# print(need_bars(vaults, value, metal))

	#vaults = np.array(["Sealed", "Open", "Open", "Locked", "Locked", "Open", "Locked", "Sealed", "Open", "Locked", "Sealed", "Sealed"])
	#value = np.array([150, 600, 250, 500, 650, 200, 300, 750, 300, 500])
	#metal = np.array(["Silver", "Gold", "Iron", "Silver", "Bronze", "Iron", "Silver", "Bronze", "Silver", "Gold", "Iron", "Gold"])
	#print(need_bars(vaults, value, metal))
	print('---')

	# Question 6
	# heists1 = np.array([100, 151, 208])
	# heists2 = np.array([100, 102, 101])
	# heists3 = np.array([100, 448, 500])
	# starting = 3
	# stopping = 6
	# print(accProfit(heists1, heists2, heists3, starting, stopping))

	#heists1 = np.array([200, 221, 242])
	#heists2 = np.array([201, 202, 201])
	#heists3 = np.array([200, 339, 360])
	#starting = 3
	#stopping = 6
	#print(accProfit(heists1, heists2, heists3, starting, stopping))
	print('---')

	## Question 7
	value = np.array([['01-31-2022', 672.01, 174],
		['02-28-2022', 504.37, 87],
		['03-31-2022', 900.77, 230],
		['04-30-2022', 843.81, 123],
		['05-31-2022', 575.72, 95],
		['06-30-2022', 781.43, 235],
		['07-31-2022', 702.21, 104],
		['08-31-2022', 624.57, 128],
		['09-30-2022', 888.02, 111],
		['10-31-2022', 998.67, 394],
		['11-30-2022', 956.27, 234],
		['12-31-2022', 523.18, 99]], dtype = object)
	print(monthly_exhibit(value))    
	print('---')

	# Question 8
	# art = np.array([165123, 564580, np.nan, 438470, np.nan, 743451, 263701, 403512, np.nan, 407124])
	# print(get_replaced(art))

	#pass