#while 반복문 while 불 표현식, 문장:
#불표현식이 참인동안 문장을 계속 반복함
# while True:
#     print("H", end="")

#while 반복문을 for 반복문처럼 사용하기
i = 0
while i<10:
    print("{}번째 반복입니다".format(i))
    i+=1

print()

#while 상태기반 반복
list_a = [1,2,1,2]
value = 2

while value in list_a:
    list_a.remove(value)

print(list_a)

print()
#유닉스 타임 기반 반복    유닉스타임:1970 1월 1일 기준 시간이 얼마나 지났는지
#import time      , time.time()>>>>>> 155484815184.1549618

import time
number = 0

target_tick = time.time() +5
while time.time() < target_tick:
    number +=1
print("5초동안 {}번 반복했습니다.".format(number))

