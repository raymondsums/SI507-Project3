from bs4 import BeautifulSoup
import unittest
import requests
import csv

#########
## Instr note: the outline comments will stay as suggestions, otherwise it's too difficult.
## Of course, it could be structured in an easier/neater way, and if a student decides to commit to that, that is OK.

## NOTE OF ADVICE:
## When you go to make your GitHub milestones, think pretty seriously about all the different parts and their requirements, and what you need to understand. Make sure you've asked your questions about Part 2 as much as you need to before Fall Break!


######### PART 0 #########

# Write your code for Part 0 here.

try:
	with open('gallery.html','r') as f:
		html = f.read()
except:
	response = requests.get('http://newmantaylor.com/gallery.html')
	html = response.text
	f = open('gallery.html','w')
	f.write(html)

kitty_soup = BeautifulSoup(html,'html.parser').find('body')
img_text = (kitty_soup.find_all('img'))
for i in img_text:
	print(i.get('alt',"No alternative text provided!"))

######### PART 1 #########

# Get the main page data...

default_url = 'https://www.nps.gov/'

try:
	with open('nps_gov_data.html','r') as file_nps:
		html_1 = file_nps.read()
except:
	response_1 = requests.get('https://www.nps.gov/index.htm')
	html_1 = response_1.text
	file_nps = open('nps_gov_data.html','w')
	file_nps.write(html_1)

nps_soup = BeautifulSoup(html_1,'html.parser')
div_1 = nps_soup.find('ul',{'class':'dropdown-menu'})
states = div_1.find_all('li')
for state in states:
	if 'ar' in state.a['href']:
		url_ar = state.a['href']
		try:
			with open('arkansas_data.html','r') as file_ar:
				html_ark = file_ar.read()
		except:
			response_2 = requests.get(default_url + url_ar)
			html_ar = response_2.text
			file_ar = open('arkansas_data.html','w')
			file_ar.write(html_ar)
	elif 'ca' in state.a['href']:
		url_ca = state.a['href']
		try:
			with open('california_data.html','r') as file_ca:
				html_ca = file_ar.read()
		except:
			response_3 = requests.get(default_url + url_ca)
			html_ca = response_3.text
			file_ca = open('california_data.html','w')
			file_ca.write(html_ca)
	elif 'mi' in state.a['href']:
		url_mi = state.a['href']
		try:
			with open('michigan_data.html','r') as file_mi:
				html_mi = file_mi.read()
		except:
			response_4 = requests.get(default_url + url_mi)
			html_mi = response_4.text
			file_mi = open('michigan_data.html','w')
			file_mi.write(html_mi)


# Try to get and cache main page data if not yet cached
# Result of a following try/except block should be that
# there exists a file nps_gov_data.html,
# and the html text saved in it is stored in a variable 
# that the rest of the program can access.

# We've provided comments to guide you through the complex try/except, but if you prefer to build up the code to do this scraping and caching yourself, that is OK.

# Get individual states' data...

# Result of a following try/except block should be that
# there exist 3 files -- arkansas_data.html, california_data.html, michigan_data.html
# and the HTML-formatted text stored in each one is available
# in a variable or data structure 
# that the rest of the program can access.

# TRY: 
# To open and read all 3 of the files

# But if you can't, EXCEPT:

# Create a BeautifulSoup instance of main page data 
# Access the unordered list with the states' dropdown

# Get a list of all the li (list elements) from the unordered list, using the BeautifulSoup find_all method

# Use a list comprehension or accumulation to get all of the 'href' attributes of the 'a' tag objects in each li, instead of the full li objects

# Filter the list of relative URLs you just got to include only the 3 you want: AR's, CA's, MI's, using the accumulator pattern & conditional statements


# Create 3 URLs to access data from by appending those 3 href values to the main part of the NPS url. Save each URL in a variable.


## To figure out what URLs you want to get data from (as if you weren't told initially)...
# As seen if you debug on the actual site. e.g. Maine parks URL is "http://www.nps.gov/state/me/index.htm", Michigan's is "http://www.nps.gov/state/mi/index.htm" -- so if you compare that to the values in those href attributes you just got... how can you build the full URLs?


# Finally, get the HTML data from each of these URLs, and save it in the variables you used in the try clause
# (Make sure they're the same variables you used in the try clause! Otherwise, all this code will run every time you run the program!)


# And then, write each set of data to a file so this won't have to run again.







######### PART 2 #########

## Before truly embarking on Part 2, we recommend you do a few things:

# - Create BeautifulSoup objects out of all the data you have access to in variables from Part 1
# - Do some investigation on those BeautifulSoup objects. What data do you have about each state? How is it organized in HTML?

# HINT: remember the method .prettify() on a BeautifulSoup object -- might be useful for your investigation! So, of course, might be .find or .find_all, etc...

# HINT: Remember that the data you saved is data that includes ALL of the parks/sites/etc in a certain state, but you want the class to represent just 
# ONE park/site/monument/lakeshore.

# We have provided, in sample_html_of_park.html an HTML file that represents the HTML about 1 park. However, your code should rely upon HTML data about Michigan, 
# Arkansas, and Califoria you saved and accessed in Part 1.

# However, to begin your investigation and begin to plan your class definition, you may want to open this file and create a BeautifulSoup instance of it to do 
# investigation on.

# Remember that there are things you'll have to be careful about listed in the instructions -- e.g. if no type of park/site/monument is listed in input, one of 
# your instance variables should have a None value...

## Define your class NationalSite here:

class NationalSite(object):
	def __init__(self, park_inst):
		self.page = park_inst
		name_list = park_inst.find_all('h3')
		if len(name_list) != 0:
			self.name = name_list[0].text
		else:
			self.name = "None"
		type_list = park_inst.find_all('h2')
		if len(type_list) != 0:
			self.type = type_list[0].text
		else:
			self.type = "None"
		description_list = park_inst.find_all('p')
		if len(description_list) != 0:
			self.description = description_list[0].text
		else:
			self.description = "None"
		location_list = park_inst.find_all('h4',{'class':""})
		if len(location_list) != 0:
			self.location = location_list[0].text
		else:
			self.location = "None"

	def __str__(self):
		try:
			return '{} | {}'.format(self.name,self.location)
		except:
			self.name = "None"
			self.location = "None"
			return '{} | {}'.format(self.name,self.location)

	def __contains__(self,test_string):
		return test_string in self.name

	def get_mailing_address(self):
		links_list = self.page.find_all('a')
		for link in links_list:
			if 'basicinfo' in link.get('href'):
				try:
					if str(link.get('href')) != "None":
						new_url = (link.get('href'))
						response_5 = requests.get(new_url)
						html_basicinfo = response_5.text
						basicinfo_soup = BeautifulSoup(html_basicinfo,'html.parser')
						addresses = basicinfo_soup.find('span',{'class':'street-address'}).text
						return addresses
				except AttributeError:
					addresses = ""
					return addresses

## Recommendation: to test the class, at various points, uncomment the following code and invoke some of the methods / check out the instance variables 
## of the test instance saved in the variable sample_inst:

#f = open("sample_html_of_park.html",'r')
#soup_park_inst = BeautifulSoup(f.read(), 'html.parser') # an example of 1 BeautifulSoup instance to pass into your class
#sample_inst = NationalSite(soup_park_inst)
#print(sample_inst)
#f.close()

######### PART 3 #########

# Create lists of NationalSite objects for each state's parks.

# HINT: Get a Python list of all the HTML BeautifulSoup instances that represent each park, for each state.

try:
	f_1 = open("arkansas_data.html","r")
	ar_soup = BeautifulSoup(f_1.read(),'html.parser')
except:
	response_2 = requests.get(default_url + url_ar)
	html_ar = response_2.text
	ar_soup = BeautifulSoup(html_ar,'html.parser')

arkansas_natl_sites = []
ar_soup_list = ar_soup.find_all('li',{'class':'clearfix'})
for ar_soup_i in ar_soup_list:
	new_inst_1 = NationalSite(ar_soup_i)
	arkansas_natl_sites.append(new_inst_1)
f_1.close()

try:
	f_2 = open("california_data.html","r")
	ca_soup = BeautifulSoup(f_2.read(),'html.parser')
except:
	response_3 = requests.get(default_url + url_ca)
	html_ca = response_3.text
	ca_soup = BeautifulSoup(html_ca,'html.parser')

california_natl_sites = []
ca_soup_list = ca_soup.find_all('li',{'class':'clearfix'})
for ca_soup_i in ca_soup_list:
	new_inst_2 = NationalSite(ca_soup_i)
	california_natl_sites.append(new_inst_2)
f_2.close()

try:
	f_3 = open("michigan_data.html","r")
	mi_soup = BeautifulSoup(f_3.read(),'html.parser')
except:
	response_4 = requests.get(default_url + url_mi)
	html_mi = response_4.text
	mi_soup = BeautifulSoup(html_mi,'html.parser')

michigan_natl_sites = []
mi_soup_list = mi_soup.find_all('li',{'class':'clearfix'})
for mi_soup_i in mi_soup_list:
	new_inst_3 = NationalSite(mi_soup_i)
	michigan_natl_sites.append(new_inst_3) 
f_3.close()

##Code to help you test these out:
#for p in california_natl_sites:
# 	print(p)
#for a in arkansas_natl_sites:
# 	print(a)
#for m in michigan_natl_sites:
# 	print(m)

######### PART 4 #########

## Remember the hints / things you learned from Project 2 about writing CSV 
## files from lists of objects!

## Note that running this step for ALL your data make take a minute or few 
## to run -- so it's a good idea to test any methods/functions you write with just a little bit of data, so running the program will take less time!

## Also remember that IF you have None values that may occur, you might run into some problems and have to debug for where you need to put in some None value / error handling!

outfile1 = open("arkansas.csv","w")
with open('arkansas.csv', 'w') as outfile1:
	writer = csv.writer(outfile1)
	outfile1.write('"name","location","type","get_mailing_address","description"\n')
	for a in arkansas_natl_sites:
		mailing_address = a.get_mailing_address()
		if mailing_address != None:
			mailing_address_1 = mailing_address.strip()
		else:
			mailing_address_1 = "None"
		writer.writerow([a.name,a.location,a.type,mailing_address_1,a.description.strip()])
outfile1.close()

outfile2 = open("california.csv","w")
with open('california.csv','w') as outfile2:
	writer = csv.writer(outfile2)
	outfile2.write('"name","location","type","get_mailing_address","description"\n')
	for p in california_natl_sites:
		mailing_address_2 = p.get_mailing_address()
		if mailing_address_2 != None:
			mailing_address_2 = mailing_address_2.strip()
		else:
			mailing_address_2 = "None"
		writer.writerow([p.name,p.location,p.type,mailing_address_2,p.description.strip()])
outfile2.close()

outfile3 = open("michigan.csv","w")
with open('michigan.csv','w') as outfile3:
	writer = csv.writer(outfile3)
	outfile3.write('"name","location","type","get_mailing_address","description"\n')
	for m in michigan_natl_sites:
		mailing_address_3 = m.get_mailing_address()
		if mailing_address_3 != None:
			mailing_address_3 = mailing_address_3.strip()
		else:
			mailing_address_3 = "None"
		writer.writerow([m.name,m.location,m.type,mailing_address_3,m.description.strip()])
outfile3.close()


