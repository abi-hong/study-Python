import requests
from bs4 import BeautifulSoup

url = "https://entertain.naver.com/home"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# print(soup.title)
# print(soup.title.get_text())

# print(soup.find("a", attrs={"class": "logo_enter"}))

# rank1 = soup.find("a", attrs={"onclick": "nclk(this, 'com.relist', '', '');"})
# print(rank1)
# print(rank1.get_text())
# rank2 = rank1.find_next_siblings("li")
# print(rank2)

news = soup.find_all("a", attrs={"onclick": "nclk(this, 'com.relist', '', '');"})
for new in news:
    print(new.get_text())
