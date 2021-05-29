import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()

driver.get('http://suninjuly.github.io/explicit_wait2.html')
button = WebDriverWait(driver, 12).until(
    text_to_be_present_in_element((By.ID, "price"), "100"))

driver.find_element_by_xpath("//button[@id='book']").click()
x_element = driver.find_element_by_xpath("//span[@id='input_value']")
x = x_element.text
y = calc(x)
driver.find_element_by_xpath("//input[@id='answer']").send_keys(y)
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
driver.quit()
