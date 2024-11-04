# Web scraping using selenium
# to simulate the javascript `load more` button click to load 
# more data to scrape
# In plain souping, the beautifulSoup is only able to scrape
# pre-loaded data in the html
from bs4 import BeautifulSoup
import csv
from lxml_html_clean import clean_html
from requests_html import HTMLSession
from selenium import webdriver
import time

world_news_url = 'https://www.ittefaq.com.bd/world-news'
country_news_url = 'https://www.ittefaq.com.bd/country'
national_news_url = 'https://www.ittefaq.com.bd/national'
sports_news_url = "https://www.ittefaq.com.bd/sports"

# with selennium
driver = webdriver.Chrome()
driver.get(sports_news_url)

count = 0
while count <= 10:
    try:
        load_more_button = driver.find_element("class name","ajax_load_btn")
        load_more_button.click()
        time.sleep(2)
    except:
        break # exit if the load more button not found
    count += 1

soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

all_h2 = soup.find_all('h2')

a_tags = [ a_tag.text for h2 in all_h2 for a_tag in h2.find_all('a')]
# for h2 in all_h2:
#     for a_tag in h2.find_all('a'):
#         a_tags.append(a_tag.get_text())

print(a_tags)
with open("headlines3.csv", mode='a', newline="", encoding='utf-8' ) as file:
    writer = csv.writer(file)
    writer.writerow(["Headlines"])
    for text in a_tags:
        writer.writerow([text])

print("data is saved in CSV")