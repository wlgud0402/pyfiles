#is instance?()>>>값으로 True,False 출력
#인스턴스가 어떤클래스 로부터 만들어졌는지 확인함
#isinstance(인스턴스, 클래스)

class Student:
    def __init__(self):
        pass

student = Student()
print("인스턴스채킹(student, Student)>>>>", isinstance(student, Student))