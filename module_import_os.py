#os 모듈
#운영체제와 관련된 기능을 가진 모듈: 새로운 폴더를 만들거나 폴더 내부의 파일 목록 보는 일함

import os

print("현제 운영체제: ", os.name)
print("현재폴더: ", os.getcwd())
print("현재폴더 내부의 요소: ", os.listdir())

#폴더를 만들고 제거
os.mkdir("hello")    #폴더를 만듦
os.rmdir("hello")    #폴더를 제거함

#파일을 생성하고 + 파일 이름을 변경함
with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")

#파일을 제거함
os.remove("new.txt")
#os.unlink("new.txt")

#시스템 명령어 실행
os.system("dir")



