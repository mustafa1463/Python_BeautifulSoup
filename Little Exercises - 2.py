#2. Write a Python program to retrieve all the paragraph tags from a given html document. Go to the editor

from bs4 import BeautifulSoup
html = open('blogger.html', 'r')
soup = BeautifulSoup(html, 'html.parser')
print(soup.find('p').text)      #this prints out the FIRST one.

print("="*100)

for text in soup.find_all('p'):
    text = text.text            #now all the paragraph tags.
    print(text)



html.close()