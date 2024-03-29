from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import requests
import time


class Guvi:
    url = "https://www.zenclass.in/login"
    driver = webdriver.Firefox()
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

    def main_menu(self):
     # Accessing Zen portal items on the left-hand side of the page

        time.sleep(5)
        l_menu = self.driver.execute_script(
                " l_menu_items=document.getElementsByClassName"
                '("list-scroll py-3 color-area");'
                " l_menu_logo= document.getElementsByClassName"
                '("ml-3 d-inline-block mt-3 font-weight-bold")[0].innerText;'
                "l_menu_head=document.getElementsByClassName"
                '("list-scroll py-3 active-area active-left-bar")[0].innerText;'
                " l_menu=[];"
                """for (let index = 0; index < l_menu_items.length; index++)
                       {
                       l_menu[index]=l_menu_items.item(index).innerText;
                       }
                       l_menu.splice(0,0,l_menu_logo,l_menu_head);
                       return l_menu ;"""
        )
     # convert list to dataframe
        df_fm = pd.DataFrame(l_menu, columns=["Main-menu"])

        writer = pd.ExcelWriter("ZenClass.xlsx", engine="xlsxwriter")

     # Convert the dataframe to an XlsxWriter Excel object.
        df_fm.to_excel(writer, sheet_name="Main-menu", index=False)

     # Get the xlsxwriter workbook and worksheet objects.
        workbook = writer.book
        worksheet = workbook.add_worksheet("Class")
     # Take screenshot of the page
        self.driver.get_full_page_screenshot_as_file("Class.png")

     # Insert an image.
        worksheet.insert_image("A1", "Class.png")

     # Close the Pandas Excel writer and output the Excel file.
        writer.save()
        return df_fm

     #query
    def query(self):
        heading = "Guvi Python AT – 1 &2 Automation Project"
        body = "This is a Project Test Code Running for the Python Automation –1&2 Project Given by mentor Mr. Suman Gangopadhyay"

        query_button: str = '//*[@id="root"]/div[1]/nav/ul/div[6]/li/span/div/div[2]'
        query_button1 = self.driver.find_element(by=By.XPATH, value=query_button)
        query_button1.click()
        time.sleep(3)

        normal: str = '// *[ @ id = "root"] / nav'
        just1 = self.driver.find_element(by=By.XPATH, value=normal)
        just1.click()
        time.sleep(3)

     # create button code
        create_button: str = '//*[@id="root"]/div[2]/div/div[1]/div[1]/button'
        create_button1_query = self.driver.find_element(by=By.XPATH, value=create_button)
        create_button1_query.click()
        time.sleep(3)
     # close button code
        close_button: str = '/html/body/div/div[2]/div/div[2]/div[6]/div[2]/div/div/section[3]/div[2]/button[1]'
        close_button1 = self.driver.find_element(by=By.XPATH, value=close_button)
        close_button1.click()
        time.sleep(3)
     #category
        category: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[1]/select'
        category1 = self.driver.find_element(by=By.XPATH, value=category)
        category1.click()
        time.sleep(3)

        category_option: str ='//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[1]/select/option[4]'
        category_option1 = self.driver.find_element(by=By.XPATH, value=category_option)
        category_option1.click()
        time.sleep(3)
     #subcategory
        subcategory: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[2]/select'
        subcategory1 = self.driver.find_element(by=By.XPATH, value=subcategory)
        subcategory1.click()
        time.sleep(3)

        subcategory_option: str ='//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[2]/select/option[2]'
        subcategory_option1 = self.driver.find_element(by=By.XPATH, value=subcategory_option)
        subcategory_option1.click()
        time.sleep(3)
     # languagecode
        language: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[3]/select'
        language1 = self.driver.find_element(by=By.XPATH, value=language)
        language1.click()
        time.sleep(3)

        language_option: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[3]/select/option[4]'
        language_option1 = self.driver.find_element(by=By.XPATH, value=language_option)
        language_option1.click()
        time.sleep(3)
     # query title
        query_title: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[5]/div/input'
        query_title1 = self.driver.find_element(by=By.XPATH, value=query_title)
        query_title1.send_keys(heading)
        time.sleep(3)

        query_description: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[5]/textarea'
        query_description1 = self.driver.find_element(by=By.XPATH, value=query_description)
        query_description1.send_keys(body)
        time.sleep(3)

        create_button1: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[13]/div/button'
        create_button_xpath = self.driver.find_element(by=By.XPATH, value=create_button1)
        create_button_xpath.click()
        time.sleep(3)


s = Guvi()



