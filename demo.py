import requests
import bs4
req = requests.get("http://120.108.116.237/~jackjow/pubList.php")
req.encoding = 'utf8'
rc = req.content
soup = bs4.BeautifulSoup(rc,"html.parser")

if req .status_code==200:
    f = open("output.txt" ,'w' , encoding='utf8')
    # f.write(soup.find("div", id='text'))
    for li in soup.find('div' , id=home).find_all('li'):
        t =li.text.replace('\n','').replace(' ','').replace(' ','')
        f.write(t+"\n")
    f.close() 



# print(soup.body)
print(soup.find("div" , id="home"))
print(soup.find("div" , id="home").find_all('li'))
# print(soup,find("ol" , id="publist").find_all('li'))

#print(req.status_code)
#print(r.content)

#print(bs4.BeautifulSoup(r.content, "html.parser"))