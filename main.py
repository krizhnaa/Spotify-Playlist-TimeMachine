from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv, find_dotenv

# user_date = input("Enter the year you want to travel back to? (YYYY-MM-DD) : ")
user_date= "2015-08-12"

response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_date}")
billboard_page = response.text
soup = BeautifulSoup(billboard_page, "html.parser")

songs = soup.select("li ul li h3")
songs_list = [ song.get_text().strip() for song in songs]
# print(songs_list)

# Spotify Authentication

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

print(client_secret)
