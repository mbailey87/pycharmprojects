from http.client import responses
from tkinter.font import names
import requests
from bs4 import BeautifulSoup

response = requests.get(url='https://news.ycombinator.com/news')

soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all(class_='score')
print(titles)

scores = [[int(score.getText().split(' ')[0]), score.get('id').split("_")[1]] for score in titles]

high_score = [0, '']
for score in scores:
    if score[0] > high_score[0]:
        high_score = score

print(high_score)
article = soup.find(id=high_score[1]).find(class_='titleline')
article_title = article.getText()
article_link = article.find(name='a').get('href')
print(article)
print(article_title)
print(article_link)



# with open('./website.html') as site:
#     data = site.read()
#
#
# soup = BeautifulSoup(data, 'html.parser')
#
# print(soup.title.string)
# print(soup.p)#gives the first tag that is p
# all_a_tags = soup.find_all(name='a')
# print(all_a_tags)
#
# tag_text = [print(tag.getText(), tag.get('href'))for tag in all_a_tags]
#
# heading = soup.find(name='h1', id='name')
# find_by_class = soup.find(name='h3', class_='heading') #must be class_
# print(heading, find_by_class)
#
# company_url = soup.select_one(selector="p a") #is looking for an anchor tag in a paragraph tag
# print(company_url)
#
# heading_class = soup.select(selector='.heading') #returns a list of all the things with that class
# print(heading_class)