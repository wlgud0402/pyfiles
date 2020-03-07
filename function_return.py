#함수 실행중 return 을 만나면 그 함수 실행한 위치로 돌아가라는말
#함수가 거기서 종료된다

#자료 없이 리턴하기
def return_test():
    print("A위치입니다")
    return
    print("B위치입니다")

return_test()

print()
print()

#자료와 함계 리턴하기
def return_test2():
    return 100

value = return_test2()
print(value)

print()
print()

#아무것도 리턴하지 않기


