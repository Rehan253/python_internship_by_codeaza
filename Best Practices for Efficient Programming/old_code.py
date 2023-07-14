import logging
import schedule
import time
import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def setup_logger():
    logging.basicConfig(filename='app.log', level=logging.INFO, 
                        format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

def job():
    logging.info("Job started.")
    website = 'https://www.daraz.pk/laptops/?spm=a2a0e.home.cate_7.5.35944076rBD2Nh'
    path = 'C:/SeleniumDriver/chromedriver.exe'

    # Create a connection to your MySQL server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="daraz_db"
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS daraz_db")

    # Create a new table for laptops
    mycursor = mydb.cursor()
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS laptops (
            title VARCHAR(500),
            price VARCHAR(255),
            rating VARCHAR(255)
        )
    """)

    def scroll_to_end(driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    driver = webdriver.Chrome()
    driver.get(website)

    #pagination
    pagination = driver.find_element(By.XPATH,"//ul[@class='ant-pagination ']")
    pages = pagination.find_elements(By.TAG_NAME,'li')
    last_page = int(pages[-2].text)
    current_page=1
    inserted_count = 0
    while current_page<=last_page:
        logging.info('Started scraping page: %s', current_page)
        time.sleep(4)

        # Find the laptop elements
        laptops = driver.find_elements(By.XPATH, "//div[@class='info--ifj7U']")

        # Store the URLs of the laptops
        laptop_urls = [laptop.find_element(By.XPATH, ".//div[@class='title--wFj93']/a").get_attribute('href') for laptop in laptops]
        
        # Click each laptop to access Ratings 
        for laptop_url in laptop_urls:
            title = 'No Data'
            price = 'No Data'
            rating = 'No Data'
            try:

                # Open the laptop URL in a new tab
                driver.execute_script("window.open('" + laptop_url +"');")

                # Switch to the new tab (it's always the last one)
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(5)


                # Scroll down to the rating
                driver.execute_script("window.scrollBy(0, 1600);")
                time.sleep(2)

                # Wait for the rating element to be visible
                rating = WebDriverWait(driver, 45).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='score-average']")))
                rating = rating.text

                try:
                    title = driver.find_element(By.XPATH,".//span[@class='pdp-mod-product-badge-title']").text
                except Exception as e:
                    logging.error(f"Error occurred while fetching title. Error: {e}", exc_info=True)

                try:
                    price = driver.find_element(By.XPATH,".//span[@class=' pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl']").text
                except Exception as e:
                    logging.error(f"Error occurred while fetching price. Error: {e}", exc_info=True)

                 # Insert the data into the laptops table
                sql = "INSERT INTO laptops (title, price, rating) VALUES (%s, %s, %s)"
                val = (title, price, rating)
                mycursor.execute(sql, val)
                mydb.commit()

                 # Increment the counter
                inserted_count += 1
                logging.info(f"Number of inserted laptops: {inserted_count}")

                # Close the tab after scraping
                driver.close()

                 # Switch back to the main page and close the tab
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(5) # Add a short delay before clicking the next laptop

            except TimeoutException:
                logging.error("Timeout occurred. Skipping the current laptop.", exc_info=True)
                # If timeout occurred, insert 'No Data' into the database
                sql = "INSERT INTO laptops (title, price, rating) VALUES (%s, %s, %s)"
                val = ('No Title', 'No Price', 'No Rating')
                mycursor.execute(sql, val)
                mydb.commit()
                # Close the tab after the exception
                driver.close()
                 # Switch back to the main page after closing the tab
                driver.switch_to.window(driver.window_handles[0])

       # mycursor.execute("SELECT * FROM laptops")
       # myresult = mycursor.fetchall()
        #for record in myresult:
         #   logging.info("Record: %s", record)
        current_page += 1

        try:
            next_page = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,".//li[@title='Next Page']")))
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_page)
            time.sleep(2)
            next_page.click()
        except TimeoutException:
            logging.error("Cannot locate or click the 'Next Page' button", exc_info=True)

    # Fetch and print all records from the laptops table
    mycursor.execute("SELECT * FROM laptops")
    myresult = mycursor.fetchall()
    for record in myresult:
        logging.info("Record: %s", record)

    #Close Connection
    mycursor.close()
    mydb.close()
    driver.quit()

    logging.info("Job finished.")
# Scheduling to run script after given interval of time

schedule.every().saturday.at("20:08").do(job)

setup_logger()
while True:
    schedule.run_pending()
    time.sleep(1)
