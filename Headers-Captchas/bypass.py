import undetected_chromedriver as uc
from twocaptcha import TwoCaptcha
from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "https://www.google.com/recaptcha/api2/demo"
page = driver.get(url)
# Site Key
sitekey = driver.find_element(by='id', value='recaptcha-demo').get_attribute('data-sitekey')
print(sitekey)

api_key = "0dcea01750c156f2223bf55f46994d3e"
solver = TwoCaptcha(api_key)
print("Solving captcha...")
response = solver.recaptcha(
  sitekey=sitekey,
  url=url
)

print(f'Captcha Key: {response["code"]}')

# Send Captcha Key to form
driver.execute_script("document.getElementById('g-recaptcha-response').value = '{}';".format(response["code"]))

# Click Submit
driver.find_element(by='xpath', value='//*[@id="recaptcha-demo-submit"]').click()

time.sleep(5)