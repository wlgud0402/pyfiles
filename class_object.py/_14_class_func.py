#class 함수 만들기
#class 클래스이름:
#   @classmethod
#   def 클래스함수(cls, 매개변수):
#       pass

#클래스 함수 호출 >>>>> 클래스이름.함수이름(매개변수)

#>>>students 라는 학생 리스트를 아예 클래스 내부에 생성,
#  학생리스트를 전부 출력하는 Student.print()를 만듦


class Student:
    count = 0
    students = []

    #클래스함수
    @classmethod
    def print(cls):
        print("--------학생목록----------")
        print("이름\t총점\t평균")
        for student in cls.students: #Student.students 도가능
            print(str(student))
        print("-------- --------- ---------")

    #인스턴스 함수
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4 

    def __str__(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())

Student("윤인성", 87, 98, 88, 95)
Student("연하진", 92, 98, 96, 98)
Student("구지연", 76, 96, 94, 90)
Student("나선주", 98, 92, 96, 92)
Student("윤아린", 95, 98, 98, 98)
Student("윤명월", 64, 88, 92, 92)

Student.print()