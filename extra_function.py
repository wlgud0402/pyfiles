#파이썬만의 기능들

a = [15,97,152,147,52]

print(sum(a))    #값을 모두 더함
print(max(a))    #최댓값을 찾아줌
print(min(a))    #최솟값을 찾아줌

print()

#reversed

b = [1,2,3,4,5]
b2 = reversed(b)

print(b)
print(b2)#<list_reverseiterator object at 0x013D51A8  함수를 모두 복제하고 뒤집는걸 불필요하다 판단

for i in reversed(b):
    print("-", i)

print()
#reversed는 큰 데이터를 복제하는것을 거절하는 느낌!
#그래서 reversed_A = reversed(A) 이렇게 새로 만들지 않고 필요할때만 넣어서 사용한다

temp = reversed([1,2,3,4,5,6])

for z in temp:
    print("첫번째 반복문: {}", format(z))

for z in temp:
    print("두번째 반복문: {}", format(z))    
    #두번째 반복문은 실행 x reversed() 의 결과가 제너레이터 이므로

print()
print()

numbers = [1,2,3,4,5,6,7]

for v in reversed(numbers):
    print("첫번째 반복문: {} ".format(v))  #for 구문내에 넣어서 바로 실행!

for v in reversed(numbers):
    print("두번째 반복문: {} ".format(v))

print()
# 플러스 팁! 비파괴적 문법 황장 슬라이싱 리버스와 기능적으로는 같다

print(numbers)
print(numbers[::-1])   #[::-1]  을넣어서 뒤집을수 있다

print("안녕하세요"[::-1])   #문자열에도 사용가능!
