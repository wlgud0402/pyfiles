#기본 매개변수    #매개변수 = 값 의 형태
#규칙 1) 기본매개변수 뒤에는 일반 매개변수가 올 수 없다.
# 값을 특정 하지 않으면 앞에 정한 값으로 출력

def print_n_times(value, n=2):     #n=2 형태의 기본 매개변수
    for i in range(n):
        print(value)
print_n_times("안녕하세요")          #값을 안정했으므로 n=2 그대로 출력
print_n_times("안녕",3)              #값을 3으로 특정>>>>3번 출력


print()
print()
#기본매개변수가 가변매개변수보다 앞에올때
# def print_uncertain_n_times2(n=2, *values):      
#     for i in range(n):           #range()함수의 매개변수에는 숫자만 들어올 수 있으므로 오류
#         for value in values:     #매개변수가 순서대로 입력되므로 n에 "안녕" 이 들어가게됨     
#             print(value)

# print_uncertain_n_times2("안녕","즐거운","파이썬")

#가변매개변수가 기본매개변수보다 앞에올때   >>>>가변매개변수가 우선시 된다   
def print_n_times2(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
print_n_times2("헬로","해피","파이썬",3)     #헬로 해피 파이썬 3 을 출력
