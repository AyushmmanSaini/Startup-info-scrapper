from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time 
#import pandas as pd 
#import csv

url='https://www.startupindia.gov.in/content/sih/en/search.html?stages=EarlyTraction%20Scaling&roles=Startup&page=300'
driver=webdriver.Firefox()
driver.get(url)
iterations = 0
web_links=[]
while iterations<20:
	web_links=[]
	website=driver.execute_script("return document.documentElement.outerHTML")
	file = BeautifulSoup(website,'lxml')
	for c in file.findAll('a',class_='img-wrap'):
	web_links.append(c['href'])
	iterations+=1
	time.sleep(5)
	print(web_links)
	del file

	## We can save the list of links into csv for further use