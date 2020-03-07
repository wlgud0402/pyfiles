#가변매개변수가 기본매개변수보다 앞에올때   >>>>가변매개변수가 우선시 된다   
def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
print_n_times("헬로","해피","파이썬",3)     #헬로 해피 파이썬 3 을 출력

print()
print()
#가변매개변수와 기본매개변수를 함께 사용하기 위한
#((키워드 매개변수))
#해결방법>>>>>매개변수 이름을 지정해서 입력:키워드 매개변수

def print_n_times2(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
print_n_times2("헬로","해피","파이썬",n=3)    #>>>>>n=3으로 지정:키워드매개변수
print()
print()

#기본 매개변수중에서 필요한 값만 입력하기 키워드 매개변수 응용
#일반매개변수값은 항상 그 자리에 맞게 입력해야 한다

def test(a, b=10, c=100):
    print(a+b+c)

test(10, 20, 30)    #기본형태 모두 새로 들어감

test(a=10, b=100, c=200)    #키워드 매개변수로 모든 매개변수를 지정

test(c=10, a=100, b=200)    #키워드 매개변수의 순서가 마구잡이

test(10, c=200)             #키워드 매개변수로 일부 매개변수만 지정한 형태


