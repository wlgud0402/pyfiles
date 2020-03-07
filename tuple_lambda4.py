#인라인 람다 >>>>람다를 함수의 매개변수에 바로 넣음
list_input_a = [1,2,3,4,5]

output_a = map(lambda x:x*x, list_input_a)
print(list(output_a))

output_b = filter(lambda x:x<3, list_input_a)
print(list(output_b))