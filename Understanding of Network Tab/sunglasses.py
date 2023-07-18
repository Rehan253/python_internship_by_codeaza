import requests
import pandas as pd
page_no=1


result=[]
for page_no in range(24):

    url = f"https://www.sunglasshut.com/wcs/resources/plp/10152/byCategoryId/3074457345626651857?isProductNeeded=true&isChanelCategory=false&pageSize=18&responseFormat=json&currency=USD&catalogId=20602&top=Y&beginIndex=0&viewTaskName=CategoryDisplayView&storeId=10152&langId=-1&categoryId=3074457345626651857&pageView=image&orderBy=default&currentPage={page_no}"

    payload = {}
    headers = {
    'authority': 'www.sunglasshut.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'aka-cc=PK; aka-ct=LAHORE; aka-zp=; bm_sz=22F4192378D9F2268CAFC81B8412DE78~YAAQVR0gF89OjF6JAQAAOjq2ZRSQVs6Ot/92/yLAegBAtwbGutMLMWS6Jzjgduq0Sjjt5VaYVmZNPgJ7rTEmEkntr5QSpaCZUrhiNbp2f8+CjJfXP/ksj+cBBQFZ63/1+L8EjIpFdoiat0pLIgSwON/v8+UhRSGL8Hpis9K0ohmn7Unl3kiIaWW8w/CHlPyPcLxplCtTErk97XD9sbFKqE1TjcVPs2CzGQP1NtCWEHN71Lf+746n5ZHYsR0bqsdJurIEajWE0jdFdL38gIg8+Mw1Ky2bupgQldDa2QnD2cPilDZ51ff84A==~3227971~3684408; dtCookie=v_4_srv_-2D82_sn_42U942R40IJQV9PU6OOOMHE8VOAUH1F9; rxVisitor=1689628596118P62AH56C7T69RL9S0Q0QMC4G152N620J; sgh-desktop-facet-state-search=; ak_bmsc=A77233042041FE565D2EE7BEB07F3782~000000000000000000000000000000~YAAQVR0gF+xPjF6JAQAA6Ee2ZRQBDgzcSmknqNN0G/wQIbdKUdw03nG39Qpl11aq2at0DJ8lYopwIgwrPBGdl2XswYlYkew3ROzLrydhU+IXr6olr44Br1YsR7Z+EuzwPxLFo6WlqyZaWU6oiblfO4/VaPTX1EXZabLGsIm6ngx4w//P3P7ygVhdxXOUlDjgz1aEoVBn1seSzs8nYCpPpme0eW73yogM9VPwpajImq80oBHDlmPfjBJXr1LKrzBwH0Go6d5hbKG3smop40GgjvZWsUrYl6GPws6VZropCLXO+2OD/jPQne9IpmS9fxIUv2f6Gj4KnHaH2bj6cRiZoQ4yebFth9lkck043U1OrggFb05ImcErmmyuXx2g8ZHDyj6oLsAgIBr9QiY2QfhpNkSjXtmDdpvE8mXm8ZxFSwgz96oUuWUmV7dVmeprySyZhHhsUFXil36gLBxnUZDVbcf5KPDVG/tF3XWgeg1xXCH0jZyz5+AopMVO8XgJfFJ4Jw==; JSESSIONID=0000dJiIlyaIRlAi3ZJu-myjX51:1c80pfc7n; TS011f624f=015966d29271bd6508e0843ec9ff43703067b3df8ea69dc0aa2fdc6df627dd2f7c0f3f0851f150000add949ec5eed62c1b58a491f689de0bffc253a0b6abeeb09b95284d02; ftr_ncd=6; mt.v=2.1936356273.1689628600190; tealium_data2track_Tags_AdobeAnalytics_TrafficSourceMid_ThisHit=direct; tealium_data_tags_adobeAnalytics_trafficSourceMid_thisSession=direct; tealium_data_session_timeStamp=1689628600293; userToken=undefined; TrafficSource_Override=1; tiktok_click_id=undefined; __wid=789631983; ftr_blst_1h=1689628600365; AMCVS_125138B3527845350A490D4C%40AdobeOrg=1; s_ecid=MCMID%7C21276722865286281310065849699630413526; AMCV_125138B3527845350A490D4C%40AdobeOrg=-1303530583%7CMCIDTS%7C19556%7CMCMID%7C21276722865286281310065849699630413526%7CMCAAMLH-1690233402%7C3%7CMCAAMB-1690233402%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1689635802s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.3.0; s_cc=true; _cs_mk_aa=0.19223394425322016_1689628604136; _abck=BD9C572B5E0CDF8A53BA4A9F1DA8E290~0~YAAQVR0gF0xSjF6JAQAAbWS2ZQrjzjZ1fnm5WHlX22mboLKuY3qn2T3K/gh9ie4WWTMx16LnVeg3T6rfNt14AUqyjEN5Bp7J9JWQFoeVge7WubYgjNpFdnKdiJj2t68w/4lL1oktwO8AfxVXxoIptBpVjzFpDtBoxhY7ESr23gk0TAi0ETJQ1FwQhpesN3tW4mMvhwebo0lHC6XhWAI5me1PX4We2CyMuVibIsPbh5Db8DXLfq7yDyb7fmTHLfM5p8zd7UPP7CFshkOVmKNrzmdCeSu4xwf+LJxyWgxySHFWPAFNIT84R8eS543j/vFNHk0thqUidDtvWMOmL7eOSX8EHNhcZ7yikSyw2d21fbvgtzT38pbZL2IthIvP3jsPEfEQdSP3WyjGpXOfdZ+VSO+Lj1zb0gqFM5jm7SU=~-1~||-1||~-1; _cs_c=1; _gcl_au=1.1.729862292.1689628609; SGPF=3eunxIg5olCTTmHGMo4Eb5R3iw-SJSn2iU538WR5l_pANonpNeFBHKQ; _ga=GA1.1.2056979604.1689628611; _scid=0177b8d6-40eb-4525-b418-a6f8bcc1893d; _fbp=fb.1.1689628613297.1957895675; _pin_unauth=dWlkPU5ESTFOR0UwTnpBdFpXTTRNUzAwWlRabExXSmxNRGd0TldZelptRTBOV0ZtTVRkaQ; smc_uid=1689628613865568; smc_tag=eyJpZCI6Njc4LCJuYW1lIjoic3VuZ2xhc3NodXQuY29tIn0=; smc_session_id=KUS5Bu3ST1xO1pWSDevRHNy9aod5IsNd; _tt_enable_cookie=1; _ttp=UeRUR-gFGXbdGEAUoRfTuR5mPA7; smc_refresh=24860; smc_sesn=1; smc_not=default; outbrain_cid_fetch=true; tfpsi=d1bd5085-363d-49b5-92c3-04f95ef5a0ba; _sctr=1%7C1689620400000; CONSENTMGR=consent:true%7Cts:1689628625545; dtLatC=13; dtSa=-; sgh-desktop-facet-state-plp=categoryid:undefined|gender:true|brands:partial|polarized:true|price:true|frame-shape:partial|color:true|face-shape:false|fit:false|materials:false|lens-treatment:false; tealium_data2track_Tags_AdobeAnalytics_TrafficSourceJid_ThisHit=307172REF; tealium_data_tags_adobeAnalytics_trafficSourceJid_stackingInSession=307171DIR-307172REF; forterToken=bb86f94559bd4acd93acfa6a4e88a6da_1689628628973__UDF43-m4_6; _cs_id=1bdb5871-8442-a04e-b764-f1f399c5c392.1689628608.1.1689628633.1689628608.1.1723792608677; _cs_s=2.0.0.1689630433904; _derived_epik=dj0yJnU9QlVPUjNVR20tWmZ5OHVRbG9wLXlTelZoTUJfTmZtb1Embj1VMU56b28tOGE1Vm1qTlRnVVlFcXpBJm09MSZ0PUFBQUFBR1MxcjlVJnJtPTEmcnQ9QUFBQUFHUzFyOVUmc3A9Mg; UserTrackingProducts=0; _scid_r=0177b8d6-40eb-4525-b418-a6f8bcc1893d; _uetsid=400ed6a024e711ee81cc6dbb99fc91c5; _uetvid=400f4ba024e711eeb0d54532803ab787; cto_bundle=6rBpp19JdlhoZnBmUDk5aVh2M0dSWjd6WFNDbWNHWXVlUE9zZElrVEd0U3ptdWxpMGxqaSUyQkVIVmdBRmNHTEY5RVROeWxWaGhBZlNNRFQ3ZkJPOVM1YVBWa0VPUWprRDlTUEJGRUVxMUNiNThWdjZUTFklMkZ1UWpSN3RrSG9QUElCV3BTQWFUU1VwVDFoUmx3RUl1bzhnbTlNc0ZBJTNEJTNE; smc_tpv=3; smc_spv=3; dtPC=-82^$28628874_730h-vMAATRUACDKQEPJAPKAAFCKMDOHTPAOKC-0e0; bm_sv=8262DA067E4FB1549CC623373BA2614A~YAAQVR0gF9NgjF6JAQAA9hq3ZRQWZELW5nn0Al7ZskDhD6FNDTEAY3r3O0pZ16IrDQH+GcLQNeqK9ROKMN6Domq5ja+2qAUV4jXG8Pq23jum7q7Gks7hG3KWneXUjn5nTViRiyi8zw2sEdpzyY9/DvpjEGsjrC+OcKAJTo4PF50IgNThb+gGdOycD0Qo1lypwlt0QZGUI6l4ivXR7+7kAurZLo1d2voXBbw4SvT267VBnY5Uk9/oNJw7YgdMGOC9ZjwbyV0=~1; rxvt=1689630489081|1689628596120; _ga_6P80B86QTY=GS1.1.1689628611.1.1.1689628696.60.0.0; smct_session={"s":1689628614906,"l":1689628705526,"lt":1689628705527,"t":55,"p":42}; utag_main=v_id:018965b667cb004deb029bf726340506f001c06700978^$_n:1^$_e:9^$_s:0^$_t:1689630505835^$ses_id:1689628600268%3Bexp-session^$_n:2%3Bexp-session^$vapi_domain:sunglasshut.com^$dc_visit:1^$dc_event:2%3Bexp-session^$dc_region:ap-east-1%3Bexp-session; tealium_data_action_lastAction=Brands:Rayban:Plp click [sgh-load-more  button][Loadmoresunglasses]; tealium_data_action_lastEvent=click [sgh-load-more  button][Loadmoresunglasses]; s_sq=%5B%5BB%5D%5D; _abck=BD9C572B5E0CDF8A53BA4A9F1DA8E290~-1~YAAQZR0gFyZxElSJAQAABiPQZQqeqE48/ICCScJT7jiYSX/LS4L0nSD5OUXIrZnKn5GGIC84PG12IJJrxP6KoCa6KFg/6kPioKYP1E00pX7SM2xlzLXjmaL7u0zHcJG6+wiRp2iYC97dyyEgwNGtBEJC43bmX19/3LkR6CXfaf33zD7bTRgKiJLrWr/9cXifXa6iAEWwvKoubjB729sJgKpQqJDJlaYNEBZTOcappFzASAHxUWMIXT211fdMtVR1M7n3cEePyorxtuenP+lwshfbQU2l/tw0wP7Pd+5U/jZCl7YODFc9ISB/ft1g/Gc4mOgqxPAJ0FD6tl4pBtyeV3jwFr3yHKcCtsmLsrWv5C+kaeoWEc+byHi0D9JcPln+FAlbjAcphCk9/qCqIGfUNqAfSudOvUjJvWF+fp8=~0~-1~-1; bm_sv=8262DA067E4FB1549CC623373BA2614A~YAAQZR0gFydxElSJAQAABiPQZRT9p5cCrXc2S+xMYPfo9Ctn0jZ9ZEtkA2MHFoUMrVVmF4GT8B+UpioUAf5ZmGAkhzL35oNnZvNFGbS6bNl17rXqqPuxWjKNVwvDaoZAo0oW5UaNldxrroNYlwi1h8XPi8W9XidN4pPcv32CyuF+wT3FIGOZxIC1EeQ5N2TLp5UgxwyLKdDnzgN8CAg4xwnwKFt0bryvgipSFnQgRIiRzF0Iyjir8D+JR5djQ7TxgdJYd+8=~1; aka-zp=',
    'referer': 'https://www.sunglasshut.com/us/ray-ban',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data =response.json()
    for p in data['plpView']['products']['products']['product']:
        result.append(p)

df = pd.json_normalize(result)
df.to_csv('data.csv')