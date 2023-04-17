from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from Source import Source
import platform
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import random


class MSMSource(Source):

    def __init__(self):
        super().__init__("MSM", "tab")

    def generateNumberSequence(self, lengthTab):
        driver = webdriver.Chrome(ChromeDriverManager().install())
            
        # navigate to the website
        driver.get('https://sadale.net/27/online-middle-square-method-generator')
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "MSM_seed"))
        )
        # find the input fields and submit button

        seed_input = driver.find_element_by_id('MSM_seed')
        num_count = driver.find_element_by_id('MSM_count')
        digits_count = driver.find_element_by_id('MSM_digits')
        output_div = driver.find_element_by_id('MSM_output')
        submit_btn = driver.find_element_by_xpath('//input[@value="Generate random numbers!"]')

        # enter the data and submit the form
        seed_input.clear()
        num_count.clear()
        digits_count.clear()
        seed_input.send_keys(random.randint(1000, 9999))
        num_count.send_keys(str(lengthTab))
        digits_count.send_keys("4")
        submit_btn.click()

        # wait until the text area has some text
        WebDriverWait(driver, 10).until(lambda driver: output_div.get_attribute("value") != "")

        # get the text
        output_text = output_div.get_attribute("value")
        # extract the generated pseudo-random numbers
        output_text = output_div.get_attribute("value")

        l = output_text.split(', ')
        numbers = [int(st) for st in l]
        print(numbers)
        self.setNumberSequence(numbers)
        
        # close the webdriver
        driver.quit()
        return self.getNumberSequence()
    