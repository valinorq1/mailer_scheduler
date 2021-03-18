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
        self.driver.get(url)
        #for i in range(1,3):
            #self.driver.get(url)

        #  основные данные
        self.driver.find_element_by_xpath("//input[contains(@id,'firstname')]").send_keys('Саша')
        self.driver.find_element_by_xpath("//input[contains(@id,'lastname')]").send_keys('Макушкин')
        self.driver.find_element_by_xpath("//input[contains(@id,'login')]").send_keys('Presley14687421')
        self.driver.find_element_by_xpath("//input[@id='password']").send_keys('En1996ru')
        self.driver.find_element_by_xpath("//input[contains(@id,'password_confirm')]").send_keys('En1996ru')
        
        self.driver.find_element_by_xpath("//span[contains(.,'У меня нет телефона')]").click()
        time.sleep(1.5)
        select = Select(self.driver.find_element_by_xpath("//select[contains(@class,'Select2-Control')]"))
        select.select_by_visible_text('Фамилия вашего любимого музыканта')
        self.driver.find_element_by_xpath("//input[contains(@id,'hint_answer')]").send_keys('Presley')  #  секретный вопрос

        captcha_field = self.driver.find_element_by_xpath("//input[contains(@id,'captcha')]")

        while True:
            # на всякий чистим поле капчи
            for k in range(1,15):
                captcha_field.send_keys(Keys.BACK_SPACE)
            #  посылаем на разгадку
            captcha = captcha_three(self.driver.page_source, API)
            if captcha:
                captcha_field.send_keys(captcha)
                self.driver.find_element_by_xpath("//button[@data-t='button:action'][contains(.,'Зарегистрироваться')]").click()
                if 'Ваш аккаунт готов!' in self.driver.page_source:
                    break
                else:
                    continue
            else:
                continue
            


st = MailScheduler()
st.register()
