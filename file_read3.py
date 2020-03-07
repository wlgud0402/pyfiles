# 데이터를 한줄씩 읽어들이기
#for 한줄을 나타내는 문자열 in 파일객체:
    #처리

#이전데이터를 한줄씩 읽으면서 키와 몸무게로 BMI를 계산해보자

with open("file_info.txt", "r") as file:
    for line in file:
        #변수선언
        (name, weight, height) = line.strip().split(",")
        #데이터 문제 없는지 확인: 문제있으면 지나감
        if (not name) or (not weight) or (not height):
            continue
        #결과 계산
        bmi = int(weight) / ((int(height) / 100) **2)
        result =""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상체중"
        else:
            result = "저체중"
        #출력
        print('\n'.join([
            "이름: {}",
            "몸무게: {}",
            "키: {}",
            "BMI: {}",
            "결과: {}"
        ]).format(name, weight, height, bmi, result))
        print()