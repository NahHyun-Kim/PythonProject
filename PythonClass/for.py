# for 변수 in 리스트(튜플/문자열): 형태로 나타낸다.
test_list = ['one', 'two', 'three']
for i in test_list: # 리스트의 요소들이 차례로 i 변수에 대입된 후, print(i) 수행
    print(i)

# 튜플 형태를 이용하여 for문 사용
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last) # 튜플 상태의 각각 값이 first, last에 대입되어 계산

# 시험 성적 합불 여부 계산, 합격자에게 축하 메세지 전송
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks: # marks의 값을 순서대로 mark에 대입
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다. 축하합니다." % number)
    else: # 60점 이하인 학생인 경우 print문을 수행하지 않고 for문의 처음으로 돌아감
        continue

# range 함수
# range(0,10)의 형태로 작성할 때, 0부터 10 미만(n-1)까지의 범위를 포함하는 range 객체를 만든다.

sum = 0
for i in range(1,11):
    sum = sum + i #1부터 11-1, 10까지의 합계를 구함
print(f"1부터 10까지의 합은 {sum} 입니다.")

# 리스트 내 요소의 개수를 반환하는 len 함수를 통해 합불 여부 작성하기
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)): # 길이인 5, 01234 값 반환
    if marks[number] < 60:
        continue
    print(f"{number+1}번 학생 축하합니다. 합격입니다.")

# for와 range를 이용한 구구단
for i in range(2, 10):
    print(f"{i}단")
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}") # 한 단을 줄을 넘기지 않고 출력하고 싶으면 end=" " 사용
    print('') # 한 단이 끝나면(j의 값이 9까지 곱해지면) 공백 출력

# 리스트 안에 for문 포함하기
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)

# 리스트 내포를 이용하여 간단하게 표현 (ex. 짝수값에만 3을 곱하고 싶을 때)
# [표현식 for 항복 in 반복 가능객체 if 조건]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

print(result) # 각 숫자 값에 3을 곱한 값 반환

result = [x*y for x in range(2,10) for y in range(1,20)]
print(result)