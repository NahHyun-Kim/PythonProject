sum = 0
for i in range(1,11):
    sum = sum + i

print(sum)

marks = [10,20,80,90]
for number in range(len(marks)):
    if marks[number] < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." % (number + 1))

for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print(' ')

a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(f"append 결과 : {result}")

result = [num * 3 for num in a]
print(f"내포 결과 : {result}")

result = [x*y for x in range(2,10) for y in range(1,10)]
print(f"리스트 내포를 이용한 구구단 : {result}")