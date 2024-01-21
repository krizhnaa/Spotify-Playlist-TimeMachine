from bs4 import BeautifulSoup
import requests

user_date = input("Enter the year you want to travel back to? (YYYY-MM-DD) : ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_date}")
billboard_page = response.text
soup = BeautifulSoup(billboard_page, "html.parser")

print(soup)