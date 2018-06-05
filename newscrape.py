from bs4 import BeautifulSoup
import requests
import pymongo
import pandas as pd
from splinter import Browser

mars_news = 'https://mars.nasa.gov/news/'
mars_weather = 'https://twitter.com/marswxreport?lang=en'

response = requests.get(mars_news)
soup = BeautifulSoup(response.text, 'html.parser')

results = soup.find_all(class_="slide")
titles_list = []
paragraphs_list = []
for result in results:
    links = result.find_all('a')
    title = links[1].text
    paragraph = result.find(class_="rollover_description_inner").text
    titles_list.append(title)
    paragraphs_list.append(paragraph)
    print(title)
    print(paragraph)


weather_response = requests.get(mars_weather)
soup = BeautifulSoup(weather_response.text, 'html.parser')

results = soup.find_all(class_="content")
tweets_list = []
for result in results:
    tweet = result.find('p', class_="TweetTextSize").text
    tweets_list.append(tweet)
    print(tweet)

mars_weather = tweets_list[0]

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

scraped_dict = {'Title': titles_list,
                'Weather': mars_weather
}