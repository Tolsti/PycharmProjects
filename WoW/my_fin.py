from bs4 import BeautifulSoup
import requests

url = 'https://myfin.by/currency'
html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')

list_of_jokes = soup.find_all('span', class_='sum')
print(list_of_jokes)