#while 반복문:break 키워드/continue 키워드
#무한 반복문에서 벗어날때 break 사용

i = 0
while True:
    print("{}번째 반복문입니다".format(i))
    i+=1
    input_text = input("반복을 종료하시겠습니까?(y/n): ")
    if input_text in ["Y","y"]:
        print("반복을 종료합니다")
        break

print()
print()
#continue() 현재 반복을 생략하고 다음반복으로 넘어갈때 사용

numbers = [5, 15, 6, 20, 7, 25]

for number in numbers:
    if number <10:     #number 가 10보다 작으면 다음 반복으로 넘어간다는 뜻
        continue
    print(number)

print()

for number in numbers:
    if number >=10:
        print(number)

