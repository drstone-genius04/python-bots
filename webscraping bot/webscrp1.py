import requests
from bs4 import BeautifulSoup

# The URL of the IMDb Top 250 Movies page
url = "https://www.imdb.com/chart/top"

# Make a GET request to the website's URL using requests
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the movie items on the page using BeautifulSoup's find_all method
movies = soup.find_all("td", class_="titleColumn")

# Loop through the movies and extract the title and rating of each movie
for movie in movies:
    # Get the title of the movie
    title = movie.find("a").text.strip()
    
    # Get the rating of the movie
    year = movie.find("span", class_="secondaryInfo").text.strip("()")

  
    print(title,year)

