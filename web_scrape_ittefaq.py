from bs4 import BeautifulSoup
import requests
import csv

world_news_url = 'https://www.ittefaq.com.bd/world-news'
country_news_url = 'https://www.ittefaq.com.bd/country'
national_news_url = 'https://www.ittefaq.com.bd/national'

#  Scraping world news from Ittefaq paper
response = requests.get(national_news_url)

soup = BeautifulSoup(response.text, 'html.parser')

all_h2 = soup.find_all('h2')

a_tags = [ a_tag.text for h2 in all_h2 for a_tag in h2.find_all('a')]
# for h2 in all_h2:
#     for a_tag in h2.find_all('a'):
#         a_tags.append(a_tag.get_text())

print(a_tags)
with open("headlines.csv", mode='a', newline="", encoding='utf-8' ) as file:
    writer = csv.writer(file)
    writer.writerow(["Headlines"])
    for text in a_tags:
        writer.writerow([text])

print("data is saved in CSV")