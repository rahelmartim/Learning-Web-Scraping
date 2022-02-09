from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()

def scrape(url):
    browser.get(url)

    news = []
    for report in browser.find_elements(By.CLASS_NAME, 'post-outer'):
        item = dict()

        item['tag'] = report.find_element(By.CLASS_NAME, 'label').get_attribute("innerHTML")        
        item['title'] = report.find_element(By.CLASS_NAME, 'entry-title').find_element(By.TAG_NAME, 'a').get_attribute("innerHTML")        
        item['author'] = report.find_element(By.CLASS_NAME, 'author').find_element(By.TAG_NAME, 'a').get_attribute("innerHTML")    
        news.append(item)

    return news

total_news = []
index = 1
next_link = 'https://blog.betrybe.com/tecnologia/'
while index <= 16:
    total_news.append(scrape(next_link))
    print(next_link)

    next_link = browser.find_element(By.CLASS_NAME, 'next').get_attribute("href")   

    browser.get(next_link)
    
    index += 1
    
print(len(total_news))
print(total_news)
#print(news)