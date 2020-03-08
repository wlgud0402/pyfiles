#인스턴스가 소멸될때 호출되는 함수 >>소멸자__del__\

class Test:
    def __init__(self, name):
        self.name = name
        print("{} -생성되었습니다".format(self.name))
    def __del__(self):  
        print("{} -파괴되었습니다".format(self.name))

test = Test("A")