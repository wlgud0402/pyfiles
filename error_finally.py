#finally 구문

#try:
    #예외가 발생할 가능성이 있는 코드
#except:
    #예외가 발생했을때 실행할 코드
#else:
    #예외가 발생하지 않았을때 실행할 코드
#finally;
    #무조건 실행할 코드(예외가 발생하든 발생하지 않든!)

try:
    number_input_a = int(input("정수입력"))
    print(number_input_a * 3.14)
except:
    print("정수 입력하라고 했잖아요")
else:
    print("예외가 발생하지 않았씁니다")
finally:
    print("프로그램은 실행되긴 했어요")

# finally 구문은
# 함수에 오류가 있든없든
# 중간에 return 으로 종료를 했든 안했든
# break로 try 구문을 빠져나가도 실행된다