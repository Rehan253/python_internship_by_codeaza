import requests
import json

url = "https://caching.graphql.imdb.com/?operationName=ChartSidebarTopGenres&variables=%7B%22locale%22%3A%22en-US%22%7D&extensions=%7B%22persistedQuery%22%3A%7B%22sha256Hash%22%3A%220ab5f454289e790a91986d51c38d26db223ec1996bccdeb61e8a1b5c9ce5a3d0%22%2C%22version%22%3A1%7D%7D"

payload = {}
headers = {
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'x-amzn-sessionid': '141-2605993-0686628',
  'x-imdb-weblab-treatment-overrides': '{"IMDB_DESKTOP_SEARCH_ALGORITHM_UPDATES_577300":"T1"}',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'content-type': 'application/json',
  'x-imdb-client-rid': 'J0JS7T03JMBSWSRTRJ4Z',
  'accept': 'application/graphql+json, application/json',
  'x-imdb-client-name': 'imdb-web-next-localized',
  'x-imdb-user-country': 'US',
  'Referer': 'https://www.imdb.com/',
  'x-imdb-user-language': 'en-US',
  'sec-ch-ua-platform': '"Windows"'
}

response = requests.request("GET", url, headers=headers, data=payload)

data=response.json()
data=data['data']['titleMetadata']['titleGenres']
for id in data:
    print(id['genreId'])
