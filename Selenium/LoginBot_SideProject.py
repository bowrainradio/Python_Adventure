from selenium import webdriver
from secrects import email,password
from time import sleep

class LoginBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login(self):
        self.driver.get('https://www.hackerrank.com')
        sleep(2)
        login_btn = self.driver.find_element_by_xpath('//*[@id="menu-item-2887"]/a')
        login_btn.click()
        login_btn_02 = bot.driver.find_element_by_xpath(
            '//*[@id="post-175"]/div/div/div[1]/div/div/div[2]/div[2]/div/div[4]/div/div/a')
        login_btn_02.click()
        sleep(1)
        email_in = self.driver.find_element_by_xpath('//*[@id="input-1"]')
        #email_in.send_keys(email)
        email_in.send_keys('stupidemail@stupid.com')
        password_in = self.driver.find_element_by_xpath('//*[@id="input-2"]')
        #password_in.send_keys(password)
        password_in.send_keys('StupidPassword')
        last_btn = self.driver.find_element_by_xpath('//*[@id="tab-1-content-1"]/div[1]/form/div[4]/button')
        last_btn.click()

bot = LoginBot()
bot.login()

