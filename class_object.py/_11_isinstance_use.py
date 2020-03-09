#isinstance함수 활용>>하나의 리스트로도 여러종류의 데이터를 다룰 수 있다.

class Student:
    def study(self):
        print("공부를 합시다")

class Teacher:
    def teach(self):
        print("학생을 가르칩니다")

classroom = [Student(),Student(),Teacher(),Student(),Student()]

for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()