#urllib 모듈
#URL을 다르는 라이브러리

from urllib import request

#urlopen()함수로 구글의 메인페이지를 읽습니다.
target = request.urlopen("https://google.com")
output = target.read()

print(output)