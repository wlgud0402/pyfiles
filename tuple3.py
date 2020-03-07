#튜플과 함수의 리턴
def test():
    return(10,20)
a,b= test()
print(a,b)

#튜플을 리턴하는 함수의 예
for i, value in enumerate([1,2,3,4,5,6]):
    print("{}번째 요소는 {}입니다".format(i,value))

print()
print()

#나누기
a,b = 97,40
print(a//b)   #몫
print(a%b)    #나머지

#divmod()함수>>> 튜플형태로 몫과 나머지를 리턴
a,b = 97,40
print(divmod(a,b))
x,y = divmod(a,b)
print(x,y)