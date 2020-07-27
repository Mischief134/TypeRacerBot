

import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



browser = webdriver.Chrome()
browser.get('https://play.typeracer.com')
time.sleep(6)
race_btn = browser.find_elements_by_xpath('//*[@id="dUI"]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/a')[0]

race_btn.click()
time.sleep(16)
text_bar = browser.find_element_by_css_selector('input[type="text"][class="txtInput"][autocorrect="off"][autocapitalize="off"]')



essay = browser.find_elements_by_css_selector('span[unselectable="on"]')
res=""
if len(essay)==2:
      res = essay[0].text+" "+essay[1].text
elif len(essay)==3:
      res = essay[0].text+essay[1].text+" "+essay[2].text

print(res)

for character in res:
    text_bar.send_keys(character)
    time.sleep(0.07)

text_bar.send_keys('.')

