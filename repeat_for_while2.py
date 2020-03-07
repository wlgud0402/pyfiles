#for 반복문 with 범위
#for 숫자변수,코드 in 범위 :

for a in range(0,10,3):
    print(str(a)+ " 반복변수")

print()
#for 반복문 with 리스트

array = [273, 32, 103, 57, 52]
for b in range(len(array)):
    print("{}번째 반복: {}".format(b, array[b]))

#for 반복문 반대로 반복하기
for c in range(4, 0-1, -1):     #0-1로 표현한 이유는 0을 넣어야한다고 강조하기 위해서이다. -1도 가능
    print("현재반복변수 :", "{}".format(c))


print()
#reversed()
for d in reversed(range(5)):
    print("현재반복변수 :", "{}".format(d))