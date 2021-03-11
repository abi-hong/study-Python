# https://www.daum.net/접속
# 송파 헬리오시티 검색
# 다음 부동산 부분에 나오는 결과 정보 웹 스크래핑


import requests
from bs4 import BeautifulSoup

# from selenium import webdriver

# browser = webdriver.Chrome()
# browser.maximize_window()

url = "https://search.daum.net/search?nil_suggest=sugsch&w=tot&DA=GIQ&sq=%EC%86%A1%ED%8C%8C+%ED%97%AC%E3%84%B9&o=1&sugo=15&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
# browser.get(url)

# browser.find_element_by_id("q").send_keys("송파 헬리오시티")
# browser.find_element_by_class_name("ico_pctop btn_search").click()

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# with open("quiz.html", "w". encoding="utf8") as f:
#    f.write(soup.prettify())

data_rows = soup.find("table", attrs={"class": "tbl"}).find("tbody").find_all("tr")

for index, row in enumerate(data_rows):
    columns = row.find_all("td")

    print("======= 매물 {} =======".format(index + 1))
    print("거래 :", columns[0].get_text())
    print("면적 :", columns[1].get_text(), "(공급/전용)")
    print("가격 :", columns[2].get_text(), "(만원)")
    print("동 :", columns[3].get_text())
    print("층 :", columns[4].get_text())
