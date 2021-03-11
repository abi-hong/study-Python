from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("./chromedriver.exe")
browser.maximize_window()  # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)

# 가는날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 14일, 15일 선택
browser.find_elements_by_link_text("14")[0].click()  # [0] -> 이번달
browser.find_elements_by_link_text("15")[0].click()  # [0] -> 이번달

# 다음달 14일, 15일 선택
browser.find_elements_by_link_text("14")[1].click()  # [1] -> 다음달
browser.find_elements_by_link_text("15")[1].click()  # [1] -> 다음달

# 이번달 14일부터 다음달 15일 선택
browser.find_elements_by_link_text("14")[0].click()  # [0] -> 이번달
browser.find_elements_by_link_text("15")[1].click()  # [1] -> 다음달

# 제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

# WebDriverWait를 통해서 브라우저를 10초동안 기다린다. xpath에 해당하는 element가 나올 때까지 기다려달라는 것이다.
# 이 과정이 10초안에 끝나면 바로 진행한다.
try:
    elem = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]"
        )
    )
    #성공했을 때 동작 수행
    print(elem.text) # 첫 번째 결과 출력
finally:
    browser.quit()

# 첫번째 결과 출력
#elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
#print(elem.text)
