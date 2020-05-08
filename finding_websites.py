from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time 
import pandas as pd 
#import csv

##url='https://www.startupindia.gov.in/content/sih/en/search.html?stages=EarlyTraction%20Scaling&roles=Startup&page=300'
driver=webdriver.Firefox()
#driver.get(url)
#iterations = 0
#web_links=[]
#while iterations<20:
##web_links=[]
##website=driver.execute_script("return document.documentElement.outerHTML")
##file = BeautifulSoup(website,'lxml')
##for c in file.findAll('a',class_='img-wrap'):
###web_links.append(c['href'])
##iterations+=1
##time.sleep(5)
#print(web_links)
#del file
link='https://www.startupindia.gov.in'
urls=pd.read_csv('websites.csv')
ful_link=[link+url[1] for url in urls.itertuples()]

comp_info=[]
for links in ful_link:
	print (links)
	driver.get(links)
	iterations = 0
	while iterations<2:
		website=driver.execute_script("return document.documentElement.outerHTML")
		file = BeautifulSoup(website,'lxml')
		comp=file.find('div',class_='company-name')
		try:
			comp_name=comp.p.text.lstrip()
			comp_web=comp.a.text
		except Exception as e:
			comp_name=None
			comp_web=None
		try:
			comp_mobile=comp.find('span',class_='telephone').text.lstrip()
		except Exception as e:
			comp_mobile=None

		try:	
			comp_mail=comp.find('span',class_='mail').text.lstrip()
		except Exception as e:
			#comp_mobile=None
			comp_mail=None
		iterations+=1
		time.sleep(3)
	if comp_mobile==None:
			continue	
	print(comp_name,comp_web,comp_mobile,comp_mail)
	comp_info.append({'Name of Company':comp_name,'Website':comp_web,'Incorporation Date':None,'Contact Number':comp_mobile,'Mail ID':comp_mail})
	#del temp_link
	del file

comp_data=pd.DataFrame(comp_info,columns=['Name of Company','Website','Incorporation Date','Contact Number','Mail ID'])
#with open('companies.html') as companies:
comp_data.to_csv ('startup_list_3.csv', index = False, header=True)
