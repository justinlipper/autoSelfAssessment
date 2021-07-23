from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime  
from datetime import timedelta 
import time

#Path string that works with the selenium library
PATH = "/mnt/c/Program Files (x86)/chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://forms.zohopublic.com/salutemissioncritical/form/COVID19SelfScreening/formperma/VLJ-iMX8LcJ1kfsYkDJZodRKKpTQbYVCZaaPAOAHI4o")
#For testing
#driver.get("https://techwithtim.net")


#################################PAGE#########################################
search = driver.find_element_by_xpath("//input[@complink='Name_First']")
search.send_keys("Justin")

search = driver.find_element_by_xpath("//input[@complink='Name_Last']")
search.send_keys("Lipper")

search = driver.find_element_by_xpath("//input[@name='Email']")
search.send_keys("justinleelipper@gmail.com")

search = driver.find_element_by_xpath("//input[@complink='Address_City']")
search.send_keys("San Jose")

search = driver.find_element_by_xpath("//input[@complink='Address_Region']")
search.send_keys("CA")

tomorrow = datetime.now() + timedelta(days=1)
tomorrow = tomorrow.strftime("%d-%b-%Y %H:%M %p")

#Variable for the if statement
today = str(datetime.now().strftime("%a"))

if today == "Fri":
	tomorrow = datetime.now() + timedelta(days=3)
	tomorrow = tomorrow.strftime("%d-%b-%Y 10:00 AM")
else: 
	tomorrow = datetime.now() + timedelta(days=1)
	tomorrow = tomorrow.strftime("%d-%b-%Y 10:00 AM")

search = driver.find_element_by_xpath("//input[@name='DateTime1']")
search.send_keys(tomorrow)

search = driver.find_element_by_xpath("//option[@value='Evoque']")
search.click()

search = driver.find_element_by_xpath("//label[@for='Checkbox_13']")
search.click()

search = driver.find_element_by_xpath("//label[@for='Checkbox3_2']")
search.click()

search = driver.find_element_by_xpath("//label[@for='Checkbox6_1']")
search.click()

search = driver.find_element_by_xpath("(//button[@elname='next'])[1]")
search.click()


#################################PAGE 2#########################################
search = driver.find_element_by_xpath("//label[@for='Checkbox1_2']")
search.click()

search = driver.find_element_by_xpath("//label[@for='Checkbox4_2']")
search.click()

search = driver.find_element_by_xpath("//label[@for='Checkbox2_3']")
search.click()

next_button = driver.find_element_by_xpath("(//button[@elname='next'])[2]")
next_button.click()

search = driver.find_element_by_xpath("//span[@class='cusChoiceSpanWrap']")
search.click()

search = driver.find_element_by_xpath("//button[@elname='submit']")
search.click()

driver.quit()
