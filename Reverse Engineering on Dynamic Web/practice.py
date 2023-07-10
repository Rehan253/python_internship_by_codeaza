import requests
from bs4 import BeautifulSoup

url = 'https://www.3m.com/3M/en_US/p/c/abrasives/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all('p', class_='mds-link_product')

for title in titles:
    print(title.text)