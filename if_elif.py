#세개 이상의 조건을 연결하는것 >>>elif   if조건문과 else 구문 사이에 입력한다
# if 조건A:
#     조건A가 참일때 실행
# elif 조건B:
#     조건B가 참일때 실행
# elif 조건C:
#     조건C가 참일때 실행
#     .
#     .
#     .
# else:
#     모든조건이 거짓일때 실행

import datetime
now = datetime.datetime.now()
month = now.month

if 3<= month <=5:
    print("현재는 봄입니다")
elif 6<= month <=8:
    print("현재는 여름입니다")
elif 9<= month <=11:
    print("현재는 가을입니다")
else:
    print("현재는 겨울입니다")


