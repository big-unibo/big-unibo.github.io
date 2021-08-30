import requests
import json
import browser_cookie3

arr_authors = [
    '55949131000', #EG
    '56344636600', #MF
    '6602888121', #MG
    '7005314544' #SR
    ]
MY_API_KEY = 'afd5bb57359cd0e85670e92a9a282d48'


cj = browser_cookie3.chrome()
r = requests.get('https://www.scopus.com/search/form.uri?display=advanced', cookies=cj)

bib = set()

def get_scopus_info(SCOPUS_ID):
    url = ("http://api.elsevier.com/content/abstract/scopus_id/"
          + SCOPUS_ID
          + "?field=authors,title,publicationName,volume,issueIdentifier,"
          + "prism:pageRange,coverDate,article-number,doi,citedby-count,prism:aggregationType")
    resp = requests.get(url,
                    headers={'Accept':'application/json',
                             'X-ELS-APIKey': MY_API_KEY})

    return json.loads(resp.text.encode('utf-8'))

for author in arr_authors:

    resp = requests.get("https://www.scopus.com/onclick/export.uri?oneClickExport=%7b%22Format%22%3a%22BIB%22%2c%22View%22%3a%22CiteOnly%22%7d&origin=AuthorProfile&zone=resultsListHeader&dataCheckoutTest=false&sort=plf-f&tabSelected=docLi&authorId=" + author,
                        cookies=cj,
                        headers={'authority': 'www.scopus.com',
                                'method': 'GET',
                                'path': '/onclick/export.uri?oneClickExport=%7b%22Format%22%3a%22BIB%22%2c%22View%22%3a%22CiteOnly%22%7d&origin=AuthorProfile&zone=resultsListHeader&dataCheckoutTest=false&sort=plf-f&tabSelected=docLi&authorId=56344636600&txGid=17441bcd80bf1c2eb8245e534261d27b',
                                'scheme': 'https',
                                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
                                'cache-control': 'max-age=0',
                                #'cookie': 'scopus.machineID='+SCOPUS_MACHINEID+'; javaScript=true; screenInfo="1080:1920"; at_check=true; AMCVS_4D6368F454EC41940A4C98A6@AdobeOrg=1; AT_CONTENT_COOKIE="FEATURE_HOMEPAGE_MICRO_UI:1,"; _ga=GA1.2.1317216563.1619781871; __cfruid=6f05cfd4bb5773e468ce735eb26fd648384aa2b1-1627550562; _fbp=fb.1.1630077617865.823449184; SCSessionID='+SCOPUS_SCSESSIONID+'; scopusSessionUUID='+SCOPUS_SESSIONUUID+'; AWSELB=CB9317D502BF07938DE10C841E762B7A33C19AADB12878A07C2164DA9D3C7A80DA22AA4F660926D28B104ABCD9FA6F2F8562BFED44A934D92BA26A54E56FF7F9DDF53B01D731518DB83D486A15C35678199A5870FF; AMCV_4D6368F454EC41940A4C98A6@AdobeOrg=-1124106680|MCIDTS|18870|MCMID|31383621986514351531675387481755470777|MCAAMLH-1630944261|6|MCAAMB-1630944261|RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y|MCOPTOUT-1630346661s|NONE|MCAID|NONE|vVersion|5.2.0|MCCIDH|-1872385915; SCOPUS_JWT=eyJraWQiOiJjYTUwODRlNi03M2Y5LTQ0NTUtOWI3Zi1kMjk1M2VkMmRiYmMiLCJhbGciOiJSUzI1NiJ9.eyJhbmFseXRpY3NfaW5mbyI6eyJhY2Nlc3NUeXBlIjoiYWU6UkVHOlNISUJCT0xFVEg6SU5TVDpTSElCQk9MRVRIIiwidXNlcklkIjoiYWU6MjYxNzQ1NjciLCJhY2NvdW50SWQiOiIzMTM5OCIsImFjY291bnROYW1lIjoiVW5pdmVyc2l0eSBvZiBCb2xvZ25hIn0sInN1YiI6IjI2MTc0NTY3IiwiaW5zdF9hY2N0X25hbWUiOiJVbml2ZXJzaXR5IG9mIEJvbG9nbmEiLCJzdWJzY3JpYmVyIjp0cnVlLCJkZXBhcnRtZW50SWQiOiI0NzU4OCIsImlzcyI6IlNjb3B1cyIsImluc3RfYWNjdF9pZCI6IjMxMzk4IiwiaW5zdF9hc3NvY19tZXRob2QiOiJTSElCQk9MRVRIIiwiZ2l2ZW5fbmFtZSI6IkVucmljbyIsInBhdGhfY2hvaWNlIjpmYWxzZSwiYXVkIjoiU2NvcHVzIiwibmJmIjoxNjMwMzM5NDY4LCJpbmR2X2lkZW50aXR5X21ldGhvZCI6IlNISUJCT0xFVEgiLCJpbnN0X2Fzc29jIjoiSU5TVCIsImluZHZfaWRlbnRpdHkiOiJSRUciLCJuYW1lIjoiRW5yaWNvIEdhbGxpbnVjY2kiLCJleHAiOjE2MzAzNDAzNjgsImF1dGhfdG9rZW4iOiI0ODlkZmRjMjllMzQxMjRiZTM4YTg2ZDdkZjc1OGI0ZGZhMjlneHJxYiIsImlhdCI6MTYzMDMzOTQ2OCwiZmFtaWx5X25hbWUiOiJHYWxsaW51Y2NpIiwiZW1haWwiOiJlbnJpY28uZ2FsbGludWNjaUB1bmliby5pdCJ9.C9sYdkODpLXp71leAhlurLO8noex-WhmA_25J1Y1ZOfTSS69zZSqdLWUKc0Tl4GvQ-gwrYGhMN3nSIGu9cKYlteaosw71VkEWOYh_H_JYdqyJjsWoT8l-UVVThdVf4eh6WrkZHR6lNoqal-udw-h7_iIMzz9fSdHXkA8pArRjv4Zzepd1hoK6qH4jhQgusXwMvPaPRpx9Vo74xOHBPLBqOE0pAmvHIasGyNhpPNKAuXmUwxuOu1h29XVHgytvUop9_Na71I6giOeZQsWrbV4ydkDoSW1epVE-aKLJP7QxVhGOsjkMmPpgoAw18C-y8ojT-wixVHjK5vPexXHrkiBqA; mbox=PC#9c797aeaaef24d5e89c64f660c9f110f.37_0#1693584271|session#0e7a2859538b40669ace360a9d9e43f5#1630341322; s_pers= c19=sc%3Arecord%3Aauthor%20details|1630341271350; v68=1630339469546|1630341271361; v8=1630339493121|1724947493121; v8_s=Less%20than%201%20day|1630341293121;; s_sess= s_cpc=0; e78=title-abs-key%28variety-aware%20olap%20of%20document-oriented%20databases%29; c21=lastname%3Dobaidat%26firstname%3Dmouaht; e13=lastname%3Dobaidat%26firstname%3Dmouaht%3A1; c13=document%20count%20%28high-low%29; s_ppvl=sc%253Asearch%253Aauthor%2520searchform%2C52%2C47%2C969%2C1920%2C969%2C1920%2C1080%2C1%2CP; e41=1; s_cc=true; s_sq=elsevier-sc-prod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dsc%25253Aanalyzer%25253Aanalyze%252520author%252520output%2526link%253D2013%2525202014%2525202015%2525202016%2525202017%2525202018%2525202019%2525202020%2525202021%2525200%25252025%25252050%25252075%2526region%253DanalyzeCitations-chart-mini%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dsc%25253Aanalyzer%25253Aanalyze%252520author%252520output%2526pidt%253D1%2526oid%253Dfunction%252528a%252529%25257Bb.onContainerClick%252528a%252529%25257D%2526oidt%253D2%2526ot%253DDIV; s_ppv=sc%253Arecord%253Aauthor%2520details%2C40%2C35%2C1212%2C1920%2C350%2C1920%2C1080%2C1%2CP;',
                                'referer': 'https://www.scopus.com/authid/detail.uri?authorId=56344636600',
                                'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-fetch-dest': 'document',
                                'sec-fetch-mode': 'navigate',
                                'sec-fetch-site': 'same-origin',
                                'sec-fetch-user': '?1',
                                'upgrade-insecure-requests': '1',
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'})
    
    #print(str(resp.content))
    bibitems = str(resp.content).split('\\n\\n')
    print(bibitems)
    bibitems.pop(0)
    for bibitem in bibitems:
        bib.add(bibitem)

with open('../_biblio/BIG.bib', 'w') as file:
    for bibitem in bib:
        file.write(bibitem.replace('\\n', '\n'))
        file.write('\n')