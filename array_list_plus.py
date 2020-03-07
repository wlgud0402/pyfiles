#리스트 연산자, 리스트 길이구하기
list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(list_a + list_b)

print()

print(list_a *3)

print(len(list_a))

print()
#리스트에 요소 추가하기 append(맨뒤에 추가), insert(위치지정할수 있음)
list_a.append(7)    #list_a 의 맨끝에 7을 추가
print(list_a)

print()
list_b.insert(1, 9)    #list_b의 1번째 자리에 9를 추가   
print(list_b)

list_c = [55,22,33]    #insert는 그자리에 새로운 값을 추가하지만 []=은 그자리원래 있던값에 덮어씌움
list_c[0] = 11
print(list_c)

#extend 리스트의 뒤에 새로운 리스트의 요소를 모두 추가
list_c.extend([9,2,3])
print(list_c)