#__str__()을 클래스 내부에 정의함
#>>>str()함수를 호출할때 __str__()함수가 자동으로 호출됨

class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4
    
    def __str__(self):                  #__str__()라는 이름으로 함수선언
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average())
    
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92),
]

print("이름","총점","평균", sep="\t")
for student in students:
    print(str(student))          #str()함수의 매개변수로 넣어서 student __str__()호출