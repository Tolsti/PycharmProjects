from bs4 import BeautifulSoup
import requests
import random
import re


url = 'http://anekdotov.net/anekdot/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')

list_of_jokes = soup.find_all('div', align = 'left')

# for i in list_of_jokes:
#     print(i.text)
# print(len(list_of_jokes) - 1)print(unicode(list_of_jokes[random.randint(0, len(list_of_jokes) - 1)].text,'cp866'))
# # list_joke=list()
# # for i in soup.h1.attrs:
#     list_joke.append(i)
# print(list_joke)
