#학생을 매개변수로 받는 형태의 함수로 만듦

#딕션어리를 리턴하는 함수 선언
def create_student(name, korean, math, english, science):
    return{
        "name":name,
        "korean":korean,
        "math":math,
        "english":english,
        "science":science
    }

#학생처리 함수 선언
def student_get_sum(student):
    return student["korean"]+student["math"]+\
        student["english"]+student["science"]

def student_get_average(student):
    return student_get_sum(student)/4

def student_to_string(student):
    return "{}\t{}\t{}".format(
        student["name"],
        student_get_sum(student),
        student_get_average(student))

#학생 리스트 선언
students = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("연하진", 92, 98, 96, 98),
    create_student("구지연", 76, 96, 94, 90),
    create_student("나선주", 98, 92, 96, 92),
    create_student("윤아린", 95, 98, 98, 98),
    create_student("윤명월", 64, 88, 92, 92),
]

print("이름","총점","평균", sep="\t")
for student in students:
    print(student_to_string(student))