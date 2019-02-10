from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import re
import pandas as pd
# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
# driver = webdriver.Chrome(r'path\to\where\you\download\the\chromedriver.exe')
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://www.carfax.com/Used-Cars-in-New-York-NY_c8636")

# Click review button to go to the review section
# review_button = driver.find_element_by_xpath('//li[@class='next']')
# review_button.click()

# Windows users need to open the file using 'wb'
# csv_file = open('reviews.csv', 'wb')
csv_file = open('df.csv', 'w', encoding='utf-8')
writer = csv.writer(csv_file)
# Page index used to keep track of where we are.
while True:
	N = 25
	for i in range(N):
		listno = "listing_" + str(i)
		posts = driver.find_element_by_id(listno).text
		for post in posts:
			post_dict = {}
			yearmakemodel = posts.splitlines()[0]
			notprice = posts.splitlines()[5]
			a,mileage = posts.split("Mileage: ")
			mileage,bodytype = mileage.split(" milesBody Type: ")
			bodytype,color = bodytype.split("Color: ")
			color,engine = color.split("Engine: ")
			engine,b = engine.split("\nDescription:")
			post_dict['Title'] = yearmakemodel
			post_dict['Cost'] = notprice
			post_dict['Miles'] = mileage
			post_dict['Colour'] = color
			post_dict['Body'] = bodytype
			writer.writerow(post_dict.values())
			print(post_dict.values())
			df = pd.DataFrame(post_dict, index=[0])
			df.to_csv('df.csv')
			break
csv_file.close()
driver.quit()