import requests
from bs4 import BeautifulSoup
import time

while True:
    # Send an HTTP GET request to CoinMarketCap
    url = 'https://coinmarketcap.com/'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        data = []
        rows = soup.select('table tbody tr')
        for row in rows:
            columns = row.select('td')
            if len(columns) >= 8:
                name = columns[2].get_text(strip=True)
                price = columns[3].get_text(strip=True)
                one_hour_change = columns[4].get_text(strip=True)
                twenty_four_hour_change = columns[5].get_text(strip=True)
                seven_day_change = columns[6].get_text(strip=True)
                try:
                    market_cap = '$'+ columns[7].get_text(strip=True).split('$')[1]
                except:
                    market_cap = columns[7].get_text(strip=True)

                volume_24h = columns[8].get_text(strip=True)
                circulating_supply = columns[9].get_text(strip=True)

                # Add data to the list
                data.append({
                    'name': name,
                    'price': price,
                    'one_hour_change': one_hour_change,
                    'twenty_four_hour_change': twenty_four_hour_change,
                    'seven_day_change': seven_day_change,
                    'market_cap': market_cap,
                    'volume_24h': volume_24h,
                    'circulating_supply': circulating_supply
                })
        print(data)


        django_url = 'http://127.0.0.1:8000/coinmarketcap/receive_data/'
        response = requests.post(django_url, json=data)
        if response.status_code == 200:
            print("Data sent successfully to Django.")
        else:
            print("Failed to send data to Django.", response.status_code)
    else:
        print("Failed to fetch data from CoinMarketCap.")
    
    # Wait for 3 seconds before making the next request
    time.sleep(3)
