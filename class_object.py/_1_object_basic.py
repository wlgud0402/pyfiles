#딕셔너리로 객체를 하나하나 만듦
students = [
    {"name": "김지형", "korean":87, "math": 98, "english": 88, "science": 95},
    {"name": "이동은", "korean":92, "math": 87, "english": 75, "science": 83},
    {"name": "김익수", "korean":78, "math": 86, "english": 77, "science": 67},
    {"name": "김기현", "korean":48, "math": 77, "english": 58, "science": 95},
    {"name": "김민수", "korean":70, "math": 98, "english": 88, "science": 89},
    {"name": "장현정", "korean":90, "math": 80, "english": 84, "science": 75},
]

print("이름", "총점", "평균", sep="\t")   #\t >>문자열사이에 탭간격

for student in students:
    score_sum = student["korean"]+ student["math"]+\
        student["english"]+ student["science"]
    score_average = score_sum / 4 
    print(student["name"], score_sum, score_average, sep="\t")