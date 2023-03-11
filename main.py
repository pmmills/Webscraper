import requests
from bs4 import BeautifulSoup

# define the URLs for the different locations
urls = {
    "London": "https://www.google.com/search?q=weather+London",
    "New York": "https://www.google.com/search?q=weather+New+York",
    "Bangkok": "https://www.google.com/search?q=weather+Bangkok",
    "Lisbon": "https://www.google.com/search?q=weather+Lisbon"
}
urlTime = "https://www.google.com/search?q=time+and+date"

# define header to mimic browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

for city, url in urls.items():
    # send a get request to url with headers
    res = requests.get(url, headers=headers)

    # parse the html though beautifulsoup
    soup = BeautifulSoup(res.text, 'html.parser')

    # find elements using css selector
    location = soup.select("span.BBwThe")[0].getText()
    time = soup.select("#wob_dts")[0].getText().strip()
    info = soup.select("#wob_dc")[0].getText().strip()
    temperature = soup.select("#wob_tm")[0].getText().strip()

    # output the weather information for the current city
    print(f"{city} - {location}")
    print(f"Time: {time}")
    print(f"Info: {info}")
    print(f"Temperature: {temperature}°C")
    print("\n")

# send a get request to time and date URL with headers
resTime = requests.get(urlTime, headers=headers)

# parse the html though beautifulsoup
soup1 = BeautifulSoup(resTime.text, 'html.parser')

# Find the current time element using its CSS selector and get its text content
time_element = soup1.select('div.gsrt.vk_bk.FzvWSb.YwPhnf[aria-level="3"]')[0]
current_time = time_element.getText()
date_element = soup1.select("span.KfQeJ")[0].getText()

# output the current time and date
print("Current date:", date_element)
print("Current time:", current_time)
print("Based on UK Timezone")
