from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Uses the chromedriver file
browser = webdriver.Chrome("./chromedriver")

# Web Site URL
browser.get("https://web.whatsapp.com/")

# Config
receptor = '"Receptor name"'
wait_qr = WebDriverWait(browser, 60)
x_arg = '//span[contains(@title, ' + receptor + ')]'
target = wait_qr.until(
    expected_conditions.presence_of_element_located((By.XPATH, x_arg)))

# Click en el receptor
target.click()

# Input class name is _1Plpp in Whatsapp web
input_box = browser.find_element_by_class_name("_1Plpp") 

message = "Mensaje a enviar"
for i in range(5):
    # Five messages
    input_box.send_keys(message + Keys.ENTER)

a = input("")
