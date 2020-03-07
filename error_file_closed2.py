#파일처리 중간에 에외 발생

try:
    file = open("info.txt", "w")
    예외.발생합니닷()
    file.close()
except Exception as e:
    print(e)

# finally:
#     file.close()  >>>예외가 발생해서 파일을 닫지 않게되도 finally를 넣으면 무조건 닫기 가능
#finally 를 쓰지않고 마지막쪽에 file.close()를 써서 닫는것도 가능
print(file.closed)