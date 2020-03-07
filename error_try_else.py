#try except else구문
#try:
    #예외가 발생할 가능성이 있는 코드
#except:
    #예외가 발생했을때 실행할 코드
#else:
    #예외가 발생하지 않았을때 실행할 코드

#else 구문 내용을 try 안에 넣어도 상관은 없음
#그냥 취향차이

try:
    number_input_a = int(input("정수입력>>"))
except:
    print("정수를 입력하지 않았습니다")
else:
    print(number_input_a * 3.14)