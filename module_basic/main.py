import test_module as test   #만든 모듈을 test. 을통해 사용하겠다는 의미이다

radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))