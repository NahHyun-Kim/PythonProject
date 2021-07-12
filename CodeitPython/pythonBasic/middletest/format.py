print("{{and}}".format())
print("{0:=<10}".format("hi")) # 왼쪽 정렬 후 나머지 공백에 =로 채움
print("{0:10.4f}".format(3.12313)) # 4자리, 총 10자리, 오른쪽으로 붙어서 표현
[a,b] = ['python', 'life']
print([a,b])

treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d 번 찍었습니다. " % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

a = range(1, 11)
print(a)
