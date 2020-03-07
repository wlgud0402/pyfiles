#BeautifulSoup 모듈로 날씨 읽어오기 >>>크롤러
#모듈을 읽어들임
from urllib import request
from bs4 import BeautifulSoup

#urlopen()함수로 기상청의 전국 날씨를 읽음
target = request.urlopen("http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

#beautifulsoup 를 사용해 웹페이지를 분석
soup = BeautifulSoup(target, "html.parser")

#location 태그를 찾습니다
for location in soup.select("location"):
    #내부의 city, wf, tmn, tmx태그를 찾아 출력 >>>string 의 형태로 문자만
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
