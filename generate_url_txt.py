import csv

import requests


with open('torch_urls.csv') as f:
    for row in csv.DictReader(f):
        if row['in_tx_ok'] =='TRUE':
            if row['dwca_url_active'] == 'TRUE':
                url = row['dwca_url']
                print(url)
            elif row['ipt_url']:
                url = row['ipt_url']
                print(url)


