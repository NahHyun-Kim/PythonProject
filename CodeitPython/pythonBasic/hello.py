# 코멘트(python에서의 주석 처리, comment)
print("hello")

# 변수 지정을 통해 데이터의 중복 표기를 줄이고, 효율성을 높일 수 있다.
burger_price = 4900
fri_price = 1490
drink_price = 1250

print(burger_price * 2) # 햄버거 2개 주문 시
print(burger_price * 3 + fri_price * 2 + drink_price * 5)

# 함수(명령을 저장) def (define으로 정의)
def hello(name): # 함수의 첫 줄을 헤더라고 부름
    print("Hello, Welcome to Codeit!")
    print(name)

hello("Nah Hyeon") # 파라미터로 들어감

# return 문
def get_square(x):
    return x * x
y = get_square(3)
print(y)
