import requests

api_url = 'http://numbersapi.com/'

response = requests.get(api_url)

if response.status_code == 43:
    print(response.text)
else:
    print(response.status_code)