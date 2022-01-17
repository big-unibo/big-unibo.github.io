import requests
import json
import textwrap3
import sys

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

    resp = requests.get("http://api.elsevier.com/content/search/scopus?query=AU-ID(" + author + ")&field=dc:identifier",
                        headers={'Accept':'application/json',
                                'X-ELS-APIKey': MY_API_KEY})

    results = resp.json()
    #print(results)
    
    i = 0
    for r in results['search-results']["entry"]:
    
        sid = [str(r['dc:identifier'])]
        # some entries seem to have json parse errors, so we catch those
        
        bibitem = get_scopus_info(sid[0])  # index 0 because the input data is a 2d array

        bib.add(json.dumps(bibitem))

        break

        """ if results['abstracts-retrieval-response']['coredata']['prism:aggregationType'] == 'Journal':
            i += 1
            fstring = '{authors}, {title}, {journal}, {volume}, {articlenum}, ({date}). <a href="https://doi.org/{doi}">{doi}</a> (cited {cites} times)\n\n'

            s = fstring.format(authors=', '.join([au['ce:indexed-name'].encode('utf-8') for au in results['abstracts-retrieval-response']['authors']['author']]),
                            title=results['abstracts-retrieval-response']['coredata']['dc:title'].encode('utf-8'),
                            journal=results['abstracts-retrieval-response']['coredata']['prism:publicationName'].encode('utf-8'),
                            volume=results['abstracts-retrieval-response']['coredata'].get('prism:volume', 'None').encode('utf-8'),
                            articlenum=str((results['abstracts-retrieval-response']['coredata'].get('prism:pageRange') or
                                        results['abstracts-retrieval-response']['coredata'].get('article-number'))).encode('utf-8'),
                            date=results['abstracts-retrieval-response']['coredata']['prism:coverDate'].encode('utf-8'),
                            doi='doi:' + results['abstracts-retrieval-response']['coredata']['prism:doi'].encode('utf-8'),
                            cites=int(results['abstracts-retrieval-response']['coredata']['citedby-count'].encode('utf-8')))
            print ('{0:3d}. {1}<br>'.format(i, s))
    
        print ('{0:3d}. {1}'.format(i, sid)) """

with open('bib.bib', 'w') as file:
    file.write(str(bib))