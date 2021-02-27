# if 조건부분(boolean 값 계산): 수행부분 기본구조
temperature = 15

if temperature <= 10:
    print("자켓을 입는다")
else:
    print("자켓을 입지 않는다")

# elif문(else-if문)
temp = 13

if temp <= 5:
    print("내복, 긴팔, 자켓을 입으세요")
elif temp <= 10:
    print("긴팔과 자켓을 입으세요.")
elif temp <= 15:
    print("긴팔을 입으세요.")
else:
    print("반팔을 입으세요.")

# 학점 계산기(절대평가 방식, 60점 미만이면 F부여)
score = 90

if score >= 90:
    print("You get an A.")
elif score >= 80:
    print("You get a B.")
elif score >= 70:
    print("You get a C.")
elif score >= 60:
    print("You get a D.")
else:
    print("You get an F.")

# 이상한 수학 문제 1(while, if문을 이용해 100이하의 자연수 중
# 8의 배수이지만, 12의 배수는 아닌 것을 모두 출력
num = 1

while num <= 100:
    # 또는 파이썬의 문법으로 i % 8 == 0 and i % 12 != 0으로 해도 된다.
    if num % 8 == 0:
        if num % 12 != 0:
            print(num)
    num = num + 1

# 이상한 수학 문제 2 (1000보다 작은 자연수 중 2 또는 3의 배수의 합을 출력)
sum = 0
undernum = 1

while undernum < 1000:
    if undernum % 2 == 0 or undernum % 3 == 0:
        sum = sum + undernum
    undernum = undernum + 1

print(sum)

# 약수 찾기(120의 약수를 모두 출력하고, 총 몇 개의 약수가 있는지 출력)
divnum = 1
divcount = 0

while divnum <= 120:
    if 120 % divnum == 0:
        print(divnum)
        divcount = divcount + 1
    divnum = divnum + 1

print(f"120의 약수는 총 {divcount}개입니다.")

# 택이의 우승상금(5000만원 12%씩 이자가 붙을 때, 아파트 vs 적금 어떤 것이 더 이득일까?)
add = 0
win = 50000000
apart = 1100000000
year = 1988

while year < 2016:
    year = year + 1
    add = win + (win * 0.12)
    win = add
    if add > apart:
        print(f"{round(add - apart)}원 차이로 동일 아저씨의 말씀이 맞습니다.")

# 피보나치 수열(20개 항 차례로 출력하는 프로그램 작성)
a = 1
b = 0

numcnt = 0

while numcnt < 20:
    print(a)
    temp = b # 값을 임시로 보관하는 temp 변수에 b 지정
    b = a # a의 값을 b로 이동
    a = b + temp # b와 temp의 값을 합친(앞, 뒤 숫자) 값을 최종값으로 a로 지정, 이를 꾸준히 출력
    numcnt = numcnt + 1
