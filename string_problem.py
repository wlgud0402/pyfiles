#문자열 사이에 공백이 문자로 인식되는 경우를 막기 위한 해결방법
test = (
    "이렇게 입력해도 "
    "하나의 문자열로 연결되어 "
    "생성됩니다."
)
print(test)
#\n은 마지막 줄에는 붙이지 않습니닸!!!!!
number = int(input("정수입력>>"))
if number % 2 == 0:
    print(("입력한 문자열은 {}입니다.\n"
    "{}는 짝수입니다."
    ).format(number, number))
else:
    print(("입력한 문자열은 {}입니다.\n"
    "{}는 홀수입니다."
    ).format(number, number))

print()
print()








#join()함수로 리스트의 요소를 문자열로 연결한다. 단 문자열로 구성된 리스트여야함 "문자용~~~"
print("--".join(["1","3","5","7","9"]))

#join()함수를통해 \n 을 문자열 사이사이에 한번에 추가해줄수 있다

number2 = int (input("정수입력>>>"))

if number2 % 2 == 0:
    print("\n".join
    (["입력한 문자열은 {}입니다",
    "{}는 짝수입니다."])
    .format(number2, number2))
else:
    print("\n".join
    (["입력한 문자열은 {}입니다",
    "{}는 홀수입니다."])
    .format(number2, number2))
    