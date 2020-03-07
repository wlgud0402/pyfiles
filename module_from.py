#from구문  >>>일일이 가져오지 않고 여러가지를 한번에 가져올 수 있게함
#from 모듈이름 import 가져오고싶은 변수,함수

from math import sin,cos,tan,floor,ceil

print(sin(1))
print(cos(1))
print(tan(1))
print(floor(2.5))
print(ceil(2.5))

#앞에 math를 붙이는게 싫고 모든기능을 가져오는 것이 목적이라면 *기호를 사용합니다
#but 이렇게 할시 식별자 이름에서 충돌이 발행할 수 있습니다.
#컴퓨터 기호에서 (*) 는 '모든것' 을 의미함

#form math import*