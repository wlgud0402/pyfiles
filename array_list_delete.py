#인덱스로 제거하기(요소의 위치기반으로) del, pop()
list_a = [0,1,2,3,4]
#0번째 자리를 삭제 del      [2:3] 범위삭제 또한 가능 단 3번자리 미포함
#[:3] 3번자리 전까지 왼쪽항들 모두 삭제 [3:] 3번째항 포함 오른쪽항 모두 삭제
del list_a[0]     
print(list_a)

print()

list_b = [11,22,33,44]            #pop삭제는 범위삭제가 불가능
list_b.pop(0)     #0번째 자리를 삭제 pop     pop(이안에 아무것도 안넣으면 마지막 요소를 삭제함)
print(list_b)

print()

#값으로 제거하기 remove>>>>>>>리스트.remove(값)

list_c = [7,1,3,5,7,9]    #중복된 값이 있는경우 앞쪽의 값을 삭제>>>모두제거하려면 반복문필요
list_c.remove(7)
print(list_c)

print()
#리스트 내부요소를 모두 제거하기>>>리스트.clear()
list_d = [1,2,3,4,5,6,7]
list_d.clear()
print(list_d)