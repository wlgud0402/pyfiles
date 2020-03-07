#범위 range 
# range(5) 0부터 4까지 
# range(2,8) 2부터 7까지
# range(0,10,2)  0부터 9까지 값의 차이는 세번째 매개변수인 2만큼가진다

a = range(10)
print(a)

print(list(a))     #리스트로 출력

b = range(2, 8)
print(list(b))

c = range(0,10,2)
print(list(c))

d = range(0, 10+1)    #10까지 포함한다는 것을 강조할수 있게됨
print(list(d))