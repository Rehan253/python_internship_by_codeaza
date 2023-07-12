import undetected_chromedriver as uc
from twocaptcha import TwoCaptcha
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up undetected Chrome driver

driver = webdriver.Chrome()

# Navigate to the webpage
url = "https://www.google.com/recaptcha/api2/demo"
driver.get(url)

# Wait for the iframe to load
time.sleep(5)

# Switch to the reCAPTCHA iframe
iframe = driver.find_element(By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/api2/anchor']")
driver.switch_to.frame(iframe)

# Find and click the reCAPTCHA checkbox
checkbox = driver.find_element(By.CSS_SELECTOR, ".rc-anchor-checkbox")
checkbox.click()

# Switch back to the default content
driver.switch_to.default_content()

# Wait for the checkbox to be checked (optional)
time.sleep(5)

# Close the browser
driver.quit()
