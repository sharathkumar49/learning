# REST API Client (consume a public API and display results)
import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()

print("Bitcoin Price Index:")
for currency, info in data['bpi'].items():
    print(f"{currency}: {info['rate']}")
