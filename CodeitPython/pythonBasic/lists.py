# 여러 개의 값을 저장하고자 할 때는 list 사용
numbers = [1, 2, 3, 4, 5, 6]
names = ["나현", "영하"]

# 배열의 전체 값 출력
print(numbers)
print(names)

# 일부 요소를 출력하고 싶을때는 배열의 indexing 사용
print(numbers[0] + numbers[1]) # 배열 인덱스는 0부터 시작함.

# 마이너스(-) 인덱스 존재 (index-1 = 마지막 값...)
# 배열의 길이가 6까지인 인덱스의 범위는 0에서 5까지, -1에서 -6까지
print(numbers[-1]) # 제일 마지막 값 출력
print(numbers[-6]) # 제일 첫번째 값 출력

# 리스트 슬라이싱(0~4지만 index 3까지를 뜻함. 즉 1,2,3,4 출력)
print(numbers[0:4])
print(numbers[2:]) # 뒤의 숫자 표기가 없으면, 인덱스의 마지막 요소까지 리턴됨
print(numbers[:3]) # 처음부터 0,1,2번째 수가 리턴됨

# 리스트 변경
numbers[0] = 7
print(numbers) # 0번째(1)의 자리에 7을 넣어, 7,1,2,3,4,5,6 출력

numbers[1] = numbers[0] + numbers[1] # 2의 자리에 7+2을 대입하여 9 출력
print(numbers)
# 리스트 함수 1(길이 len, 요소 추가 append : 맨 뒤에만 요소 추가)
print(len(numbers))

funcnumbers = []
print(len(funcnumbers)) # 전체 함수의 길이 출력(현재 0)
funcnumbers.append(5) # funcnumbers의 끝에 정수 5를 넣으라는 함수
funcnumbers.append(8)
funcnumbers.append(9)
print("리스트의 길이는: %d" % len(funcnumbers))

# 리스트 함수 2(제거 del, 원하는 자리에 요소 추가 insert)
del funcnumbers[1] # funcnumbers의 두번째 값 제거
print(funcnumbers)
    # del numbers[4:] 인덱스 4부터 마지막까지 삭제할 것
funcnumbers.insert(1, 2) # index 0 자리에 정수 1을 넣어줄 것
print(funcnumbers)

# 리스트 함수 3(정렬 sorted 연결 +)
print(sorted(funcnumbers)) # 순서대로 정렬된 list를 리턴
numhap = numbers + funcnumbers
print(f"numbers 리스트와 funcnumbers 리스트의 전체 요소는 {numhap} 입니다.")
    # sorted 함수는 문자열도 정렬이 가능함(숫자->영문 알파벳...)

# while문을 활용하여 list에 원소 넣기
j = 1
list = []
while j <= 10:
    list.append(j)
    j = j + 1

print(list)

# 리스트에서 값의 존재 확인하기
# value가 list의 요소인지 확인
def in_list(some_list, value):
    i = 0
    while i< len(some_list):
        # some_list에서 value를 찾으면 True를 리턴
        if some_list[i] == value:
            return True
        i = i + 1

    # 만약 some_list에서 value를 찾지 못했으면 False를 리턴
    return False

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(in_list(primes, 7)) # primes 리스트 안에 값이 있으므로 True 리턴
print(in_list(primes, 12)) # primes 리스트 안에 값이 없으므로 False 리턴

# 그러나, 리스트의 값 확인은 자주 있는 부분이라 기본적인 파이썬 기능으로 내장되어 있음
# in 이라는 키워드를 통해 (val in 리스트)
print(7 in  primes) # primes 리스트 안에 7이 있는가? (True)
print(15 in primes) # primes 리스트 안에 15가 있는가? (False)

# 없는지 확인 = not in
print(7 not in primes) # 7이 있으므로 False
print(16 not in primes) # 16이 없으므로 True

# 리스트 안의 리스트(Nested List)
# 세 번의 시험을 보는 수업
grades = [[90, 95, 100], [78, 89, 92] , [85, 91, 100]]

print(f"첫 번째 학생의 성적은 {grades[0]}점 입니다.")
print(f"세 번째 학생의 성적은 {grades[2]}점 입니다.")
print(f"첫 번째 학생의 첫 번째 과목 성적은 {grades[0][0]}점 입니다.")

firstavg = round(((grades[0][0] + grades[1][0] + grades[2][0]) / 3),2)
print(f"첫 번째 시험 성적의 평균은 {firstavg}점 입니다.")

# sorted 함수는 정렬된 새로운 리스트를 리턴하나,
# 기존의 list에서 정렬을 해 주는 sort함수
numbers = [5, 3, 7, 1]
numbers.sort()
print(f"sort() 함수로 정렬된 numbers의 원소는 {numbers}입니다.")

# reverse 메소드(뒤집어진 순서로 배치)
numbers.reverse()
print(f"reverse() 함수로 뒤집은 numbers의 원소는 {numbers}입니다.")

# index 메소드(list에서 지정한 value값을 가지고 있는 원소의 인덱스를 리턴)
members = ["나현", "영하", "하람"]
print(members.index("영하")) # "영하"가 위치한 1 리턴(0,1,2 중)
print(members.index("나현")) # "나현"이 위치한 0 리턴(0,1,2 중)

# remove 메소드(list에서 첫 번째로 value값을 가지고 있는 원소를 삭제)
# del 리스트[인덱스] 에 위치한 원소 삭제 / remove는 리스트.remove(원소의 값)
fruits = ["딸기", "딸기바나나", "깊은속바닷속파인애플", "파인애플", "수박", "멜론"]
fruits.remove("깊은속바닷속파인애플")
fruits.remove("딸기")
print(fruits)