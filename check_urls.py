import csv

import requests

headers_win = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

headers = {
    'User-Agent': 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0'
}

with open('torch_urls.csv') as f:
    for row in csv.DictReader(f):
        url = row['dwca_url'].strip()
        #print('checking status:', url)
        try:
            if url == '':
                print('NO_URL',',FALSE')
            else:
                r = requests.head(url, timeout=2, headers=headers)
                #print(r.status_code)
                if r.status_code == 200: 
                    print(url,',TRUE')
                else:
                    print(url,',FALSE')

        except TimeoutError:
            print('Timed out for :', url)
            #pass
        except Exception as e:
            print(e)
            #pass
