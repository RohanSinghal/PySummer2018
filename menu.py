#!/home/vatsalbabel/Work/Anaconda/bin/python

import os

print("Choose an option-\n1. Google Search\n2. Google Image Search\n3. Finding the URL\n4. Current time and date\n5. Open Web Browser\n6. IP of all the network\n7. Verify EmailId and contact")

option = int(input())

if option==1:
	search = input("Enter a string to search on google - ")
	search = search.replace(" ", "+")
	search = "firefox www.google.com/?#q="+search
	os.system(search)
elif option==2:
	search = input("Enter a string to search on google images - ")
	search = search.replace(" ", "+")
	search = "firefox www.google.com/?tbm=isch&#q="+search
	os.system(search)
else:
	pass


