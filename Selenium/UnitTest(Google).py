from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_search_machinelearning(self):
        """Search for *Machine learning* and prints out suggestion and titles of every result from 10 pages"""

        self.driver.get("https://google.com")

        # closing google privacy popup

        iframe = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable([By.CSS_SELECTOR, '#cnsw > iframe'])
        )
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_id("introAgreeButton").click();

        # Searching Machine Learning
        self.driver.find_element_by_name("q").send_keys("Machine Learning")
        self.driver.implicitly_wait(2)

        # Takes a screenshot before search click
        self.driver.save_screenshot("reports/screenshot.png")

        # Saves autocomplete suggestion and prints them out
        searchList = self.driver.find_elements_by_xpath("//li[@class='sbct']//b")
        print(f"Total search suggestions: {len(searchList)}")
        for element in searchList:
            print(f"Machine Learning {element.text}")
        self.driver.find_element_by_name("btnK").click()

        # Keeps saving titles from every page till it will hit 10th page
        page_num = 1
        title_index = 1
        searchLength = 0
        while page_num <= 9:
            self.driver.implicitly_wait(2)
            searchTitles = self.driver.find_elements_by_xpath("//div[@class='tF2Cxc']//h3")
            searchLength += len(searchTitles)
            for title in searchTitles:
                print(f"{title_index}. {title.text}")
                title_index += 1
            self.driver.find_element_by_xpath('//*[@id="pnnext"]').click()
            page_num += 1
        print(f"Total search result for {page_num} pages: {searchLength}")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/rainbow/Desktop/RainbowCode/Python/Selenium/reports"))