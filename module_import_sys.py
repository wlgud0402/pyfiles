#sys 모듈
#시스템과 관련돈 정보를 가지고 있는 모듈
#명령 매개변수를 받을 때 많이 사용된다

import sys

print(sys.argv)    #명령 매개변수를 출력한다 (sys.arge)>>가바로 매개변수

print("getwindowsversion: ", sys.getwindowsversion())
print("copyright: ", sys.copyright)
print("version: ", sys.version)

sys.exit()

#cmd 명령 프롬프트 창에서 python 파일명.py 10 20 30
#을 입력하면 10 20 30 이라는 리스트가 sys.argv에 들어온다
#이를 통해 뒤에 file.txt 같은것을 추가해 파일경로를 외부에서 지정할수도 있다
