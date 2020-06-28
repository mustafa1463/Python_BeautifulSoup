#5. Write a Python program to find the length of the text of the first <h2> tag of a given html document. Go to the editor

from bs4 import BeautifulSoup
html = open('blogger.html', 'r')
soup = BeautifulSoup(html, 'html.parser')

h2 = soup.find('h2').text
length= 0

for i in h2:
    length += 1

print(h2)

print(length)

