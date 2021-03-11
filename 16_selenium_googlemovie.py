# 동적 페이지에 대한 웹스크래핑
# 동적 페이지 : 일반적으로 접속될 때, 페이지가 불러와지는 것이 아닌 사용자가 동작했을 때 그때서야 동작하는 웹페이지를 의미한다
import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept-Language": "ko-KR,ko",
}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class": "ImZGtf mpg5gc"})
print(len(movies))

# with open("movie.html", "w", encoding="utf8") as f:
#    f.write(soup.prettify())  # .prettify : html 문서를 예쁘게 출력

for movie in movies:
    title = movie.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()
    print(title)

