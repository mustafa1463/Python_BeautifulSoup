#4. Write a Python program to extract the text in the first paragraph tag of a given html document. Go to the editor

from bs4 import BeautifulSoup

html = open('blogger.html', 'r')
soup = BeautifulSoup(html, 'html.parser')

print(soup.find('p').text)

html.close()