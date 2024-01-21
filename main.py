from bs4 import BeautifulSoup
import requests

# user_date = input("Enter the year you want to travel back to? (YYYY-MM-DD) : ")
user_date= "2015-08-12"

response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_date}")
billboard_page = response.text
soup = BeautifulSoup(billboard_page, "html.parser")

songs = soup.find_all("h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

songs_list = [ song.get_text().strip() for song in songs]
print(songs_list)
