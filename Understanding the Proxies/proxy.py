import requests
proxies={'https':'131.153.48.254:8080'}
r = requests.get('https://httpbin.org/ip',proxies=proxies)
print(r.text)