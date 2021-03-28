from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import requests
import base64


class messengerBot():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def getMemes(self):
        self.driver.get('https://giphy.com/explore/website')
        sleep(2)
        self.driver.find_element_by_id('didomi-notice-agree-button').click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        listSrc = []
        for x in range(1, 11):
            meme = bot.driver.find_element_by_xpath(f'//*[@class="giphy-grid"]//a[{x}]')
            memeHref = meme.get_attribute('href')
            listSrc.append(memeHref)
        print(listSrc)
        x = 1
        for meme in listSrc:
            self.driver.get(meme)
            self.driver.find_element_by_xpath('//*[@id="react-target"]/div/div[5]/div/div[2]/div[1]/div[2]/div[2]/div[2]/i').click()
            link = bot.driver.find_element_by_xpath('//*[@id="react-target"]/div/div[5]/div/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/input')
            print(f"Link for Meme nr{x}: {link.get_attribute('value')}")
            myMeme = requests.get(link.get_attribute('value'), allow_redirects=True)
            open(f'gifs/meme{x}.gif', 'wb').write(myMeme.content)
            x += 1

    def googleSearch(self):
        searchThing = input("What's for today?: ")
        quantityOfMemes = int(input("How many memes?(max 20): "))+1
        self.driver.get('https://www.google.com')
        iframe = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable([By.CSS_SELECTOR, '#cnsw > iframe'])
        )
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_id("introAgreeButton").click()

        self.driver.find_element_by_name("q").send_keys(searchThing)
        sleep(1)
        self.driver.find_element_by_name("btnK").click()
        self.driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
        sleep(1)
        listSrc = []
        for x in range(1, quantityOfMemes):
            meme = self.driver.find_element_by_xpath(f'//*[@class="islrc"]//*[@class="isv-r PNCib MSM1fd BUooTd"][{x}]//img').get_attribute('src')
            listSrc.append(meme)

        x = 1
        for memeSrc in listSrc:
            print(x)
            head, data = memeSrc.split(',', 1)
            file_ext = head.split(';')[0].split('/')[1]
            plain_data = base64.b64decode(data)
            with open(f'/Users/rainbow/Desktop/RainbowCode/Python/Selenium/imgs/memes/image{x}.' + file_ext, 'wb') as f:
                f.write(plain_data)
            x += 1

    def sendGifs(self):
        location = input("What for today?: ")
        name = input("Who we're targeting today?: ")
        hours = float(input("How many hours apart?: "))
        # seconds in one hour
        seconds = 3600
        total_time = round(int(hours * seconds))
        self.driver.get('https://www.messenger.com')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@class="_9o-r"]//button[2]').click()
        sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys("666096756")
        self.driver.find_element_by_xpath('//*[@id="pass"]').send_keys("Imyamvymfgmsa1920")
        self.driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
        sleep(10)
        self.driver.find_element_by_xpath(f'//*[@class="aahdfvyu"]//*[@class="l9j0dhe7"]//span[contains(text(), "{name}")]//..//..//../../../../../../../../../a').click()
        sleep(2)
        for memesIndex in range(1,11):
            if location == "gifs":
                image_path = f"/Users/rainbow/Desktop/RainbowCode/Python/Selenium/imgs/gifs/meme{memesIndex}.gif"
            elif location == "memes":
                image_path = f"/Users/rainbow/Desktop/RainbowCode/Python/Selenium/imgs/memes/image{memesIndex}.jpeg"
            image_input = self.driver.find_element_by_xpath('//*[@class="tkr6xdv7"]//input')
            image_input.send_keys(image_path)
            sleep(1)
            self.driver.find_element_by_xpath('//*[@class="oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 pq6dq46d mg4g778l btwxx1t3 pfnyh3mw p7hjln8o knvmm38d cgat1ltu bi6gxh9e kkf49tns tgvbjcpo hpfvmrgz cxgpxx05 dflh9lhu sj5x9vvc scb9dxdr l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l"]').click()
            sleep(total_time)

        self.driver.close()
        self.driver.quit()

# bot = messengerBot()
# bot.googleSearch()


