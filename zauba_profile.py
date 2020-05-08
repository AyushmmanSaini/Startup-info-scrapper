from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
# Advanced CSV loading example
'''data = pd.read_csv(
    "data/files/complex_data_example.tsv",      # relative python path to subdirectory
    sep='\t'           # Tab-separated value file.
    quotechar="'",        # single quote allowed as quote character
    dtype={"salary": int},             # Parse the salary column as an integer 
    usecols=['name', 'birth_date', 'salary'].   # Only load the three columns specified.
    parse_dates=['birth_date'],     # Intepret the birth_date column as a date
    skiprows=10,         # Skip the first 10 rows of the file
    na_values=['.', '??']       # Take any '.' or '??' values as NA
)
'''
c_name_l= pd.read_csv('web_list-2.csv',usecols=['Name of Company','Contact Number'])
#print(c_name_l)
info_list=[]
for comp in c_name_l.itertuples():
	#print(company[1])
	#print()
	if comp==None:
		continue
	company=str(comp[1])
	#ph=comp[2]
	#print(ph)
	print(company)
	company.replace("-"," ")
	url='https://www.zaubacorp.com/companysearchresults/'+'-'.join(str(comp[1]).split(' '))
	#print(url)
	website = requests.get(url).text
	file = BeautifulSoup(website,'lxml')
	try:
		file= file.table.find('a')
	except Exception as e:
		continue
	
	link=file['href']
	c_name=file.text.lstrip()
	#print(company)
	#print(c_name)
	name=c_name.split(' ')[0]
	#print(name)
	name1=company.split(' ')[0] 
	#print(name1)
	if name==name1 or name==name1.title() or name==name1.lower() or name==name1.capitalize() or name==name1.upper() or company==c_name or company==c_name.title() or company==c_name.upper() or company==c_name.lower() or company==c_name.capitalize():
		website = requests.get(link).text
		file = BeautifulSoup(website,'lxml')
		file_text=file.find('div',class_='container information')

		comp_info=file_text.text
		comp_info=comp_info.split('\n')[1]

		comp_name=comp_info.split('is')[0].lstrip()

		#c#omp_incdate=comp_info[comp_info.find('on')+3:comp_info.find('.')]
		file1=file.body.find('table',class_='table table-striped').tbody.text
		comp_incdate=file1.split('\n')[62].split(' ')[2]

		comp_email=file.find('div',class_='col-12')
		comp_email=comp_email.p.text.split(' ')[3]
		try:
			file2=file.findAll('tr',class_='accordion-toggle main-row')
			comp_ceo=[]
			for i in range(len(file2)):
				comp_ceo.append(file2[i].a.text.lstrip())
			#print(comp_ceo)
		except Exception as e:
			continue
		#print(comp_info)

	else:
		continue	

	info_list.append({'Name of Company':comp_name,'Incorporation Date':comp_incdate,'Directors/Partners':comp_ceo ,'Contact Number':comp[2],'Mail ID':comp_email})

comp_data=pd.DataFrame(info_list,columns=['Name of Company','Incorporation Date','Directors/Partners','Contact Number','Mail ID'])
#with open('companies.html') as companies:
comp_data.to_csv ('startuplist-3.csv', index = False, header=True)	