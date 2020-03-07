#재귀함수를 이용한 피보나치 수열 구하기 232p
#토끼 번식 문제

def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
#시간이 오래걸렸다
print(fibonacci(7))

