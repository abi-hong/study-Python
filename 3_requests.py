import requests

res = requests.get("http://google.com")
# res = requests.get("http://naver.com") #url정보를 넘겨주면 됨
# res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status()
# print("응답코드 :", res.status_code) #200이면 정상

# 두가지로 나타낼 수 있다(if문 / raise_for_status)

# if res.status_code == requests.codes.ok: #정상이라는 뜻
#    print("정상입니다")
# else:
#    print("무제가 생겼습니다. [에러코드 ", res.status_code, "]")

# res.raise_for_status() #웹스크랩핑을 하기위해서 올바른 코드를 가지고 오면 문제가 없고 그렇지 않은 경우는 에러를 낸다.
# print("웹 스크래핑을 진행합니다")


print(len(res.text))  # 가져온 글자 개수
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
