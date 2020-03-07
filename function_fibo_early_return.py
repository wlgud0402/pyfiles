#조기 리턴
dictionary = {
    1:1,
    2:2
}
def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n-1) +fibonacci(n-2)
        dictionary[n] = output
        return output
print(fibonacci(10))
#사용후 줄어들은 들여쓰기 else 제거됨
dictionary_early = {
    1:1,
    2:2
}
def fibonacci_early(n):
    if n in dictionary_early:          #함수의 실행조건에 안맞는 것들을 미리 조기에 날려버림
        return dictionary_early[n]     #한블럭안에 넣음
    output_early = fibonacci_early(n-1) +fibonacci(n-2)
    dictionary_early[n] = output_early
    return output_early

print(fibonacci_early(10))
