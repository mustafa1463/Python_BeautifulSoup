#6. Write a Python program to find the text of the first <a> tag of a given html text. Go to the editor


from bs4 import BeautifulSoup
html = open('blogger.html', 'r')
soup = BeautifulSoup(html, 'html.parser')

a = soup.find('a').text
print(a)