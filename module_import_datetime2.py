import datetime
now = datetime.datetime.now()

#시간 처리하기

#특정시간 이후구하기   timedelta()
after = now + datetime.timedelta(\
    weeks=1,\
    days=1,\
    hours=1,\
    minutes=1,\
    seconds=1)
print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))

print()
#특정시간요소 교체하기replace() 주로 년에 쓴다 WHY? timedelta() 로는 년을 할 수 없으므로 
output = now.replace(year=(now.year +1))
print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))

