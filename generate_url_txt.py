import csv

import requests


with open('torch_urls.csv') as f:
    for row in csv.DictReader(f):
        if row['in_tx_ok'] =='TRUE':
            if row['dwca_url_active'] == 'TRUE':
                print('Supposedly active:', row['dwca_url'])
            else:
                url = row['dwca_url']
                print('checking status:', url)
                try:
                    r = requests.head(url, timeout=2)
                    #print(r['Content-Length'])
                    print(type(r))
                    print(r.status_code)
                except TimeoutError:
                    print('Timed out for :', url)
                except Exception as e:
                    print(e)
                    pass
