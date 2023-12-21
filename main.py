import requests
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com/all/views/all/"

crypto_dct = {}

response = requests.get(url)
soup = BeautifulSoup(response.text , features="lxml")

cryptos = soup.find_all("a" , class_="cmc-table__column-name--name cmc-link")
crypto_Market = soup.find_all("span" , class_="sc-7bc56c81-1 bCdPBp")
crypto_price = soup.find_all("div" , class_ = "sc-a0353bbc-0 gDrtaY")
   


if len(cryptos) == len(crypto_Market) == len(crypto_price):
    
    crypto_dict = dict(
        zip(
            [crypto.text.strip() for crypto in cryptos],
            [
                {"Market": market.text.strip(), "Price": price.text.strip()}
                for market, price in zip(crypto_Market, crypto_price)
            ],
        )
    )

   
    for key, value in crypto_dict.items():
        print(f'{key}: {value}')
else:
    print("error")