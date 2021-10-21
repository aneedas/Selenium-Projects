### Parameters ###
test_url = "https://www.instagram.com/"
hashtag_url = "https://www.instagram.com/explore/tags/rescuedog/"
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
        self.driver = webdriver.Firefox(executable_path='/Users/Aneeta/Documents/PY PROJECTS/test/geckodriver')
        self.driver.maximize_window()
        self.url = test_url
        self.test_username = test_username
        self.test_password = test_password
        self.hashtag_url = hashtag_url


	### Test Execution ###
    def test_main_function(self):


        # go to instagram 
        driver = self.driver
        driver.get(self.url)

        time.sleep(5)

        #Login
        username = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')
        login_button = driver.find_element_by_xpath("//*[contains(text(), 'Log In')]")

        username.send_keys(self.test_username)
        password.send_keys(self.test_password)

        time.sleep(1)
        login_button.click()

        time.sleep(7)

        driver.get(self.hashtag_url)
        time.sleep(5)
        # target hashtag
        #search_bar = driver.find_element_by_class_name("LWmhU._0aCwM")
        #search_bar.click()
        #time.sleep(3)
        #search_bar_active = driver.find_element_by_class_name('XTCLo.x3qfX')
        #search_bar_active.send_keys(self.test_hashtag)
        #time.sleep(5)
        #search_bar_active.send_keys(Keys.ENTER)
        #time.sleep(5)
        # like limited number of posts
        posts = driver.find_elements_by_class_name("eLAPa")

        posts[0].click()

        num = 5
        for x in range(num):
            time.sleep(6)
            like_button = driver.find_element_by_class_name("QBdPU.B58H7")
            driver.execute_script("arguments[0].click();", like_button)
            #like_button.click()
            time.sleep(5)
            next = driver.find_element_by_class_name("_65Bje.coreSpriteRightPaginationArrow")
            driver.execute_script("arguments[0].click();", next)
            #next.click()


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

    