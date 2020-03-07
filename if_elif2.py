#elif 살짝 변화 위에서 지나치면 하위값만 검사하고 상위값은 검사를 생략
# ex) elif 4.2 <=score < 4.5    >>>>> elif 4.2 <=score

score = float(input("학점입력>"))

if score == 4.5:    #꼭 if, elif, else 가 끝나는 곳에는 :를 넣어서 끝남을 표시
    print("신")
elif 4.2 <= score: 
    print("교수님의 사랑")
elif 3.5 <= score:
    print("현체제의 수호자")
elif 2.8 <= score:
    print ("일반인")
else:
    print("인생좆망")
