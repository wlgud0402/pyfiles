#매개변수를 활용     #함수의 ()안에 들은것>>매개변수
def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("안녕하세요",5)

print()
print()
#가변 매개변수>>>> 여러개를 넣을 수있다    *가변매개변수
#규칙 1) 가변매개변수 뒤에는 일반 매개변수가 올 수 없다
#규칙 2) 가변매개변수는 하나만 사용할 수 있다

def print_uncertain_n_times(n, *values):
    for i in range(n):
        print(*values)

print_uncertain_n_times(3, "안녕","즐거운","파이썬")

print()
print()
def print_uncertain_n_times2(n, *values): 
    for i in range(n):
        for value in values:           #반복문을 두번 사용해서 쪽 출력하게 만듦
            print(value)

print_uncertain_n_times2(3, "안녕","즐거운","파이썬")