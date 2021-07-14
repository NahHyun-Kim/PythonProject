def square(x):
    print("함수 시작")
    return x * x
    print("함수 끝") #return문 : 함수종료 + 값 돌려주기(dead code)

print(square(3))

def print_square(x):
    print(x * x)

def get_square(x):
    return x * x

# return 문이 없으면 none이라는 값으로 돌려줌
print(print_square(3))

# 옵셔널 파라미터 (기본값을 설정해두어, 함수 호출 시 파라미터에 해당되는 값을 넘기지 않았을 경우 파라미터는 기본값을 가짐)
def myself(name, age , nationality = "한국"):
    print("내 이름은 %s" % name)
    print("내 나이는 %d살" % age)
    print("국적은 %s" % nationality)
myself("코드잇", 1) # 기본값이 설정된 파라미터를 바꾸지 않으면, "한국" 값이 출력된다.
myself("코드잇", 1, "미국")

# Syntatic Suger(간략한 표현)
# x = x + 1 (x += 1), x = x % 7 (x %= 7)...

# scope(범위) : 로컬변수(함수 내에서만 사용 가능), 글로벌 변수(모든 곳에서 사용 가능)
def my_function():
    x = 3
    print(x)

my_function()
# print(x)를 이 위치에서 할 시, 함수 내에서 정의한 변수(로컬 변수)기 때문에 오류 발생
# 파라미터도 일종의 로컬변수로 볼 수 있음 / 함수에서 로컬변수 먼저 찾고 + 없으면 전역변수를 이용함

def is_evenly_divisible(number):
    if(number % 2 == 0):
        msg = True
    else:
        msg = False
    return msg
# or return number % 2 == 0만 주어 true or false를 출력 가능

print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))