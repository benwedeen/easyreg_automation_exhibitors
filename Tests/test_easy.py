import pytest, allure, time, re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from resources.lists import *

#pytest -v -s Tests\test_easy.py

class Test_Automation:
    @allure.title("testing valid login credentials")
    def test_login(self):
        pytest.skip()
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get(URL)
        self.driver.find_element_by_id(username_id).send_keys(valid_email)
        self.driver.find_element_by_id(password_id).send_keys(valid_access_code)
        self.driver.find_element_by_id(signin_id).click()
        find_menu = self.driver.find_element_by_xpath(menu_dropdown_path).is_displayed()

        if find_menu == True:
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False
    @allure.title("testing invalid login credentials")
    def test_faillogin(self):

        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get(URL)

        self.driver.find_element_by_id(username_id).send_keys(valid_email)
        self.driver.find_element_by_id(password_id).send_keys(invalid_regcode)
        self.driver.find_element_by_id(signin_id).click()
        time.sleep(1)
        html = self.driver.current_url

        if html == invalid_login_URL:
            allure.attach(self.driver.get_screenshot_as_png(), name="Invalid Credentials",
                          attachment_type=allure.attachment_type.PNG)
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False
    @allure.title("testing valid email element")
    def test_email_elements(self): #checking if email login exsists

        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get(URL)
        status = self.driver.find_element_by_id(username_id).is_displayed()
        if status==True:
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False
    @allure.title("testing valid password element")
    def test_password_elements(self): #checking if password login exsists

        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get(URL)
        status = self.driver.find_element_by_id(password_id).is_displayed()
        if status==True:
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False
    @allure.title("testing valid menu booth path")
    def test_menu_booth(self): #checking if schedule menu opens after login
        pytest.skip()
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get(URL)
        self.driver.find_element_by_id(username_id).send_keys(valid_email)
        self.driver.find_element_by_id(password_id).send_keys(valid_access_code)
        self.driver.find_element_by_id(signin_id).click()
        self.driver.find_element_by_xpath(menu_dropdown_path).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(menu_preview_booth_path).click()
        time.sleep(1)
        html = self.driver.current_url

        if html==URL_booth:
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False
    @allure.title("testing 7 menu elements are valid")
    def test_menu_elements(self):#checking for all menu drop down elements
        pytest.skip()
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get(URL)
        self.driver.find_element_by_id(username_id).send_keys(valid_email)
        self.driver.find_element_by_id(password_id).send_keys(valid_access_code)
        self.driver.find_element_by_id(signin_id).click()
        self.driver.find_element_by_xpath(menu_dropdown_path).click()
        time.sleep(1)
        menu_elements = self.driver.find_elements(By.CLASS_NAME, 'nk-menu-text')
        amount = len(menu_elements)
        amount = amount - 2
        if amount==7:
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False








