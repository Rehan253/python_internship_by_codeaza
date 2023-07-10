import requests


url = "https://api.bazaarvoice.com/data/statistics.json?apiversion=5.4&passkey=ormfnaprafumxqk95bptphk6m&stats=Reviews&filter=ContentLocale:en_US&filter=ProductId:b5005316002|3m-country-catalog|fuzeexperience|en_us,b40071210|3m-country-catalog|fuzeexperience|en_us,b40068718|3m-country-catalog|fuzeexperience|en_us,b40074769|3m-country-catalog|fuzeexperience|en_us,b40066585|3m-country-catalog|fuzeexperience|en_us,b40064963|3m-country-catalog|fuzeexperience|en_us,b40065241|3m-country-catalog|fuzeexperience|en_us,b40064945|3m-country-catalog|fuzeexperience|en_us,b40064947|3m-country-catalog|fuzeexperience|en_us,b40071637|3m-country-catalog|fuzeexperience|en_us,b40064821|3m-country-catalog|fuzeexperience|en_us,b40064729|3m-country-catalog|fuzeexperience|en_us,b40065258|3m-country-catalog|fuzeexperience|en_us,b5000000288|3m-country-catalog|fuzeexperience|en_us,b10013803|3m-country-catalog|fuzeexperience|en_us,b40064857|3m-country-catalog|fuzeexperience|en_us,b40071215|3m-country-catalog|fuzeexperience|en_us,b40071644|3m-country-catalog|fuzeexperience|en_us,b40064838|3m-country-catalog|fuzeexperience|en_us,b40071131|3m-country-catalog|fuzeexperience|en_us,b40064752|3m-country-catalog|fuzeexperience|en_us,b40064814|3m-country-catalog|fuzeexperience|en_us,b40064717|3m-country-catalog|fuzeexperience|en_us,b40068741|3m-country-catalog|fuzeexperience|en_us,b40071204|3m-country-catalog|fuzeexperience|en_us,b40064929|3m-country-catalog|fuzeexperience|en_us,b40071849|3m-country-catalog|fuzeexperience|en_us,b40064784|3m-country-catalog|fuzeexperience|en_us,b40068803|3m-country-catalog|fuzeexperience|en_us,b40064765|3m-country-catalog|fuzeexperience|en_us,b40064830|3m-country-catalog|fuzeexperience|en_us,b40064856|3m-country-catalog|fuzeexperience|en_us,b40065240|3m-country-catalog|fuzeexperience|en_us,b40071664|3m-country-catalog|fuzeexperience|en_us,b40064978|3m-country-catalog|fuzeexperience|en_us,b40064793|3m-country-catalog|fuzeexperience|en_us,b40065285|3m-country-catalog|fuzeexperience|en_us,b40064802|3m-country-catalog|fuzeexperience|en_us,b40071943|3m-country-catalog|fuzeexperience|en_us,b5005329008|3m-country-catalog|fuzeexperience|en_us,b5005325102|3m-country-catalog|fuzeexperience|en_us,b5005325013|3m-country-catalog|fuzeexperience|en_us,b5005316000|3m-country-catalog|fuzeexperience|en_us,b5005276004|3m-country-catalog|fuzeexperience|en_us,b5005271016|3m-country-catalog|fuzeexperience|en_us"

payload = {}
headers = {
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.9',
  'Connection': 'keep-alive',
  'Origin': 'https://www.3m.com',
  'Referer': 'https://www.3m.com/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'cross-site',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

response = requests.request("GET", url, headers=headers, data=payload)
data_obj = response.json()
print(data_obj.get('Results')[0])
