# -*- coding: utf-8 -*-
import os
import time


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import Select


from utils import captcha_three

class MailScheduler():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options, executable_path=os.getcwd() + './chromedriver')
        

    def register(self):
        url = "https://passport.yandex.ru/registration"
        for i in range(1,3):
            self.driver.get(url)

        self.driver.find_elements_by_xpath("//input[contains(@id,'firstname')]")
        self.driver.find_elements_by_xpath("//input[contains(@id,'lastname')]")
        self.driver.find_elements_by_xpath("//input[contains(@id,'login')]")
        self.driver.find_elements_by_xpath("//input[@id='password']")
        self.driver.find_elements_by_xpath("//input[contains(@id,'password_confirm')]")
        
        self.driver.find_elements_by_xpath("//span[contains(.,'У меня нет телефона')]").click()
        #
        select = Select(self.driver.find_elements_by_xpath("//select[contains(@class,'Select2-Control')]"))
        select.select_by_visible_text('Фамилия вашего любимого музыканта')
        #
        self.driver.find_elements_by_xpath("//input[contains(@id,'hint_answer')]").send_keys('Presley')

        
