
import requests
import bs4
import time
import datetime
import calendar

###################################################################
# Main
###################################################################

exercise = -1
while (exercise != 0):
	exercise = int(input("Which exercise would you like to test (1-6, 0 to exit)? "))

	#####################################################
	# Exercise 1:
	#####################################################
	if exercise == 1:
		res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
		if res.status_code == requests.codes.ok:
			print("Everything is OK")
		else:
			print("Something bad happened")
		print(len(res.text))
		print(res.text[:47])
	
	#####################################################
	# Exercise 2:
	#####################################################
	elif exercise == 2:
		res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
		res.raise_for_status()
		fp = open("myFile.txt", "wb")
		for chunk in res.iter_content(100000):
			fp.write(chunk)
		fp.close()

		fp = open("myFile.txt", "r")
		content = fp.readlines()
		print(''.join(content[50:60]))
		fp.close()
		
	#####################################################
	# Exercise 3:
	#####################################################
	elif exercise == 3:
		res = requests.get("https://www.futureme.org/")
		res.raise_for_status()
		soup = bs4.BeautifulSoup(res.text, features="html.parser")
		titles = soup.select("title")
		print(titles[0])
		print(titles[0].getText())
	
	#####################################################
	# Exercise 4:
	#####################################################
	elif exercise == 4:
		res = requests.get("http://hmpg.net/")
		res.raise_for_status()
		soup = bs4.BeautifulSoup(res.text, features="html.parser")
		pgs = soup.select("p")
		for pg in pgs:
			print("-" * 40)
			print(pg)
		for pg in pgs:
			print("-" * 40)
			print(pg.getText())
	
	#####################################################
	# Exercise 5:
	#####################################################
	elif exercise == 5:
		res = requests.get("https://www.daylightofdarkness.com/")
		res.raise_for_status()
		soup = bs4.BeautifulSoup(res.text, features="html.parser")
		imgs = soup.select("img")
		for img in imgs:
			print(img.get("src"))
	
	#####################################################
	# Exercise 6:
	#####################################################
	elif exercise == 6:
		secs = int(input("How many seconds since epoch? "))
		print(time.gmtime(secs))
		print(time.localtime(secs))
		stamp = datetime.datetime.fromtimestamp(secs)
		print(stamp)
		print(stamp.year)
		print(stamp.month)
		print(stamp.hour)
		utcStamp = datetime.datetime.fromtimestamp(calendar.timegm(time.gmtime(secs)))
		print(utcStamp)
		delta = datetime.timedelta(days=30)
		print(stamp + delta)
		print(stamp.strftime("%B %d, %Y"), end='')
		nineEleven = datetime.datetime(2001, 9, 11, 0, 0, 0)
		if stamp < nineEleven:
			print(" is before 9/11")
		else:
			print(" is after 9/11")

	
	#####################################################
	# Invalid choice 
	#####################################################
	elif exercise == 0:
		exit

	else:
		print("Your response must be from 0 to 6, try again: ")
