import requests
from bs4 import BeautifulSoup
import datetime
import pickle
import re
from multiprocessing import Pool
from multiprocessing import cpu_count


def scrape_a_page(html_soup):
    project_name = re.sub('\s+', ' ', html_soup.find('h1').text).strip()
    grade = re.match('^\w+', html_soup.find('span', class_='rateYDS').text)[0]



# url = 'https://www.mountainproject.com/route/106774200/zorro'
# response = requests.get(url)
# html_soup = BeautifulSoup(response.text, 'html.parser')
# scrape_a_page(html_soup)
# pool = Pool(cpu_count())

url = 'https://www.mountainproject.com/data/get-routes-for-lat-lon?lat=37.7385&lon=-119.5748&maxDistance=200&minDiff=5.6&maxDiff=5.10&key=200392249-3af78beec25d2935b0e438df1ceef746'
response = requests.get(url)
print(response.content)
