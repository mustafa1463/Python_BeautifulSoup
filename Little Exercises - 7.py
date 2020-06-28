#7. Write a Python program to find the href of the first <a> tag of a given html document. Go to the editor

from bs4 import BeautifulSoup
html = open('blogger.html', 'r')
soup = BeautifulSoup(html, 'html.parser')

a = soup.find('a')
a = str(a)
list1 = a.split('"')
print(list1[1])
