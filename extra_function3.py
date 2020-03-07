#enumerate() 현재 요소가 몇번째인지 알수 있게함

list_a = ["요소A", "요소B", "요소C"]

print(enumerate(list_a))   #바로적용 불가능

print(list(enumerate(list_a)))   #list로 강제 변환

#for 반복문과 enumerate()함수 조합해서 사용하기

for i, value in enumerate(list_a):
    print("{}번째 요소는 {}입니다.".format(i, value))
