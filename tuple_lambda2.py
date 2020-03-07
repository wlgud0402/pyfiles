#map()함수와 filter()함수    map(함수, 리스트)   filter(함수, 리스트)
#map함수는 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트를 구성해주는 함수이다
#filter함수는 리스트의 요소를 함수에 넣고 리턴된 값이 True 인 것으로, 새로운 리스트를 구성
#map 함수는 수식,,,,, filter 함수는 범위를 넣을때 사용함

#함수선언
def power(item):    #power()함수= 값을 제곱해줌
    return item * item
def under_3(item):
    return item<3
#변수선언    
list_input_a = [1,2,3,4,5]
#map()함수 사용
output_a = map(power, list_input_a)
print(output_a)    #제너레이터
print(list(output_a))

output_b = filter(under_3, list_input_a)
print(list(output_b))
