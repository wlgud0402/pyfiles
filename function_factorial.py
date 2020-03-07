#팩토리얼을 구하는 방법 
#1) 반복문
#2) 재귀함수

#반복문으로 팩토리얼 구하기
def factorial(n):
    output = 1
    for i in range(1, n+1):
        output *= i
    return output

print(factorial(10))

print()
print()
#재귀함수로 팩토리얼 구하기

def factorial_recursion(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursion(n-1)

print(factorial_recursion(5))

