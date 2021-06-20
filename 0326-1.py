import requests
import bs4
url = "http://isrc.ccs.asia.edu.tw/www/myjournal/myjournal.htm" # 黃明祥老師的連結
response = requests.get(url)
response.encoding = 'big5'
rc = response.content
soup = bs4.BeautifulSoup(rc, 'html.parser') 
if response.status_code == 200:
    f = open('output-publication.txt', 'w', encoding='utf8')
    for tagP in soup.find_all('p', 'MsoNormal'):
        t = tagP.text.replace('\t', '').replace('\n', '')
        f.write(t+'\n')

f.close()