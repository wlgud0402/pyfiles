#for 반복문 딕셔너리와 사용하기   key는 딕셔너리 함수에 내장된 키워드 딕셔너리 내부의 변수로도 가능 
# name, age, hoby

dict_b = {
    "name":["김지형","김기현","이동은","김익수"],
    "age":["25","28","55","55"],
    "hoby":["singing", "coding","piano","poker"]
}


for key in dict_b:
    print(key, dict_b[key])