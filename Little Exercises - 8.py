#8. Write a Python program to extract all the URLs from the webpage python.org that are nested within <li> tags from . Go to the editor
import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

urls = []
for h in soup.find_all('li'):
    a = h.find('a')
    urls.append(a.attrs['href'])
print(urls)