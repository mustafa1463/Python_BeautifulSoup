from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com/').text  #source cod'u aldık.

soup = BeautifulSoup(source,'lxml')

article = soup.find('article')
print(article.prettify())

headline = article.h2.a.text
print(headline)
print("="*100)
summary = article.div.p.text
print(summary)
print("="*100)
summary = article.find('div',class_='entry-content').p.text
print(summary)

vid_src = article.find('iframe', class_="youtube-player")['src']
print(vid_src)
vid_id = vid_src.split("/")[4]
vid_id = vid_id.split('?')
vid_id = vid_id[0]

yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)
print("="*100)
print("="*100)




