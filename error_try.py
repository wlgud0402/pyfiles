#try except 구문 
#try:
    #예외가 발생할 가능성이 있는 코드
#except:
    #예외가 발생했을때 실행할 코드

try:
    number_input_a = int(input("정수입력>>"))
    
    print(number_input_a * 3.14)
except:
    print("무언가 잘못되었습니다")