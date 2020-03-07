#파일이 닫혔는지 확인하기
#>>>파일.closed()  >>>>>잘 닫혔으면 True 아니면 Flase 로 나온다
try:
    file = open("info.txt", "w")
    file.close()
except Exception as e:        #except 예외의 종류 as 변수로써사용할 이름:
    print(e)                  #예외가 뭔지 잘 모르겠으면 예외의 어머니 Exception 을 넣음

print(file.closed)

