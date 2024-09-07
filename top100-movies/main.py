# Gets all the necessary libraries
from bs4 import BeautifulSoup
import requests


response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/") # gives access to the web page
empireWebpage = response.text   # stores the web page html as text

# allows us to parse through the html stored in the var empireWebpage
soup = BeautifulSoup(empireWebpage, "html.parser")

articleTitleTags = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")  # stores all the h3 tags
articleTitleList = [article_tag.getText() for article_tag in articleTitleTags]                  # creates a list with all 100 movies in decreasing order

# creates a file and stores all 100 movies from starting from 1
with open("top100Movies.txt", "w") as file:
    for movie in articleTitleList[::-1]:
        file.write(movie)
        file.write("\n")

