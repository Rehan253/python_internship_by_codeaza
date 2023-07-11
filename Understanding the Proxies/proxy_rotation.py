import requests

with open("valid_proxies.txt",'r') as f:
    proxies = f.read().split('\n')


links = ['http://www.daraz.pk/health-beauty-tools/?spm=a2a0e.home.cate_2.2.35e34076OrVbjl',
         'http://www.daraz.pk/baby-gear/?spm=a2a0e.home.cate_5.5.35e34076OrVbjl',
         'http://www.daraz.pk/smart-watches/?spm=a2a0e.home.cate_7.7.35e34076OrVbjl',
         'http://www.daraz.pk/buy-fresh-produce/?spm=a2a0e.home.cate_1.1.35e34076iNEHYz']
         

counter=0

for link in links:
    try:

        print(f'using the proxy:  {proxies[counter]}')
        res = requests.get(link,proxies={'http':proxies[counter],'https':proxies[counter]},timeout=10)
        print(res.status_code)



    except:
        print('Failed')
        

    finally:
        counter +=1
    