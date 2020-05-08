from bs4 import BeautifulSoup
import requests
import re
#from selenium import webdriver
#import time
import pandas as pd
#website = requests.get('http://www.thetinytapps.com/contact-us/').text

def get_phn(c_web):
	try:
		website = requests.get(c_web).text
	except:
		return	
	#website=driver.execute_script("return document.documentElement.outerHTML")
	file = BeautifulSoup(website,'lxml')
	try:
	    phone = file.select("a[href*=callto]")[0].text
	    return (phone)
	except:
	    pass
	
	try:
	    phone = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-][2-9][0-9]{2}[-][0-9]{4}\b', file.text)[0]
	    return (phone)
	except:
	    pass

	try:
	   phone = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b', file.text)[-1]
	   return (phone)
	except:
	    pass

	try:
	   phone = re.findall(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', file.text)
	   return (phone)
	except:
	    pass
	try:
	   phone = re.findall(r'.*?(\(?\d{3})? ?[\.-]? ?\d{3} ?[\.-]? ?\d{4}).*?', file.text)
	   return (phone)
	except:
	    pass
	try:
	   phone = re.findall(r'(\+?\d[-\.\s]?)?(\(\d{3}\)\s?|\d{3}[-\.\s]?)\d{3}[-\.\s]?\d{4}', file.text)
	   return (phone)
	except:
	    pass
	return 

#driver=webdriver.Firefox()
web_l= pd.read_csv('startup_list_1.csv',usecols=['Website','Name of Company'])
for web in web_l.itertuples():
	c_web=web[2]
	c_name=web[1]
	print (c_name)
	if c_name=='Tracxpress distribution solutions pvt ltd':
		continue
	if c_web[4]!='http':
		c_web='http://'+c_web
	
	phn = get_phn(c_web)
	
	if phn==None:
		#cont=['/contact-us','/contact','/contact']
	  	print('Phn no not found')
		#iterations+=1
		#time.sleep(2)
	else:
		print(phn)		