import csv

import requests


with open('torch_urls.csv') as f:
    for row in csv.DictReader(f):
        url = row['dwca_url']
        #print('checking status:', url)
        try:
            r = requests.head(url, timeout=2)
            #print(r['Content-Length'])
            #print(type(r))
            #print(r.status_code)
            if r.status_code == 200: 
                print(url, ', TRUE')
            else:
                print(url, ', FALSE')

        except TimeoutError:
            print('Timed out for :', url)
            #pass
        except Exception as e:
            print(e)
            #pass
