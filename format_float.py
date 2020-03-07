#format 부동소수점 실수, float자료형 출력 강제>>{:f}
output_a = "{:f}".format(52.273)    
output_b = "{:15f}".format(52.273)      #15칸만들기
output_c = "{:+15f}".format(52.273)     #15칸만들고 부호추가
output_d = "{:+015f}".format(52.273)    #15칸만들고 부호추가, 0으로 채우기

print(output_a)
print(output_b)
print(output_c)
print(output_d)

#소수점아래 자리수 지정, 이때 자동으로 반올림 일어남
output_e = "{:15.3f}".format(52.273)     #52.273
output_f = "{:15.2f}".format(52.273)     #52.27
output_g = "{:15.1f}".format(52.273)     #52.2

print(output_e)
print(output_f)
print(output_g)

#의미없는 소수점 제거 0과 0.0을 합치기 {:g}
side_number_a = 52.0
side_number_b = "{:g}".format(side_number_a)

print(side_number_a)           #52.0
print(side_number_b)           #52