try:
    a = [273,103,52,57,100]
    number = int(input("정수입력 0~4까지"))
    print(a[number])
except Exception as e:
    if type(e) == ValueError:
        print("값에 문제가 있습니다")
    elif type(e) == IndexError:
        print("0~4까지 입력해주세요")

try:
    a = [273,103,52,57,100]
    number = int(input("정수입력 0~4까지"))
    print(a[number])
except ValueError as e:
    print("값에 문제가있습니다")
except IndexError as e:
    print("0~4까지 입력해주세요")
except Exception as e:
    print("알수없는 예외 발생!")

    # print(type(e))    >>>>>어떤종류의 예외인지 알수 있다

    # print(e)          >>>>>일어난 오류 메세지를 출력함
