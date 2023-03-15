import urllib.parse
import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime

# create list and base url string
locations = ["London", "NewYork", "Bangkok"]
base_url = "https://www.google.com/search?q=weather+"

# header used to mimic a browser to pass the info
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

#while below loop is true will the loop will continue until found false
while True:
    # loop to create dynamic url for the web pages
    for location in locations:
        # generate the url for location
        url = base_url + location.replace(" ", "+")

        # send get request with the header to act as a browser and bring back the info
        response = requests.get(url, headers=headers)

        # parse the information with the beautifulsoup library
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract current weather information
        location_name = soup.select("span.BBwThe")[0].getText()
        timeGo = soup.select("#wob_dts")[0].getText().strip()
        timeGo = timeGo.split(" ")[1]

        info = soup.select("#wob_dc")[0].getText().strip()
        celsius = int(soup.select("#wob_tm")[0].getText().strip())
        farenheit = celsius * 9 / 5 + 32

        # Print weather information for location
        print(f"Location: {location_name}")
        print(f"Time: {timeGo}")
        print(f"Weather: {info}")
        print(f"Temperature: {celsius}°C, {farenheit}°F\n")

    # time format for lewis
    now = datetime.now()
    lewis_dt = now.strftime("%d_%m_%y - %H:%M:%S")
    print(f"-----------------\n")
    print(f"Current Date - Time = {lewis_dt}\n")

    # loops every 20 seconds
    time.sleep(20)
