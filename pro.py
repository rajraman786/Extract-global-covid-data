import requests
import texttable
import csv
from tkinter import *
import tkinter.messagebox
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

def take_data(x):
	
	for i in range(220):
	
		if(data[i][0]==x):
			
			a=data[i][1]
			b=data[i][2]
			c=data[i][3]
			break
	return(a,b,c)

#code for gui starts here

def reset():
    country_name.set("")
    case_da.delete(0,END)
    death_da.delete(0,END)
    continent_da.delete(0,END)

def extract():
    
    if (country_name.get()==""):
        tkinter.messagebox.showerror("Error","country name not enterred\n")
    else:
        ca,de,co=take_data(country_name.get())
        case_da.insert(0,str(ca))
        death_da.insert(0,str(de))
        continent_da.insert(0,str(co))


root = Tk()
root.geometry("600x600")
root.minsize(600,600)
root.maxsize(600, 600)
root.title("Extracting Covid Data")
photo = PhotoImage(file="MASK.png")
Label(root,image=photo).place(x=0,y=0)

Label(root, text="For Extracting Covid Data \n Enter Country Name", font="comicsansms 15 bold", pady=15, bg='yellow').place(x=170,y=30)
Label(root, text="Extract", font="comicsansms 15 bold", pady=15, bg='yellow').place(x=260,y=200)
Label(root, text="Cases", font="comicsansms 15 bold", pady=15, bg='yellow').place(x=50,y=300)
Label(root, text="Death", font="comicsansms 15 bold", pady=15, bg='yellow').place(x=250,y=300)
Label(root, text="Continent", font="comicsansms 15 bold", pady=15, bg='yellow').place(x=450,y=300)


country_name = StringVar()
Entry(root, textvariable=country_name).place(x=230,y=150)
case_da=Entry(root)
case_da.place(x=20,y=400)
death_da=Entry(root)
death_da.place(x=220,y=400)
continent_da=Entry(root)
continent_da.place(x=440,y=400)
#Creates button attached with extract function
extract_da = Button(root,font=('arial',15,'bold'), text = "Extract",pady=15, bg='green', command=extract) 
extract_da.place(x=250,y=200)

#Creates button attached with reset function
reset_da = Button(root,font=('arial',15,'bold'), text = "Reset", bg ='red', command=reset) 
reset_da.place(x=250,y=500)


root.mainloop()

#code for gui ends here

# create texttable object 
table = texttable.Texttable() 
table.add_rows([(None, None, None, None)] + data)  # Add an empty row at the beginning for the headers 
table.set_cols_align(('c', 'c', 'c', 'c'))  # 'l' denotes left, 'c' denotes center, and 'r' denotes right 
table.header((' Country ', ' Number of cases ', ' Deaths ', ' Continent ')) 
  
#print(table.draw())


fields = ['Country','Cases','Death','Continent']
# opening and creating a csv file :
with open('mydata.csv', 'w') as file:
    csv_writer = csv.writer(file)
    # first write the column names
    csv_writer.writerow(fields)
    # now add the left row data..
    csv_writer.writerows(data)
