#random모듈>>>랜덤한 값을 생성해줌
import random            
print(random.random())   #그냥 import random 했을시 random모듈의 random 을 호출해야함
                         #그러므로 print(rando())이 불가능하다

print(random.uniform(2.5,10.0))   #random float:  2.5 <=x <10.0

print(random.expovariate(1/5))    #interval between arrivals averaging 5 seconds

print(random.randrange(10))       #integer from 0 to 9

print(random.randrange(0,101,2))  #even integer from 0 to 100

print(random.choice(["win", "lose", "draw"]))   #single random element from a seq
                                                #리스트 내부요소를 랜덤하게 선택
deck = "ace two three four".split()
random.shuffle(deck)                            #shuffle a list
print(deck)

print(random.sample([10,20,30,40], k=4))               #four samples without replacement
                    #리스트 요소중에 k개를 뽑습니다
