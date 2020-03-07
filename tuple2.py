#리스트와 튜플의 특이한 활용  변수선언, 할당
[a,b] = [10, 20]
(c,d) = (30,40)
print(a,b,c,d)

#특이한 활용 (2) 괄호를 생략할 수도 있다
tuple_test = 11,22,33,44
print(tuple_test)

e,f,g = 14,15,16
print(e,f,g)

#튜플로 변수의 값을 교환
t1,t2 =1,8
print(t1,t2)
t1,t2 = t2,t1        #a,b =b,a 로 값을 뒤바꿈
print(t1,t2)
