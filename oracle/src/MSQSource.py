from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from Source import Source

class LCGSource(Source):

    def __init__(self):
        super().__init__("MSQ", "tab")

    def getNumberSequence(self, lengthTab):
        # set up the webdriver
        driver = webdriver.Chrome('/home/w116511/Downloads/chromedriver')
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
        seed_input.send_keys("5484")
        num_count.send_keys("10")
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
        # close the webdriver
        driver.quit()

        return