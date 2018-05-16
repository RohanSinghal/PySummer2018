#!/home/vatsalbabel/Work/Anaconda/bin/python

import os
import time
import webbrowser
import requests
from bs4 import BeautifulSoup

print("Choose an option-\n1. Google Search\n2. Google Image Search\n3. Finding the URL\n4. Current time and date\n5. Open Web Browser\n6. IP of all the network\n7. Verify EmailId and contact")

option = int(input())

if option==1:
	search = input("Enter a string to search on google - ")
	list1 = search.split()
	for i in list1:
		search = "https://www.google.com/?#q="+i
		webbrowser.open_new_tab(search)

elif option==2:
	search = input("Enter a string to search on google images - ")
	list1 = search.split()
	for i in list1:
		search = "https://www.google.co.in/search?q="+i+"&soruce=lnms&tbm=isch"
		webbrowser.open_new_tab(search)

elif option==3:
	search = input("Enter a string to search on google - ")
	list1 = search.split()
	for i in list1:
		search = "https://www.google.co.uk/search?q=" + i
		page = requests.get(search)
		soup = BeautifulSoup(page.text, "html.parser")
		aas = soup.findAll('a')	
		for i in aas:
			url = i.get('href')
			index = url.find('?q=')
			url = url[index+3::]
			if url.find('https://')==0:
				index = url.find('&')
				print(url[:index])

elif option==4:
	print(time.asctime())

elif option==5:
	webbrowser.open_new_tab('https://')

elif option==6:
	os.system('nmap -sP 10.0.0.0/24')

else:
	pass
