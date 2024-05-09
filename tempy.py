import csv

with open('kingdoms.csv', 'r') as fin: 
    reader = csv.reader(fin)
    readerlist = [line for line in reader]
    
    for i in readerlist[1:]:
        print(tuple(i))
