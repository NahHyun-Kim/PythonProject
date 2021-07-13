# 지불한 금액 payment, 물건의 가격 cost(거스름돈 계산기)
def calculate_change(payment, cost):
    # 거스름돈 계산에 필요한 변수 설정
    fives = 50000
    ones = 10000
    five = 5000
    one = 1000
    result = payment - cost

    print(f"50000원 지폐 : {result // fives}장") # 버림 나눗셈 연산자 //로 지폐 장수 구하기
    result = result % fives # 나누고 남은 나머지값(%)이 result가 됨
    print(f"10000원 지폐 : {result // ones}장")
    result = result % ones
    print(f"5000원 지폐 : {result // five}장")
    result = result % five
    print(f"1000원 지폐 : {result // one}장")

calculate_change(100000, 33000)


# 짝수? 홀수? (짝수이면 True, 홀수이면 False 리턴)
def is_evenly_divisible(number):
    if (number % 2 == 0):
        msg = True
    else:
        msg = False
    return msg

print(f"짝수면 True, 홀수면 False : {is_evenly_divisible(3)}")
