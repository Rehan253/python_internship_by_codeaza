
# Final Project of Python Internships

This is a Flask-based API that scrapes finance data from Yahoo Finance and stores it in a MySQL database. The API provides endpoints to fetch the scraped data and retrieve all data from the database.


## Requirements
To run this API, you need the following software installed:

### 1 Python
### 2 Flask 
### 3 Selenium 
### 4 MySQL Connector/Python 
### 5 Google Chrome

## Installation
Install the required Python packages using pip.

#### pip install -r requirements.txt

The requirements.txt file contains a list of required Python packages along with their versions.


## Usage

Start the API server by running the following command:

#### python app.py

The API will be accessible at http://localhost:5000/
## Endpoints

### GET /
This endpoint returns a welcome message indicating that you've reached the Finance Data API.

### GET /fetch-data
This endpoint triggers the scraping of finance data from Yahoo Finance, stores it in the MySQL database, and returns the scraped data in JSON format.

### GET /get-all-data
This endpoint fetches all the data stored in the MySQL database and returns it in JSON format.



## Logging

The API logs relevant events in the application.log file. The log file captures the timestamp, log level, and corresponding messages
## Work Flow

With the implementation of this API, you can now easily scrape finance data from Yahoo Finance, store it in a MySQL database, and retrieve it through API endpoints. The API provides a convenient and efficient way to access financial information for various symbols and companies.

To test the API, you can access the following endpoints:

GET /: This endpoint will return a welcome message indicating that you've reached the Finance Data API.

GET /fetch-data: Triggering this endpoint will initiate the scraping of finance data from Yahoo Finance, and the scraped data will be stored in the MySQL database. The API will respond with the scraped data in JSON format.

GET /get-all-data: Accessing this endpoint will retrieve all the data stored in the MySQL database and return it in JSON format.

You can also explore the log file application.log to monitor the events and activities of the API, which includes any errors or successful data insertions.

With this API in place, you can now easily access finance data, perform analyses, and build applications based on the retrieved information. It serves as a foundation for various financial data-driven projects and opens up possibilities for further enhancements and features
## Conclusion

In conclusion, the Finance Data API demonstrates the integration of web scraping, data storage using MySQL, and serving data through RESTful API endpoints with Flask. By following the installation and setup instructions, you can quickly deploy the API locally and begin fetching financial data for analysis and visualization