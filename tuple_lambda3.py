#람다: 간단한 함수를 쉽게 선언하는 방법
#      lamda 매개변수: 리턴값>>>의 형태로 만듦

# (#lambda2.py와 비교)

power = lambda x:x*x
under_3 = lambda x:x<3

list_input_a = [1,2,3,4,5]

output_a = map(power, list_input_a)
print(list(output_a))

output_b = filter(under_3, list_input_a)
print(list(output_b))
