from bs4 import BeautifulSoup
import requests

with open('simple.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')   #lmxl ile parse edeceğiz.

match1 = soup.title
match2 = soup.title.text
print(match1)
print(match2)
print("="*100)

match3 = soup.div   #ilk div tagini veriyor! sadece ilkini.
match4 = soup.find('div', class_='footer')  #footer id'si olan div'i ver.
print(match4)
print("="*100)

article = soup.find('div', class_="article")
print(article)
headline = article.h2.a.text
print(headline)

summary = article.p.text
print(summary)
print("="*100)
print("="*100)

article_all = soup.find_all('div', class_="article")  #class'ı article olanların hepsinden bir liste oluşturuyor.

for article in article_all:
    artical = article.h2.a.text
    print(artical)
    summary = article.p.text
    print(summary)






