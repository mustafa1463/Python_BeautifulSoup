#1. Write a Python program to find the title tags from a given html document.
from bs4 import BeautifulSoup
index = open('index.html', 'r')

soup = BeautifulSoup(index, 'html.parser')

print(soup.find('title').text)
index.close()
