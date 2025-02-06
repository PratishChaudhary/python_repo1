import requests

url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2024-12-12&'
       'sortBy=popularity&'
       'apiKey=1d2f869a41aa4e29bda9f55b3e487a53')

response = requests.get(url)

print(response.json())