import requests
from bs4 import BeautifulSoup

# Web Scrapping

def get_exchange_rate(target1, target2):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }
    # response = requests.get("https://kr.investing.com/currencies/{}-{}".format(target1, target2), headers=headers)
    response = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From={}&To={}".format(target1, target2), headers=headers)

    content = BeautifulSoup(response.content, 'html.parser')

    # containers = content.find('div', {'data-test': "instrument-price-last"})
    containers = content.find('p', {'bnLtQr'})

    print(f'1 {target1}: {containers.text}')

get_exchange_rate('USD', 'CAD')