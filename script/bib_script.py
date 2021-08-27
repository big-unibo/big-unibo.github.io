import requests
import json

arr_authors = [
    '55949131000', #EG
    '56344636600', #MF
    '6602888121', #MG
    '7005314544' #SR
    ]
MY_API_KEY = 'afd5bb57359cd0e85670e92a9a282d48'


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
                        headers={'authority': 'www.scopus.com',
                                'method': 'GET',
                                'path': '/onclick/export.uri?oneClickExport=%7b%22Format%22%3a%22BIB%22%2c%22View%22%3a%22CiteOnly%22%7d&origin=AuthorProfile&zone=resultsListHeader&dataCheckoutTest=false&sort=plf-f&tabSelected=docLi&authorId=56344636600&txGid=17441bcd80bf1c2eb8245e534261d27b',
                                'scheme': 'https',
                                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
                                'cache-control': 'max-age=0',
                                'cookie': 'scopus.machineID=A3E0D62AF0ED1AE893E8360F32A7D340.wsnAw8kcdt7IPYLO0V48gA; javaScript=true; screenInfo="1080:1920"; at_check=true; AMCVS_4D6368F454EC41940A4C98A6%40AdobeOrg=1; AT_CONTENT_COOKIE="FEATURE_HOMEPAGE_MICRO_UI:1,"; _ga=GA1.2.1317216563.1619781871; __cfruid=6f05cfd4bb5773e468ce735eb26fd648384aa2b1-1627550562; SCSessionID=512FF0964214049D0AE9821E157AB935.i-0b15cf5290d720477; scopusSessionUUID=91a96ee4-4346-4902-b; AWSELB=CB9317D502BF07938DE10C841E762B7A33C19AADB1930A4F248DC6D388802B26E0DC6A1AA33516DE9F512FAE3569919DB15CED562DBAFDF2ADE925350150D7900CAD0CA8A62B81F8346473EE66139D81350E468E51; AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=-1124106680%7CMCIDTS%7C18867%7CMCMID%7C31383621986514351531675387481755470777%7CMCAAMLH-1630677759%7C6%7CMCAAMB-1630677759%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1630080159s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0%7CMCCIDH%7C-1872385915; SCOPUS_JWT=eyJraWQiOiJjYTUwODRlNi03M2Y5LTQ0NTUtOWI3Zi1kMjk1M2VkMmRiYmMiLCJhbGciOiJSUzI1NiJ9.eyJhbmFseXRpY3NfaW5mbyI6eyJhY2Nlc3NUeXBlIjoiYWU6UkVHOlNISUJCT0xFVEg6SU5TVDpTSElCQk9MRVRIIiwidXNlcklkIjoiYWU6MjYxNzQ1NjciLCJhY2NvdW50SWQiOiIzMTM5OCIsImFjY291bnROYW1lIjoiVW5pdmVyc2l0eSBvZiBCb2xvZ25hIn0sInN1YiI6IjI2MTc0NTY3IiwiaW5zdF9hY2N0X25hbWUiOiJVbml2ZXJzaXR5IG9mIEJvbG9nbmEiLCJzdWJzY3JpYmVyIjp0cnVlLCJkZXBhcnRtZW50SWQiOiI0NzU4OCIsImlzcyI6IlNjb3B1cyIsImluc3RfYWNjdF9pZCI6IjMxMzk4IiwiaW5zdF9hc3NvY19tZXRob2QiOiJTSElCQk9MRVRIIiwiZ2l2ZW5fbmFtZSI6IkVucmljbyIsInBhdGhfY2hvaWNlIjpmYWxzZSwiYXVkIjoiU2NvcHVzIiwibmJmIjoxNjMwMDc3MjQ5LCJpbmR2X2lkZW50aXR5X21ldGhvZCI6IiIsImluc3RfYXNzb2MiOiJJTlNUIiwiaW5kdl9pZGVudGl0eSI6IlJFRyIsIm5hbWUiOiJFbnJpY28gR2FsbGludWNjaSIsImV4cCI6MTYzMDA3ODE0OSwiYXV0aF90b2tlbiI6ImM0MDIyM2E4MzE0YjAwNGQ0OTRhYWU4MWY3ZDhmMzE3YjJkYWd4cnFiIiwiaWF0IjoxNjMwMDc3MjQ5LCJmYW1pbHlfbmFtZSI6IkdhbGxpbnVjY2kiLCJlbWFpbCI6ImVucmljby5nYWxsaW51Y2NpQHVuaWJvLml0In0.FkJk3wFsfTUu3W-EjHl39fgEj-fYdItQOUaeKz5yFhMby_21ujXObjM92iy_orDeT16I0jcrJBT1c_RPwVzu6mIMlNNu_Bb_gXr1eu5-de-lxe0xFQi3xJPLfdTBa1hYhOyFDYBOwlQuQlMeFf3d0Z5b01r1FPNHUbqKCU9vAZN9KnVi0iV20DJLJIIIHvjzVsFJ5T1S83Q_MILuXmh0u9a_8K3a1CU5iF6KmBdL2itdpV4D3CCW8B4oR4jQ-f1XevjbAapc1gELk9wOfkGYHCpETdlpUvV-bdn8KZ0xjtlfVPZbjzjfV7mB0aNsOb4nhu_D2NUPl6FbMKPZSfoZgg; _gid=GA1.2.1115304492.1630077618; _fbp=fb.1.1630077617865.823449184; mbox=PC#9c797aeaaef24d5e89c64f660c9f110f.37_0#1693322802|session#7148538b9475420593959597fa206941#1630079861; s_sess=%20s_cpc%3D0%3B%20e78%3Dtitle-abs-key%2528variety-aware%2520olap%2520of%2520document-oriented%2520databases%2529%3B%20c21%3Dcite%253D2-s2.0-85082444588%3B%20e13%3Dcite%253D2-s2.0-85082444588%253A1%3B%20c13%3Ddate%2520%2528newest%2529%3B%20s_ppvl%3Dsc%25253Arecord%25253Aauthor%252520details%252C95%252C33%252C2769%252C1920%252C969%252C1920%252C1080%252C1%252CP%3B%20s_ppv%3Dsc%25253Arecord%25253Adocument%252520record%252C77%252C77%252C912%252C1920%252C581%252C1920%252C1080%252C1%252CP%3B%20e41%3D1%3B%20s_cc%3Dtrue%3B%20s_sq%3Delsevier-sc-prod%253D%252526c.%252526a.%252526activitymap.%252526page%25253Dsc%2525253Aanalyzer%2525253Aanalyze%25252520author%25252520output%252526link%25253D2013%252525202014%252525202015%252525202016%252525202017%252525202018%252525202019%252525202020%252525202021%252525200%2525252025%2525252050%2525252075%252526region%25253DanalyzeCitations-chart-mini%252526pageIDType%25253D1%252526.activitymap%252526.a%252526.c%252526pid%25253Dsc%2525253Aanalyzer%2525253Aanalyze%25252520author%25252520output%252526pidt%25253D1%252526oid%25253Dfunction%25252528a%25252529%2525257Bb.onContainerClick%25252528a%25252529%2525257D%252526oidt%25253D2%252526ot%25253DDIV%3B; s_pers=%20c19%3Dsc%253Arecord%253Aauthor%2520details%7C1630079802070%3B%20v68%3D1630078000458%7C1630079802081%3B%20v8%3D1630078026669%7C1724686026669%3B%20v8_s%3DLess%2520than%25201%2520day%7C1630079826669%3B',
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

with open('bib.bib', 'w') as file:
    for bibitem in bib:
        file.write(bibitem.replace('\\n', '\n'))
        file.write('\n')