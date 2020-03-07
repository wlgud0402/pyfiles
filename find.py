#문자열 찾기[위치] find()왼쪽부터 찾음     rfind()오른쪽부터 찾음

a = "안녕안녕하세요".find("안녕")     #>>>>>>>>>>>
print(a)
print()
b = "안녕안녕하세요".rfind("안녕")     #<<<<<<<<<<<<
print(b)


#in 연산자
print("안녕" in "안녕하세요") #>>>>>TRUE
print("잘자" in "안녕하세요") #>>>>>FALSE
