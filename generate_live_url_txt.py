import csv

import requests


with open('torch_urls.csv') as f:
    for row in csv.DictReader(f):
        if row['in_tx_ok'] =='TRUE':
            if row['dwca_url_active'] == 'FALSE':
                if row['dwca_live_url_active'] =='TRUE':
                    url = row['dwca_live_url']
                    print(url)


