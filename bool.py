#bool(True, False) 로 문자열도 비교할수 있다. 사전식으로 앞에오는 말일수록 작은값
print("가방">"하마")      #가방이 하마보다 앞에있으므로 더 작은값을 가진다
print("가방"<"하마")

print()
#not , and(둘다 참일때만 true) , or(둘중하나 참일때도 true)

#<not>
print(not True)   #>>>>>False
print(not False)  #>>>>>True
 
print()
x = 10
y = x<20
print("x:", y)
print("not x:", not y)