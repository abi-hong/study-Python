from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("./chromedriver.exe")
browser.get("http://naver.com")

elem = browser.find_element_by_class_name("link_login")
elem.click()

browser.back()
browser.forward()
browser.refresh()

elem = browser.find_element_by_id("query")
elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)

elem = browser.find_element_by_tag_name("a")
for e in elem:
    e.get_attribute("href")

browser.get("http://daum.net")
elem = browser.find_element_by_name("q")
elem.send_keys("나도 코딩")
elem.send_keys(Keys.ENTER)

elem = browser.find_element_by_xpath("xpath 경로")
elem.click()
browser.close()
browser.quit()
