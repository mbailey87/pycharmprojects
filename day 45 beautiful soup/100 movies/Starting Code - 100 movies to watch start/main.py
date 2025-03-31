import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)

soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all('h3',class_='title')
titles.reverse()

titles = [title.getText() for title in titles]
print(titles)
with open("./movies.txt", 'a', encoding="utf-8") as file:
    for movie in titles:
        file.write(f"{movie}\n")



