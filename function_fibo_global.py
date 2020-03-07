#global 키워드>> 외부의 변수 설정한 값을 가져옴
#사용법 global 변수이름
counter = 0

def fibonacci(n):
    print("fibonacci({})을 구합니다".format(n))
    global counter
    counter += 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
print("fibonacci(10)계산에 활용된 덧셈의 횟수는 {}번 입니다".format(counter))

#123을구합니다가 여러번 출력됨

