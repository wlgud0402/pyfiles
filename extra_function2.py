#enumerate()함수

#ex) list_a = ["요소A", "요소B", "요소C"]
#ex) 0번째 요소는 요소A 입니다.
#ex) 1번째 요소는 요소 B입니다.
#ex) 2번째 요소는 요소 C입니다.

list_a = ["요소A", "요소B", "요소C"]
i = 0
for a in list_a:
    print("{}번째 요소는 {}입니다.".format(i, a))
    i += 1

print()
print()

for z in range(len(list_a)):
    print("{}번째 요소는 {}입니다.".format(z, list_a[z]))