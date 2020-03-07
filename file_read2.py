#텍스트 한줄씩 읽기   >>>>>CSV, XML, JSON
#CSV = Comma Separated Values    쉼표로 구분된 값

#이름, 키, 몸무게
#김지형, 177, 77

#램덤하게 1000명의 키와 몸무게 만들기
import random

hanguls = list("abcdefghijklmn")
with open("file_info.txt", "w") as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        file.write("{}, {}, {}\n".format(name, weight, height))