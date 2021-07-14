from random import randint

# input 내장함수를 이용하여 입력 받기, input은 문자열 형태로 입력된다.
name = input("이름을 입력하세요: ") # input에 입력된 부분으로 대체됨
print("안녕하세요 " + name)

num = input("숫자를 입력하세요: ")
print(type(num)) # class 'str'으로 나옴. 형변환 필요

# 숫자형으로 (int) 형변환하여 입력받기
x = int(input("첫 번째 정수: "))
y = int(input("두 번째 정수: "))
print("두 정수의 합 : %d" % (x+y))

# 1에서 20 사이의 숫자를 맞추는 게임 만들기
randnum = randint(1, 20)
i = 4 # 총 4번의 맞출 기회를 세기 위한 변수
count = 0 # 몇 번만에 숫자를 맞추는지 횟수를 저장하기 위한 변수

while 0 <= i:
    count = count + 1

    if i == 0:
        print(f"아쉽습니다. 정답은 {randnum}였습니다.")

    usernum = int(input(f"기회가 {i}번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: "))
    if usernum == randnum:
        print(f"축하합니다. {i}번만에 숫자를 맞추셨습니다.")
        break
    elif randnum > usernum:
        print("Up")
    elif randnum < usernum:
        print("Down")
    i = i-1



