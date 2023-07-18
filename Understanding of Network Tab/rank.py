import requests
import pandas as pd

url = "https://cricketapi-icc.pulselive.com/icc-ratings/allTimeBestPlayers?playerRatingRole=bat&matchScope=t20i&pageSize=20&dmsPlayerIdRequired=true"

payload = {}
headers = {
  'authority': 'cricketapi-icc.pulselive.com',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'origin': 'https://www.icc-cricket.com',
  'referer': 'https://www.icc-cricket.com/',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

data=response.json()
data=data['content']
print(data)
df = pd.json_normalize(data)
df.to_csv('rannking')