#for 반복문

for i in range(10):      #10번 반복 하겠다는말!    여기서 is는 반복자(불특정)
    print("반복")

#for 반복자 in 반복할수 있는것:
    #코드

#리스트 요소 하나하나가 element 변수로 들ㄹ어가서 차례차례 반복후 출력
list_a = [12,45,34,78,97,34]

for element in list_a:
    print(element)

#for반복문을 문자열과 함께 사용할수도 있다
for element in list_a:
    print("숫자", element)

for comment in "안녕하세요":
    print("-", comment)