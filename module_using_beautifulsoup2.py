from urllib import request
from bs4 import BeautifulSoup

# naver에서 페이지 가져옴
target = request.urlopen("https://www.naver.com/")
# utf-8로 읽음
result = target.read().decode("utf-8")

soup = BeautifulSoup(result, "html.parser")

# List 로 받아짐
titles = soup.select(".ca_a")  #css 선택

print(titles[0].text)

for v in titles:
    print(v.text)