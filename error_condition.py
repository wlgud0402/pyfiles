#조건문으로 예외 처리하기

user_input_a = input("정수입력>>")

if user_input_a.isdigit():
    number_input_a = int(user_input_a)

    print(number_input_a *3.14)
else:
    print("정수를 입력하지 않았습니다")