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

    resp = requests.get("http://api.elsevier.com/content/search/scopus?query=AU-ID(" + author + ")&field=eid",
                        headers={'Accept':'application/json',
                                'X-ELS-APIKey': MY_API_KEY,
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'})

    results = resp.json()
    #print(results)
    
    i = 0
    for r in results['search-results']["entry"]:
    
        print(r)
        sid = [str(r['eid'])]

        print("https://www.scopus.com/onclick/export.uri?oneClickExport=%7b%22Format%22%3a%22BIB%22%2c%22View%22%3a%22CiteOnly%22%7d&origin=recordpage&eid=" + sid[0].replace('SCOPUS_ID:','') + "&zone=exportDropDown&outputType=export&txGid=2588ce2e043ad4d4b6c800a31f634310")
        resp = requests.get("https://www.scopus.com/onclick/export.uri?oneClickExport=%7b%22Format%22%3a%22BIB%22%2c%22View%22%3a%22CiteOnly%22%7d&origin=recordpage&eid=" + sid[0].replace('SCOPUS_ID:','') + "&zone=exportDropDown&outputType=export",
                    headers={'X-ELS-APIKey': MY_API_KEY,
                             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
                             'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                             'sec-ch-ua-mobile': '?0',
                             'sec-fetch-dest': 'document',
                             'sec-fetch-mode': 'navigate',
                             'sec-fetch-site': 'none',
                             'sec-fetch-user': '?1',
                             'upgrade-insecure-requests': '1'})

        #                     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

        #print("http://www.sciencedirect.com/sdfe/arp/cite?pii=" + sid[0].replace('SCOPUS_ID:','') + "&format=text%2Fx-bibtex&withabstract=true")
        print(resp.content)

        # TODO: REMOVE FIRST 3 LINES FROM resp.content

        #bib.add(str(resp.content))
        break
    break

# with open('bib.bib', 'w') as file:
#     for bibitem in bib:
#         file.write(bibitem)
#         file.write('\n')