# 거스름돈 계산기(거스름돈을 각 지폐 몇장으로 줄 지 출력)
def calculate_change(payment, cost):
    rest = payment - cost
    fives = 50000
    ones = 10000
    five = 5000
    one = 1000
    print(f"50000원 지폐 : {rest // fives}장")
    rest = rest % fives
    print(f"10000원 지폐 : {rest // ones}장")
    rest = rest % ones
    print(f"5000원 지폐 : {rest // five}장")
    rest = rest % five
    print(f"1000원 지폐 : {rest // one}장")

calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)