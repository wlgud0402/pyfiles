#날짜, 시간

import datetime       #날짜를 가져와주는 모듈을 인스톨 javascript의 fs같은 느낌
#import 자체는 폴더내의 다른 파일을 이름만으로 읽어올수 있다 여기서 datetime은 fs같은거

now = datetime.datetime.now()   #왼쪽now 는 변수 오른쪽 now()는 현재 날짜 시간을 구하는것

print(now)    #현재 년,월,일,시간 표기    now.year    now.month 등으로 그 정보만 가져올수 있다

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

#오전과 오후를 구분
if now.hour <12:
    print("현재시각은 {}시로 오전입니다".format(now.hour))
print()
if now.hour >12:
    print("현재시각은 {}시로 오후입니다".format(now.hour))  #if문이 거짓인경우 뒤의 조건문을 실행X

print()
#계절을 구분하는 프로그램
if 3<= now.month <=5:
    print("현재는 {}월로 봄입니다".format(now.month))

if 6<= now.month <=8:
    print("현재는 {}월로 여름입니다".format(now.month))

if 9<= now.month <=11:
    print("현재는 {}월로 가을입니다".format(now.month))

if now.month == 12 or 1<= now.month <=2:
    print("현재는 {}월로 겨울입니다".format(now.month))
