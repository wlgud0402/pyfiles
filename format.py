#format 함수로 숫자를 문자열로 변환                   숫자,문자,불린(True, False)도 포함
# "{}".format(10)>>>>숫자10이 문자 10으로 변화  
string_a = "{}".format(100)
print(type(string_a))

format_a = "연봉{}만원 되기".format(5000)
print(format_a)

#특정 칸에 출력하기 숫자를 통해
# output_a = "{:0~커지는만큼 먼칸에 생성d}".format(52)
# print(output_a)

#빈칸을 0으로 채우기
output_b = "{:05d}".format(52)       #>>>>>>>00052
output_c = "{:015d}".format(-52)     #>>>>>>>-0000000000052

print()
print(output_b)
print(output_c)

#기호를 뒤로 밀건나 앞으로 미는것, 음수의 경우 format()속의 수가 음수일경우에도 상관없이 {이안은 +이다}
output_d ="{:+5d}".format(52)       #기호를 뒤로밀기:양수
output_e ="{:+5d}".format(-52)      #기호를 뒤로밀기:음수      
output_f ="{:=+5d}".format(52)      #기호를 앞으로밀기:양수
output_g ="{:=+5d}".format(-52)     #기호를 앞으로밀기:음수
output_h ="{:+05d}".format(52)      #0으로 채우기:양수
output_i ="{:+05d}".format(-52)     #0으로 채우기:음수


print(output_d)
print(output_e)
print(output_f)
print(output_g)
print(output_h)
print(output_i)


