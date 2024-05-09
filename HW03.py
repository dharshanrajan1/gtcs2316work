

import requests
import re , json
from pprint import pprint
from bs4 import BeautifulSoup

## NOTES:

# CS 2316 - Spring 2023 - HW03 Regex, APIs, BeautifulSoup
# HW03: This homework is due by Sunday, February 18th @ 11:59PM through Gradescope

# You are required to complete the missing bodies of the functions below.
# Further instructions are provided in the comments ...
# A few tips:
#   - Make sure you return the right value and datatype
#   - Test your code for each function by uncommenting the respective test cases
#     in the if __name__ == '__main__' block
#   - Do not import modules within functions
#   - Use print only where instructed. Do not leave any extra print statements in place
#   - Submit in Gradescope as HW03.py  - Your submission should be named exactly HW03.py
#   - Print your variables as you code in order to see what values they have,
#     especially for questions with API and BeautifulSoup

def tsunami_dates(tsunami_report):
	return sorted(re.findall(r"\d{2}/\d{2}/\d{4}",tsunami_report))
	"""
	Question 1 - Regex

	Given a report of recent tsunamis and information about them in terrible formatting, 
	return a list of dates that have recently experienced a tsunami sorted by month. 
	Dates are in mm/dd/yyyy format. 
	
	NOTE: This must be done in one line.

	Args:
		tsunami_report (str)
	Returns:
		list

	>>> tsunami_dates("Tsunami on 07/19/2016 in South Georgia Island Region, Tsunami on 09/01/2016 in 
		Gisborne NZ, Tsunami on 11/21/2016 in Honshu Japan, Tsunami on 12/08/2016 in Solomon Islands")
	['07/19/2016', '09/01/2016', '11/21/2016', '12/08/2016']

	"""

	

def call_log(numbers_called):
	# print re.sub((re.findall("-\d{3}-\d{4}", numbers_called))
	return re.sub("\d{3}-\d{4}", "xxx-xxxx", numbers_called)
	"""
	Question 2 - Regex

	You have a report of all the phone numbers that called the emergency service during a 
	landslide. You want the area codes,	but want to censor the rest of the phone number for 
	public release. Replace the last seven digits of each phone number with 'xxx-xxxx'. 
	All phone numbers will be of the format ###-###-####.

	NOTE: This must be done in one line.
	NOTE: Refer to the RegEx handout to see useful RegEx methods.

	Args:
		numbers_called (str)
	Returns:
		str

	>>> call_log("423-290-0098, 865-409-1021, 479-935-1339, 822-913-1670, 804-507-8919")
	"423-xxx-xxxx, 865-xxx-xxxx, 479-xxx-xxxx, 822-xxx-xxxx, 804-xxx-xxxx"

	"""

	
	
def tornado_warning(warning_message):
	# for sentence in warning_message:
	# 		print(sentence)

	## .sub()==re.sub(r‘regEx ’, new_string, a_string)
	## I need to get a regex to match the punctuation and sub in just one of each of the duplicate punctuation. 
	return "".join(re.sub(r'([^\w\s])\1+', r'\1', warning_message))


	"""
	Question 3 - Regex

	You are part of GTENS and need to alert the campus that we are under a tornado warning! 
	However, you're scared of tornadoes and got a little carried away with the punctuation. 
	Go back through the message and make sure there is only one punctuation mark at the end 
	of the sentence.
	
	NOTE: This must be done in one line.
	NOTE: Refer to the RegEx handout to see useful RegEx methods.

	HINT: .findall() and .join() may be helpful.

	Args:
		warning_message (str)
	Returns:
		str

	>>> tornado_warning("OH NO!!!! Georgia Tech can you hear me?? There's a tornado coming... Stay inside!!!")
	"OH NO! Georgia Tech can you hear me? There's a tornado coming. Stay inside!"
	
	"""

	

def wildfire_alert(alert_text):
	##return re.sub("[]", "", re.sub("WF", '', alert_text)) bracket match not working, doesn't include brackets 
	## used list comprhension to and .strip() to remove preceding space, i also had to add an if because otherwise it added an extra entry. 
	return [alert_text.strip() for alert_text in re.split(r'\[WF\]\s*', alert_text) if alert_text.strip()]
	"""
	Question 4 - Regex
	You have to proof the wildfire alert being sent out to the entire city. However, there are tags around each phrase from when 
	the alert was written. Return a list of all of the phrases in the alert to send out in a more readable format. 

	NOTE: This must be done in one line.

	Args:
		alert_text (str)
	Returns:
		list

	>>> wildfire_alert("[WF] Wildfire Update [WF] [WF] Details [WF] [WF] More details [WF]")
	['Wildfire Update', 'Details', 'More Details']

	"""
	

def provide_relief(page):
	r=requests.get("https://api.reliefweb.int/v1/" + page)
	data=r.json()
	templist=[]
	# pprint(data)
	for i, j in data.items():
		templist.append(i)
	return templist 
	"""
	Question 5 - API

	Base API URL: "https://api.reliefweb.int/v1/"

	You know how to use an API, but your friend doesn't, and given the wake of a 
	tsunami, you need to make a list of all	the keys which you can access from a 
	given page of the API. The page will use the base URL above with the page name
	appended to the end of the url string. 

	For example, the "book" page will have a URL of "https://api.reliefweb.int/v1/book"

	Args:
		page (str)
	Returns:
		list
 
	>>> provide_relief("countries")
	['time', 'href', 'links', 'took', 'totalCount', 'count', 'data']

	"""


def find_disasters(num):
	r=requests.get('https://api.reliefweb.int/v1/countries')
	data=r.json()
	# pprint(data)
	## updates data 
	while num>0: 
		data=requests.get(data['links']['next']['href']).json()
		num-=1
		# pprint(data)
	innerdict={}
	# pprint(data)
	for adict in data['data']: 
		tempstatus=requests.get(adict['href']).json()['data'][0]['fields']['status']
		name=adict['fields']['name']
		innerdict[name]=tempstatus
	# pprint(tempstatus)
	# print(adict)
	
	return innerdict





	"""
	Question 6 - API

	URL: 'https://api.reliefweb.int/v1/countries'

	Using the same API from Question 5, now you have a more difficult problem. 
	You want to know the status of natural disasters among different countries 
	and decide to make a dictionary mapping each country to its status. 

	However, for the sake of sending fewer requests, you only care about 10 
	countries at a time. An integer passed into the function will indicate 
	which set of 10 countries you want to gather information for. 
 
	An integer of 0 represents the first 10 countries (0-10). An integer of 1 
	represents the next 10 countries (11-20), and so on. You only want to return 
	the countries associated with the number provided. Accessing the original API 
	data will provide you with the first 10 countries. To get the next 10, you must 
	iterate through the "links" key and find the data associated with the next set 
	of 10 countries. Keep doing this for however many iterations needed. 
 
	NOTE: You will need to use given href links throughout your code to navigate the API.

	HINT: A while loop may be helpful.
 
	Args:
		num (int)
	Returns:
		dict
 
	>>> find_disasters(0)
	{'Bonaire, Saint Eustatius and Saba (The Netherlands)': 'normal', 
	'Saint Martin (France)': 'normal', 
	'Wallis and Futuna (France)': 'normal'
	...
	'Pitcairn Islands': 'normal'}

	The approach that I will take is: 
		r.requests.get("----")
	Then i need to set it equal to a json file, you have to do this every time 
	you work through an api 
	 while loop is better (print out as you are going)
	 has another url at the end for the next set of 10 countries 
	"""	

	

def plagues(website):
	r=requests.get(website)
	soup=BeautifulSoup(r.text,"html.parser")
	table= soup.find("table", {"class": "wikitable"})
	rows=table.find_all("tr")[1:]
	emptylist=[]

	for i in rows:
		data=i.find_all("td")
		tupleval1=(data[1].text.strip())
		tupleval2=(data[6].text.strip().replace('–', '−').split('−')[0])
		finaltuple=(tupleval1,tupleval2)
		emptylist.append(finaltuple)
	return sorted(emptylist, key=lambda x:int(x[1]))

	"""
	Question 7 - Webscraping

	You will be webscraping the wikipedia page for historical epidemics and pandemics. 
	You will be retrieving the data from the table under the "Epidemics and pandemics 
	with at least 1 million deaths" header.

        https://en.wikipedia.org/wiki/List_of_epidemics_and_pandemics

    You will create a list of tuples. Each tuple will contain the name of the 
    epidemic/pandemic and the starting year of the outbreak. The list will be
    sorted by the starting year from earliest to latest.

    Cleaning:
        - For the name make sure to remove any newline or other characters
        - The dash separating the start and end years in the table are "–" 
          and "−"; regular dashes will not work.

	Args:
		website	(str)
	Returns:
		list

	>>> plagues("https://en.wikipedia.org/wiki/List_of_epidemics_and_pandemics")
	[('Antonine Plague', '165'),
 	('Plague of Justinian', '541'),
 	('735–737 Japanese smallpox epidemic', '735'),
 	('Black Death', '1346'),
 	('1520 Mexico smallpox epidemic', '1519'),
	
				...

 	('1957–1958 influenza pandemic', '1957'),
 	('Hong Kong flu', '1968'),
 	('HIV/AIDS epidemic', '1981'),
 	('COVID-19 pandemic', '2019')]

	"""

	

def volcanoes(website):
	r=requests.get(website)
	soup=BeautifulSoup(r.text,"html.parser")
	table= soup.find_all("table", {"class": "wikitable"})[1]
	rows=table.find_all("tr")[1:]
	emptydict={}
	counter=0
	for i in rows: 
		data=i.find_all("td")
		tempvar= data[0].text.strip()
		if "[" not in tempvar:
			if tempvar not in emptydict:
				emptydict[tempvar]=1
			else:
				emptydict[tempvar]+=1
	return emptydict



			
		

	"""
	Question 8 - Webscraping

	You will be webscraping the wikipedia page for volcanic eruptions during the
	Holocene era. You will be retrieving the data from the table under the "Before 
	Common Era (BCE)" header.

        https://en.wikipedia.org/wiki/List_of_large_Holocene_volcanic_eruptions

    You will create a dictionary. The keys will be the names of the volcanoes,
    and the values will be the number of eruptions from each volcano within the
    table.

    Cleaning:
        - For volcano names, exclude any volcanoes that have any footnote tags
          such as "[34]".

	Args:
		website (str)
	Returns:
		dict

	>>> volcanoes("https://en.wikipedia.org/wiki/List_of_large_Holocene_volcanic_eruptions")
	{'Apoyeque': 1,
 	'Avachinsky': 4,
 	'Cerro Blanco (Argentina)': 1,
 	'Etna': 1,

 				...

 	'Tavui': 1,
 	'Towada': 3,
 	'Youngest Caldera, Santorini': 1,
 	'Água de Pau': 2}
	
	"""		

	

if __name__ == "__main__":

	# # Q1
	# pprint(tsunami_dates("Tsunami on 08/29/2018 in Loyalty Islands, Tsunami on 05/15/2018 in Northeast Coast US, Tsunami on 01/23/2018 in Off Kodiak Island AK, Tsunami on 07/17/2017 in Western Aleutian Islands"))
	# pprint(tsunami_dates("Tsunami on 07/19/2016 in South Georgia Island Region, Tsunami on 09/01/2016 in Gisborne NZ, Tsunami on 11/21/2016 in Honshu Japan, Tsunami on 12/08/2016 in Solomon Islands"))
	# print("---")

	# Q2
	# pprint(call_log("423-290-0098, 865-409-1021, 479-935-1339, 822-913-1670, 804-507-8919"))
	# pprint(call_log("678-626-5490, 302-357-3636, 607-598-9218, 209-963-9320, 760-238-0440"))
	# print("---")

	# # Q3
	# pprint(tornado_warning("OH NO!!!! Georgia Tech can you hear me?? There's a tornado coming... Stay inside!!!"))
	# # pprint(tornado_warning("EVERYONE STAY INSIDE!!!! There is a tornado outside???? Keep safe..."))
	# print("---")

	# # Q4
	# pprint(wildfire_alert("[WF] Wildfire Update [WF] [WF] Details [WF] [WF] More details [WF]"))
	# print("---")

	# # Q5
	# pprint(provide_relief("countries"))
	# pprint(provide_relief(""))
	# print("---")

	# Q6
	# pprint(find_disasters(0))
	# pprint(find_disasters(5))
	# print("---")

	# # Q7
	# pprint(plagues("https://en.wikipedia.org/wiki/List_of_epidemics_and_pandemics"))
	# print("---")

	# # Q8
	pprint(volcanoes("https://en.wikipedia.org/wiki/List_of_large_Holocene_volcanic_eruptions"))
	print("---")

	pass