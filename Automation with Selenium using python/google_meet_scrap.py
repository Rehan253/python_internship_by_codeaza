from selenium import webdriver
from selenium.webdriver.common.by import By
import time

website = 'https://meet.google.com/'
driver = webdriver.Chrome()
driver.get(website)

language_selector = driver.find_element(By.ID, "lang-selector")
driver.execute_script("arguments[0].scrollIntoView(true);", language_selector)
time.sleep(2)

language_selector.click()

# Wait for the language option to be clickable

english=driver.find_element(By.XPATH,"//option[@value='/intl/en-GB/meet/']")
english.click()
time.sleep(2)

# Wait for the element to be clickable
#element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-Bz112c-M1Soyc VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe LQeN7 cjtUbb Dg7t5c']")))
#element.click()

link = driver.find_element(By.XPATH, "//a[@href='https://meet.google.com/new']")
link.click()
time.sleep(30)
driver.quit()
