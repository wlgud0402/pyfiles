#items() 함수사용
list_a = {
    "이름" : "김지형",
    "나이" : 25,
    "직업" : "학생"
}
print(list_a)

print()
#item()함수 결과 출력
print(list_a.items())

print()
#for 반복문과 item()사용

for key, element in list_a.items():
    print("{} : {}".format(key, element))