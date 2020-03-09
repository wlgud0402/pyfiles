#class변수 만들기
#class 구문 바로 아래단계에 변수 선언

#class 클래스이름:
#   클래스변수 = 값

#class변수에 접근하기
#클래스이름.변수이름


#클래스 선언
class Student:
    count = 0

    def __init__ (self, name, korean, math, english, science):
        #인스턴스 변수 초기화
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        #클래스변수설정
        Student.count += 1 
        print("{}번째 학생이 생성되었습니다".format(Student.count))

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92),
]

print()
print("현재 생성된 총 학생 수는 {}명입니다".format(Student.count))