#함수의 꽃 메모화



#메모변수를 만듭니다
dictionary = {
    1:1,
    2:2
}
#함수 선언
def fibonacci(n):
    if n in dictionary:
        #메모가 되있으면 메모된 값을 리턴
        return dictionary[n]
    else:
        #메모가 되있지 않으면 값을 구함
        output = fibonacci(n-1) + fibonacci(n-2)
        dictionary[n] = output   #한번 계산한 output을 메모에 저장
        return output
print(fibonacci(20))