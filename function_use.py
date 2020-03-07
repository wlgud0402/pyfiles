#기본 함수의 활용
#일반적으로 값을 만들어 리턴하는 형태로 많이 쓰임

def sum_all(start, end):
    output = 0
    for i in range(start , end+1):
        output += i
    return output

print(sum_all(2, 5))


print()
print()
#키워드 매개변수를 사용해서 (?, ?, ?)   range에서 세번째인자는 범위사이의 차이값
def sum_all2(start=0, end=100, step=1):
    output2 = 0 
    for i in range(start, end+1, step):
        output2 += i
    return output2

print(sum_all2(0,100,10))
print(sum_all2(end=100))
print(sum_all2(end=100, step=2))
