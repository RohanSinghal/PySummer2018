#!/home/vatsalbabel/Work/Anaconda/bin/python

import os
import time
import webbrowser
import requests
from bs4 import BeautifulSoup

print("Choose an option-\n1. Google Search\n2. Google Image Search\n3. Finding the URL\n4. Current time and date\n5. Open Web Browser\n6. IP of all the network\n7. Find EmailId and contact")

#Taking option input from the user
option = int(input())

if option==1:
	#Making a google search
	search = input("Enter a string to search on google - ")
	list1 = search.split()
	for i in list1:
		search = "https://www.google.com/?#q="+i
		webbrowser.open_new_tab(search)

elif option==2:
	#Making a google image search
	search = input("Enter a string to search on google images - ")
	list1 = search.split()
	for i in list1:
		search = "https://www.google.co.in/search?q="+i+"&soruce=lnms&tbm=isch"
		webbrowser.open_new_tab(search)

elif option==3:
	#Scrapting to find the URL from the first page of google
	search = input("Enter a string to find the related url from google - ")
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
	#Getting the current date and the time
	print(time.asctime())

elif option==5:
	#Opening the web browser
	webbrowser.open_new_tab('https://')

elif option==6:
	#Finding the IP of connected system
	output = os.popen('ifconfig').read().strip()
	ethernet = output
	index_of_enp = ethernet.find('inet')
	ethernet = ethernet[index_of_enp::]
	wifi = output[output.find('wlp')::]
	index_of_wifi = wifi.find('inet')
	wifi = wifi[index_of_wifi::]
	if index_of_enp!=-1 and index_of_enp<index_of_wifi:	
		ethernet = ethernet[5::]
		ip = ethernet[:wifi.find(' ')-3]
	else:
		wifi = wifi[5::]
		ip = wifi[:wifi.find(' ')-3]

	ip = ip + "0/24"
	output = os.popen('nmap -sP ' + str(ip)).read()
	list1 = output.splitlines()
	index = 0
	for ii in range(len(list1)):
		list1[index] = str(list1[index]).strip()
		if list1[index].endswith(')'):
			IP_index = list1[index].find('(1')
			print(list1[index][IP_index::])
			list1.pop(index)
		else:
			index += 1		

else:
	#Finding the EmailId and contact number of the admin of the given error
	search = input("Enter the domain name of the website - ")
	search = "whois "+ search
	#Taking console output in a string and filtering the string
	result = os.popen(search).read()
	index = result.find('Admin Phone')
	result = result[index::]
	index = result.find('.com')
	result = result[:index+4]
	list1 = result.splitlines()
	index = 0
	#Finding the email and contant of the admin from the string
	for i in range(len(list1)):
		list1[index] = str(list1[index]).strip()
		if list1[index].count('Ext')>0 or list1[index].count('Fax')>0:
			list1.pop(index)
		else:
			print(list1[index])
			index += 1

	
