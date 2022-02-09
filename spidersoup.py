import requests
from bs4 import BeautifulSoup

def get_html_soup(url = 'https://blog.betrybe.com/tecnologia/'):    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    res = requests.get(url, headers=headers)
    html_page = res.text

    soup = BeautifulSoup(html_page, 'html.parser')
    soup.prettify()
    #print(soup.title)
    #print(soup.title.string)
    #print(soup.head)
    #print(soup.body)
    return soup

def get_all_page_news(soup_page):
    news = []

    for post in soup_page.find_all("div", {"class": "post-outer"}):   
        item =  dict()
        item['tag'] = post.find("span", {"class": "label"}).string        
        item['title'] = post.find("h2", {"class": "entry-title"}).a.string    
        item['author'] = post.find("span", {"class": "author"}).a.string
        news.append(item)

    return news

def get_next_page(soup_page):
    try:
        return soup_page.find("a", {"class": "next page-numbers"})['href']
    except TypeError:
        return None

def scrape_all(url):
    all_news = []
    
    while get_next_page(get_html_soup(url)) is not None:
        print(get_next_page(get_html_soup(url)))
        all_news.extend(get_all_page_news(get_html_soup(url)))
        url = get_next_page(get_html_soup(url))
    
    return all_news
        

