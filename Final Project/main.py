import logging
from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
import mysql.connector
import time
import datetime

# Set up the logger
logging.basicConfig(filename='application.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

def scrape_data(driver, website):
    driver.get(website)
    time.sleep(5)

    symbols_ = [s.text for s in driver.find_elements(By.XPATH, '//a[@class="Fw(b)"]')]
    names_ = [n.text for n in driver.find_elements(By.XPATH, '//td[@class="data-col1 Ta(start) Pstart(10px) Miw(80px)"]')]
    last_price_ = [p.text for p in driver.find_elements(By.XPATH, '//td[@class="data-col2 Ta(end) Pstart(20px)"]')]
    change_ = [c.text for c in driver.find_elements(By.XPATH, "//td[@class='data-col3 Ta(end) Pstart(20px)']//span")]
    per_change_ = [pc.text for pc in driver.find_elements(By.XPATH, '//td[@class="data-col4 Ta(start) Pstart(20px) Pend(6px) W(130px)"]')]

    return symbols_, names_, last_price_, change_, per_change_

def create_database_and_table(db, cursor):
    cursor.execute("CREATE DATABASE IF NOT EXISTS finance_data")
    db.database = 'finance_data'
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS finance_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            symbol VARCHAR(255),
            name VARCHAR(255),
            last_price VARCHAR(255),
            change_in_price VARCHAR(255),
            per_change VARCHAR(255)
        )
    """)

def insert_into_db(cursor, symbols_, names_, last_price_, change_, per_change_):
    for symbol, name, last_price, change, per_change in zip(symbols_, names_, last_price_, change_, per_change_):
        sql = "INSERT INTO finance_data (symbol, name, last_price, change_in_price, per_change) VALUES (%s, %s, %s, %s, %s)"
        val = (symbol, name, last_price, change, per_change)
        try:
            cursor.execute(sql, val)
            logging.info(f'Data for {symbol} inserted successfully.')
        except Exception as e:
            logging.error(f'Error occurred while inserting data for {symbol}: {e}')

def get_all_data(cursor):
    cursor.execute("SELECT * FROM finance_data")
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append({
            'id': row[0],
            'symbol': row[1],
            'name': row[2],
            'last_price': row[3],
            'change_in_price': row[4],
            'per_change': row[5]
        })
    return data

@app.route('/', methods=['GET'])
def go_home():
    return 'Welcome to the Finance Data API!'

@app.route('/fetch-data', methods=['GET'])
def scrape_and_store():
    try:
        website = 'https://finance.yahoo.com/lookup'
        driver = webdriver.Chrome()

        symbols_, names_, last_price_, change_, per_change_ = scrape_data(driver, website)
        driver.quit()

        db = mysql.connector.connect(host="localhost", user="root", password="", database="")
        cursor = db.cursor()

        create_database_and_table(db, cursor)
        insert_into_db(cursor, symbols_, names_, last_price_, change_, per_change_)

        db.commit()
         # Log the time of last data storage
        last_data_store_time = datetime.datetime.now()
        logging.info(f'Data Inserted Successfully at {last_data_store_time}!')
        db.close()

        data = {
            'symbols': symbols_,
            'names': names_,
            'last_price': last_price_,
            'change': change_,
            'per_change': per_change_
        }

        return jsonify(data)
    except Exception as e:
        logging.error(f'Error occurred in scrape_and_store: {e}')
        return jsonify({'error': str(e)})

@app.route('/get-all-data', methods=['GET'])
def fetch_all_data():
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="", database="finance_data")
        cursor = db.cursor()

        data = get_all_data(cursor)
       
        db.close()
        last_request_time = datetime.datetime.now()
        logging.info(f'Data fetched successfully at {last_request_time}.')
        return jsonify(data)
    except Exception as e:
        logging.error(f'Error occurred in fetch_all_data: {e}')
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
