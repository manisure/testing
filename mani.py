from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import requests
import time




class Guvi:
    url = "https://www.zenclass.in/login"
    s = Service(executable_path="C:\selenium_driver firefox\geckodriver.exe")
    driver = webdriver.Firefox(service=s)
    data = requests.get(url)
    driver.maximize_window()

    def Login(self):
        username = "mani.kandan25@yahoo.com"
        password = "Sab996233@"
        self.driver.get(self.url)
        time.sleep(5)
     # username
        username_xpath = '/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input'
        username1 = self.driver.find_element(by=By.XPATH, value=username_xpath)
        username1.send_keys(username)
        time.sleep(5)
     #password
        password_xpath = '/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input'
        password1 = self.driver.find_element(by=By.XPATH, value=password_xpath)
        password1.send_keys(password)
        time.sleep(5)
     #login
        submit_button_xpath = '/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/button'
        submit_button = self.driver.find_element(by=By.XPATH, value=submit_button_xpath)
        submit_button.click()
        time.sleep(5)
     #query
    def query(self):
        heading = "Guvi Python AT – 1 &2 Automation Project"
        body = "This is a Project Test Code Running for the Python Automation –1&2 Project Given by mentor Mr. Suman Gangopadhyay"

        query_button: str = '/html/body/div/div[1]/nav/ul/div[6]/li/span/div/div[2]'
        query_button1 = self.driver.find_element(by=By.XPATH, value=query_button)
        query_button1.click()
        time.sleep(3)
     # create button code
        create_button: str = '/html/body/div/div[2]/div/div[1]/div[1]/button'
        create_button1_query = self.driver.find_element(by=By.XPATH, value=create_button)
        create_button1_query.click()
        time.sleep(3)
     # close button code
        close_button: str = '/html/body/div/div[2]/div/div[2]/div[6]/div[2]/div/div/section[3]/div[2]/button[1]'
        close_button1 = self.driver.find_element(by=By.XPATH, value=close_button)
        close_button1.click()
        time.sleep(3)
     #category
        category: str = '/html/body/div/div[2]/div/div[2]/div/div/form/div[2]/div[1]/select'
        category1 = self.driver.find_element(by=By.XPATH, value=category)
        category1.click()
        time.sleep(3)
     #subcategory
        subcategory: str = '/html/body/div/div[2]/div/div[2]/div/div/form/div[2]/div[2]/select'
        subcategory1 = self.driver.find_element(by=By.XPATH, value=subcategory)
        subcategory1.click()
        time.sleep(3)
     # languagecode
        language: str = '/html/body/div/div[2]/div/div[2]/div/div/form/div[2]/div[4]/select'
        language1 = self.driver.find_element(by=By.XPATH, value=language)
        language1.click()
        time.sleep(3)
     # query title
        query_title: str = '/html/body/div/div[2]/div/div[2]/div/div/form/div[5]/div/input'
        query_title1 = self.driver.find_element(by=By.XPATH, value=query_title)
        query_title1.send_keys(heading)
        time.sleep(3)

        query_description: str = '/html/body/div/div[2]/div/div[2]/div/div/form/div[5]/textarea'
        query_description1 = self.driver.find_element(by=By.XPATH, value=query_description)
        query_description1.send_keys(body)
        time.sleep(3)

        create_button1: str = '/html/body/div/div[2]/div/div[2]/div/div/form/div[13]/div/button'
        create_button_xpath = self.driver.find_element(by=By.XPATH, value=create_button)
        create_button_xpath.click()
        time.sleep(3)


s = Guvi()
s.Login()




