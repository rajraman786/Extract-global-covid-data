import requests
import texttable
from bs4 import BeautifulSoup 
url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
# get URL html 
page = requests.get(url) 
soup = BeautifulSoup(page.text, 'html.parser') 
data = [] # list to store data...
# soup.find_all('td') will scrape every element in the url's table 
data_iterator = iter(soup.find_all('td')) 
# data_iterator is the iterator of the table 
# This loop will keep repeating till there is data available in the iterator 
while True: 
	try: 
		country = next(data_iterator).text 
		confirmed = next(data_iterator).text
		deaths = next(data_iterator).text
		continent =next(data_iterator).text
		# For 'confirmed' and 'deaths', make sure to remove the commas and convert to int 
		data.append(( 
			country, confirmed.replace(', ', ''),deaths.replace(', ', ''), 
			continent )) 
	# StopIteration error is raised when there are no more elements left to iterate through 
	except StopIteration: 
		break
# Sort the data by the number of confirmed cases 
data.sort(key = lambda row: row[1], reverse = True) 


# create texttable object 
table = texttable.Texttable() 
table.add_rows([(None, None, None, None)] + data)  # Add an empty row at the beginning for the headers 
table.set_cols_align(('c', 'c', 'c', 'c'))  # 'l' denotes left, 'c' denotes center, and 'r' denotes right 
table.header((' Country ', ' Number of cases ', ' Deaths ', ' Continent ')) 
  
print(table.draw())
import csv
# header for csv file ..
fields = ['Country','Cases','Death','Continent']
# opening and creating a csv file :
with open('mydata.csv', 'w') as file:
    csv_writer = csv.writer(file)
    # first write the column names
    csv_writer.writerow(fields)
    # now add the left row data..
    csv_writer.writerows(data)
