#아무것도 없는 딕셔너리에 값 추가하기
dict_a = {}
dict_a["name"] = "새로운이름"
dict_a["head"] = "새로운정신"
dict_a["body"] = "새로운 몸"

print(dict_a)
print()
#딕셔너리 내부에 키가 있는지 확인하기 in, get()
key = input(">접근하고자 하는 키")

if key in dict_a:
    print("키가 존재합니다")
else:
    print("키가 존재하지 않습니다")
print()
print()

value = dict_a.get("name")
print("키의 값: ", value)
#키가 없으면 None 라고 출력되므로
if value == None:
    print("키가 존재하지 않습니다")


value = dict_a.get("age")
print("키의 값: ", value)
if value == None:
    print("키가 존재하지 않습니다")

