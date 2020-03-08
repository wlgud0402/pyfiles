#클래스가 가지고있는 함수를 메소드 라고 부른다

#사용방법
# class 클래스이름:
#     def 메소드이름(self, 추가적인 매개변수):
#         pass



#클래스를 선언합니다
class Student():
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math+\
            self.english+self.science

    def get_average(self):
        return self.get_sum() / 4

    def to_string(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())

#학생 리스트 선언
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92),
]

#학생 반복
print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student.to_string())