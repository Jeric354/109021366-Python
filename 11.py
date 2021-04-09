import urllib.request as req
ur1="http://dns2.asia.edu.tw/~jdwang/PaperList.html"

request = req.Request(ur1, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf8")

import bs4
root = bs4.BeautifulSoup(data, "html.parser")
titles= root.find("div" , class_="title")
print(titles)   