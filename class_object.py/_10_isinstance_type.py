#isinstance()함수와 type()함수의 차이

class Human:
    def __init__(self):
        pass
class Student(Human):
    def __init__(self):
        pass

student =Student()

print(isinstance(student, Human))
print(type(student) == Human)
#Student 클래스는 Human 클래스를 상속받아서 만들었다
#isinstance 함수는 이러한 상속관계까지 확인, type함수는 상속관계 확인X