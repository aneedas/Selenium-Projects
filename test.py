# This program tests Facebook's login and logout functions #

### Parameters ###
test_url = "https://facebook.com"
test_username = "email@gmail.com"
test_password = "pw"


### Imports ###
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys


### Test Class ###
class PythonOrgSearch(unittest.TestCase):

	### Test Setup ###
	def setUp(self):

		self.driver = webdriver.Firefox(executable_path=r'/Users/aneeta/Desktop/test/geckodriver')
		self.driver.maximize_window()
		self.url = test_url
		self.test_username = test_username
		self.test_password = test_password


	### Test Execution ###
	def test_main_function(self):	


		driver = self.driver
		driver.get(self.url)

		time.sleep(10)
		#Step 1) 
		email = driver.find_element_by_id("email")
		email.send_keys(self.test_username)

		password = driver.find_element_by_id("pass")
		password.send_keys(self.test_password)



		#Click login button
		searchbutton = driver.find_element_by_name("login")
		searchbutton.click()


		#Click logout button
		time.sleep(10)

		menubutton = driver.find_element_by_css_selector("div[aria-label='Account']")
		menubutton.click()

		time.sleep(10)

		logout = driver.find_element_by_xpath ('//*[text()="Log Out"]')

		time.sleep(10)

    
    ### Test Tear Down ###	
	def tearDown(self):

		result = str(sys.exc_info()[1])
		if result == "none" or result == "None":
			print("test.py passed.")
			

		else:
			print(str(result) + "$ test.py failed.")


		self.driver.quit()


if __name__ == "__main__":
	unittest.main()
