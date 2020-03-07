#반복문을 사용한 리스트 생성
array = []
for i in range(0,20,2):
    array.append(i * i)
print(array)

print()

#리스트 안에 for문 사용하기
list_a = [z * z for z in range(0, 20, 2)]      #최종결과를 앞에 작성 z*z
print(list_a)

print()
#if문도 추가하기

newarray = [1,2,3,4,5,6,7,8,9]
output = [number for number in newarray if number != 3]  

print(output)