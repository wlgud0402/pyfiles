#강제종료되는것만 일단 막아보자
#잘 되는건 실행시키고 아닌건 패스 시키자>>except 구문에 pass를 넣음

list_input_a = ["52", "273", "32", "스파이", "103"]

list_number = []
for item in list_input_a:
    #숫자로 변환해서 리스트에 추가하자
    try:
        float(item)              #예외없으면 다음으로 이동  
        list_number.append(item) #예외없이 통과하면 리스트에 넣어줘!
    except:
        pass   #예외는 패스

print("{}내부에 있는 숫자는".format(list_input_a))
print("{}입니다".format(list_number))   