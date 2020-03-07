#람다라는 기능
#함수의 매개변수로 함수를 전달

#1)매개변수로 받은 함수를 10번 호출하는 함수
def call_10_times(func):
    for i in range(10):
        func()

def pirnt_hello():
    print("안녕하세요")

call_10_times(pirnt_hello)
