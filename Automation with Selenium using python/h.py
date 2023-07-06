from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Specify the path to your webdriver executable (e.g., chromedriver)
driver = webdriver.Chrome()

# Load the webpage
driver.get('https://sunnah.com/bukhari/1')

# Find the radio button using the XPath expression
radio_button_xpath = '//input[@id="ch_urdu"]'
radio_button = driver.find_element(By.XPATH,radio_button_xpath)


# Click the radio button
radio_button.click()

time.sleep(2)
# Close the Selenium webdriver when you're done
hadiths= driver.find_elements(By.XPATH,'//div[@class="urdu_hadith_full urdu"]')

for h in hadiths:
    print(h.text)



  

