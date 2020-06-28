from bs4 import BeautifulSoup
import requests

with open('simple.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')   #lmxl ile parse edeceğiz.


print(soup)  #bütün html ' i açtı! formatlanmamış halde.
print("="*100)
print(soup.prettify())   #bu da html'i formatlı bir şekilde gösteriyor.