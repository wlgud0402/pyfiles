#끝자리로 짝수와 홀수 구분
number = input("정수를 입력하세요>")

last_character = number[-1]     #number 변수의 마지막 자리의 숫자를 추출

last_number = int(last_character)

#줄이 너무 길어지면 \로 줄바꿈을 시킨다 마치 자바스크립트의 <br>
if last_number == 0\
    or last_number == 2\
    or last_number == 4\
    or last_number == 6\
    or last_number == 8:#끝에는 :로 조건문을 끝냄
    print("짝수입니다")

print()
if last_number == 1\
    or last_number == 3\
    or last_number == 5\
    or last_number == 7\
    or last_number == 9:#끝에는 :로 조건문을 끝냄
    print("홀수입니다")


#in 연산자로 짝수, 홀수 구분
number2 = input("정수입력>")
last_character2 = number2[-1]

if last_character2 in "02468":
    print("짝수입니다")

if last_character2 in "13579":
    print("홀수입니다")

#나머지 연산자를 활용해서 짝수와 홀수 구분
number3 = input("정수입력")
number3 = int(number3)
if number3 %2 == 0:
    print("짝수입니다.")
if number3 %2 == 1:
    print("홀수입니다.")
