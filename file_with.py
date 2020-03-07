#with 키워드   열고 안닫는 실수 없게 자동으로 실행후 닫음
#사용법

#with open(문자열:경로, 문자열:모드) as 파일객체:
    #문장

with open("file_open_with.txt", "w") as file:
    file.write("HELLO WORLD")
