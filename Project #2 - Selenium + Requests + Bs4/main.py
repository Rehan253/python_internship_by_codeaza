import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd
url = "https://www.facebook.com/api/graphql/"


def diff_characters_and_index(string1, string2):
    min_length = min(len(string1), len(string2))

    for i in range(min_length):
        if string1[i] != string2[i]:
            return i, string1[i], string2[i]

    if len(string1) != len(string2):
        return min_length, string1[min_length:], string2[min_length:]

    return None


### second api call
payload2 = 'av=100088881459539&__user=100088881459539&__a=1&__req=i&__hs=19556.HYP%3Acomet_pkg.2.1..2.1&dpr=2&__ccg=MODERATE&__rev=1007858379&__s=syco9l%3Aiqude6%3A3ghkq7&__hsi=7257262229750389383&__dyn=7AzHK4HzEmwIxt0mUyEqxenFwLBwopU98nwgUao4u5QdwSxucyUco5S3O2Saw8i2S1DwUx60DUG0Z82_CxS320om78bbwto88422y11xmfz81s8hwGxu782lwv89kbxS2218wc61axe3S7Udo5qfK0zEkxe2GewyDwkUtxGm2SUbElxm3y3aexfxmu3W3y261eBx_y88E3qxWm2Sq2-azo7u3C223908O3216xi4UdUcojxK2B0oobo8oC1Hg6C&__csr=gmR6mwDb4sL5jht5uziOOEjEIAiJjqF8ABFPlq6jH8D48hiiXjq8i8AlFeBjRiT9GBqTN19qpirGIHCxeiHRfh4iaiu2C9hkKi9Ay6q4GJ2oWqFAmu4Au4VFVoWicKQt6J5GKh28CqbABgsGWBx24HwLxjADx24VdAwUwAyE8oK3G25oSm6ovyk6EtybghwwzUcpAbBxmmq4U88Wi6oWUcElwlEjwSwCxifKbzUao-262OewjF8fqwPxy4ouwoUowQxe1lxq3y7EyE5W06OFU03B_w0Xbwam0qq063odAcwo9o16o1c829U0BW1HBw1AKOo6x01bqu04b8hxfw19C2Aw14k0cOgjxm1Nw4rK0iS1dx4h9wi406LpUbiBx-0foAo9U720dvxWu1Gw5dg1EE5K9w8m0ji0cIwn40uym&__comet_req=15&fb_dtsg=NAcPiiCT57FLhrKtxJQqQ7P8oHL__fqR03Rhutgms7KlEsucFztRAsA%3A36%3A1689670733&jazoest=25621&lsd=h9Ns0PlpunNlgS8skJe8Kw&__spin_r=1007858379&__spin_b=trunk&__spin_t=1689713036&qpl_active_flow_ids=431626709&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=GroupsCometMembersPageNewMembersSectionRefetchQuery&variables=%7B%22count%22%3A10%2C%22cursor%22%3A%22AQHRSXIZzAXkCBxLWbVQ16IyXGlVIAJnmpgUnIN-Q73d4wifiF2Jt6OZlUJFzeuRw8VS%22%2C%22groupID%22%3A%221892957960867332%22%2C%22recruitingGroupFilterNonCompliant%22%3Afalse%2C%22scale%22%3A2%2C%22id%22%3A%221892957960867332%22%7D&server_timestamps=true&doc_id=7396994073660826'
headers2 = {
  'authority': 'www.facebook.com',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/x-www-form-urlencoded',
  'cookie': 'sb=jOhOY1646pKYFYbE1xNrp2RZ; datr=jOhOY2f0p4cX_VC-p0GNUB0h; c_user=100088881459539; dpr=1.5625; xs=36%3ArCguTi_s5WkUxg%3A2%3A1689670733%3A-1%3A-1%3A%3AAcXEuEDYOTezTkT5y1KLaBRGTWUVjBjrLgUj0zkEng; fr=0nej4IBlbGVxVOnf9.AWVKo7jRCd5HP5BBDPNwV9wZnUI.BktujM.Ws.AAA.0.0.BktujM.AWUESvujkhY; wd=1229x267; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1689713050484%2C%22v%22%3A1%7D',
  'origin': 'https://www.facebook.com',
  'referer': 'https://www.facebook.com/groups/1892957960867332/members',
  'sec-ch-prefers-color-scheme': 'light',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-full-version-list': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.199", "Google Chrome";v="114.0.5735.199"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-ch-ua-platform-version': '"10.0.0"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'viewport-width': '1229',
  'x-asbd-id': '129477',
  'x-fb-friendly-name': 'GroupsCometMembersPageNewMembersSectionRefetchQuery',
  'x-fb-lsd': 'h9Ns0PlpunNlgS8skJe8Kw'
}



payload = 'av=100088881459539&__user=100088881459539&__a=1&__req=i&__hs=19556.HYP%3Acomet_pkg.2.1..2.1&dpr=2&__ccg=MODERATE&__rev=1007858379&__s=ymo9jw%3Aiqude6%3A951dzp&s=ymo9jw%3Aiqude6%3A951dzp&__hsi=7257251677962596601&__dyn=7AzHK4HzEmwIxt0mUyEqxenFwLBwopU98nwgUao4u5QdwSxucyUco5S3O2Saw8i2S1DwUx60DUG0Z82_CxS320om78bbwto88422y11xmfz81s8hwGxu782lwv89kbxS2218wc61axe3S7Udo5qfK0zEkxe2GewyDwkUtxGm2SUbElxm3y3aexfxmu3W3y261eBx_y88E3qxWm2Sq2-azo7u3C223908O3216xi4UdUcojxK2B0oobo8oC1hxB0qo&__csr=gmR6mwDb4sL5jht5thAIG5PihaRdGAyimDdcwFkysj4kAKQSy4y95qjFkZkJOqFmJYgimCkCWHaVESmiHRfh4iaiu74byklbAyp8xCxaHgCeCGp5Dx97xequmeAzbJ7hHhqHAgy9CyV9k7aKFogxaUbUkV9Ugxejp8e898G26bwWwxmdBxC7UB1G7oyQ4o88-36p2VolBCxe22eAxCeK3a5o5q4UdE9EkzXyU-2CfwxwIzE4Wi3SEcUox67E6e68d8jwlomwUxW8G1uw1IGu00VvU0eOU2Bw6Cw1wS3p3862m0hC0j20yu09uwqVo0pbIC1Eg0iSDw12O4ojU0ipwF80h503cA4Ulwso16Xw4Jwjoh4io4x01HSu2QFovw3S962u1Mw3nUuDwqE1jk0qa1ryo25w4Qw3b85N07EBw&__comet_req=15&fb_dtsg=NAcOAUhdnAzNUROyv59FpL0H65KcbQxSSD26CNkQO1-u-ie13zkrOEg%3A36%3A1689670733&jazoest=25260&lsd=LkWWvLzB2Zhmovzr7wcklQ&__spin_r=1007858379&__spin_b=trunk&__spin_t=1689710579&qpl_active_flow_ids=431626709&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=GroupsCometMembersPageNewMembersSectionRefetchQuery&variables=%7B%22count%22%3A10%2C%22cursor%22%3A%22AQHRmeqMnFoy25eGlfxLM19X8tAo8ZNOx7EDl9LL3beyMz79MOoeOQZ4KuBLc107AD4PZMd77tDxKjtRmO2pTrqR8Q%22%2C%22groupID%22%3A%221892957960867332%22%2C%22recruitingGroupFilterNonCompliant%22%3Afalse%2C%22scale%22%3A2%2C%22id%22%3A%221892957960867332%22%7D&server_timestamps=true&doc_id=7396994073660826'
headers = {
  'authority': 'www.facebook.com',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/x-www-form-urlencoded',
  'cookie': 'sb=jOhOY1646pKYFYbE1xNrp2RZ; datr=jOhOY2f0p4cX_VC-p0GNUB0h; c_user=100088881459539; dpr=1.5625; xs=36%3ArCguTi_s5WkUxg%3A2%3A1689670733%3A-1%3A-1%3A%3AAcXEuEDYOTezTkT5y1KLaBRGTWUVjBjrLgUj0zkEng; fr=0nej4IBlbGVxVOnf9.AWVKo7jRCd5HP5BBDPNwV9wZnUI.BktujM.Ws.AAA.0.0.BktujM.AWUESvujkhY; wd=1229x267; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1689710594920%2C%22v%22%3A1%7D',
  'origin': 'https://www.facebook.com',
  'referer': 'https://www.facebook.com/groups/1892957960867332/members',
  'sec-ch-prefers-color-scheme': 'light',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-full-version-list': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.199", "Google Chrome";v="114.0.5735.199"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-ch-ua-platform-version': '"10.0.0"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'viewport-width': '1229',
  'x-asbd-id': '129477',
  'x-fb-friendly-name': 'GroupsCometMembersPageNewMembersSectionRefetchQuery',
  'x-fb-lsd': 'LkWWvLzB2Zhmovzr7wcklQ'
}


# Lists to store the attributes
list_urls=[]
pay_load_list=[payload2,payload]
profile_img_src=[]
bio=[]
joined=[]
name=[]



# call API through request to get data in Json format
response = requests.request("POST", url, headers=headers, data=payload)   
data = response.json()

for i in range(10):


        list_urls.append(data.get('data').get('node').get('new_members').get('edges')[i].get('node').get('url'))
        name.append((data.get('data').get('node').get('new_members').get('edges')[i].get('node').get('name')))
        profile_img_src.append(data.get('data').get('node').get('new_members').get('edges')[i].get('node').get('profile_picture').get('uri'))
        try:
            bio.append(data.get('data').get('node').get('new_members').get('edges')[i].get('node').get('bio_text').get('text'))
        except:
             bio.append('NA')
        joined.append(data.get('data').get('node').get('new_members').get('edges')[i].get('join_status_text').get('text'))





list_urls2=[]




response = requests.request("POST", url, headers=headers, data=payload2) 
data = response.json()


for i in range(10):


        list_urls.append(data.get('data').get('node').get('new_members').get('edges')[i].get('node').get('url'))
        name.append((data.get('data').get('node').get('new_members').get('edges')[i].get('node').get('name')))
        profile_img_src.append(data.get('data').get('node').get('new_members').get('edges')[i].get('node').get('profile_picture').get('uri'))
        try:
            bio.append(data.get('data').get('node').get('new_members').get('edges')[i].get('node').get('bio_text').get('text'))
        except:
             bio.append('NA')
        joined.append(data.get('data').get('node').get('new_members').get('edges')[i].get('join_status_text').get('text'))




# combine the urls of profile of two api calls
final_list= list_urls+list_urls2

print(len(final_list))
print(len(set(final_list)))

df_dict= {'Name':name,'Profile Image':profile_img_src,'Joined':joined,'Profile URL':final_list,'Bio Text':bio}

# Save dat to excel file
df=pd.DataFrame(df_dict)
df.to_excel('data.xlsx')



