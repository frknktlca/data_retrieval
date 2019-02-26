import requests

from bs4 import BeautifulSoup

url = "https://www.youtube.com"

response = requests.get(url)

html_content = response.content

soup = BeautifulSoup(html_content,"html.parser")

name = soup.find_all("h3",{"class":"yt-lockup-title "})

for i in name:
    print(i.text)