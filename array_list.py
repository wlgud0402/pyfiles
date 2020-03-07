array = [123, 32, 25, "안녕하세요", True, False]
print(array)
#자리대로 출력
print(array[0])
print(array[-1])
print(array[1:3])

print()
#변경, 추가
array[0] = "변경"
print(array[0])

#리스트안 항목의 자리수 출력, 리스트속 리스트
print(array[0][0]) #>>>>>변경이라는 항목의 0번째자리에 있는걸 출력

lists = [[1,2,3,], ["안녕", "hello"], [33,28,"공부"]]
print(lists[0][1])   #>>>>>lists속의 0번째 리스트 [1,2,3] 출력 그후 1번째에 있는 2를 출력

