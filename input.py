string = input("인사말을 입력하세요")
print(string)


#input 로 받은 자료들은 숫자든 문자든 type 은 문자형으로 된다, 불린 형태도 물론 그렇게 나옴true, false
hi = input("인사해주세요")
print(type(hi))     #>>>>>>>str 문자형

number = input("원하시는숫자는?")
print(type(number))   #>>>>>>str 문자형

#그러므로 input으로 입력받은 숫자를 다른 숫자와 더학 위해서는 입력받은 문자형 형태의 숫자를 숫자형으로 변환해야함
#int()
string_a = input("입력A:")
int_a = int(string_a)

string_b = input("입력B:")
int_b = int(string_b)

print("문자형자료:",string_a + string_b)        #문자형이므로 숫자의 나열 붙임
print("숫자형자료:", int_a + int_b)             #숫자형이므로 숫자가 연산자에 의해 더해짐


#숫자를 문자형으로 변환
output_a = str(52)
output_b = str(52.234)

print(type(output_a), output_a)
print(type(output_b), output_b)