import requests
import time
from  bs4 import BeautifulSoup

URL = "https://www.majortests.com/word-lists/word-list-0{0}.html"


def generate_urls(ur1,start_page, end_page):
    urls = []
    for page in range(start_page, end_page):
        urls.append(ur1.format(page))
    return urls

def get_resource(url) :
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }
    return requests.get(url,headers=headers) 
def parse_html(html_str) : 
    return BeautifulSoup(html_str, "lxml")



def     get_word(soup,file):
    words = []
    count = 0
    for wordlist_table in soup.find_all(class_="wordlist"):
        count +=1
        for word_entry in wordlist_table.find_all("tr"):
            new_word = []
            new_word.append(file)
            new_word.append(str(count))
            new_word.append(word_entry.th.text)
            new_word.append(word_entry.td.text)
            words.append(new_word)
    return words
def wed_scraping_bot(urls):
    eng_words = []
    for url in urls:
        file = url.split("/")[-1]
        print("catching:", file, "wed data...")
        r = get_resource(url)
        if r.status_code == requests.code.ok:
            soup = parse_html(r.text)
            words = get_word(soup,file)
            eng_words = eng_words + words
            print("waiting 5 secound...")
            time.sleep(5)
        else:
            print('HTTP request error')    
    return eng_words    


    if __name__ == "__main__":
    urlx = generate_urls(URL, 1, 3)
    eng_words = wed_scraping_bot(urlx
    print(eng_words)