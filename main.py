import requests
from bs4 import BeautifulSoup

#define the URL
url = "https://www.google.com/search?q=weather+coventry"

#define deader to mimic browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

#send a get request to url with headers
res = requests.get(url, headers=headers)

#parse the html though beautifulsoup
soup = BeautifulSoup(res.text, 'html.parser')

#find elements using css selector
location = soup.select("span.BBwThe")[0].getText()
time = soup.select("#wob_dts")[0].getText().strip()
info = soup.select("#wob_dc")[0].getText().strip()
temperature = soup.select("#wob_tm")[0].getText().strip()

#outputs n that
print(location)
print(time)
print(info)
print(temperature + "°C")
