#3. Write a Python program to get the number of paragraph tags of a given html document. Go to the editor

from bs4 import BeautifulSoup

html = open('blogger.html', 'r')
sum = 0
soup = BeautifulSoup(html, 'html.parser')
tags = soup.find_all('p')

for i in tags:
    sum += 1

print("The number of p tags: " + str(sum))



html.close()  #Never forget to close!!!