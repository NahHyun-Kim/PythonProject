# 파이썬에 기본 내장된 built_in 함수 이용
age = "24"
print(type(age))

n_age = int(age)
print(type(n_age))

# 사용자 함수(새로운 함수) 정의(define)
# 파이썬은 중괄호가 아닌 들여쓰기를 통해 구간을 구분함
def say_hello():
    print("hello")

say_hello() # 함수 실행

# Function Arguments
def hello_name(who):
    print("hello", who)

hello_name("nh")

# Optional parameter
def minus(a, b=0): # b의 값이 지정되지 않을 경우, default 값으로 0을 대입
    print(a - b)

minus(2) # b의 값이 주어지지 않았으므로 b=0, 2-0 = 2 반환

# return
def p_plus(a,b):
    print(a+b)

def r_plus(a,b):
    return a + b
    print("somthing...") # 실행되지 않음(dead code - return문 후에 함수는 종료됨)

p_result = p_plus(2,3)
r_result = r_plus(2,3)

# p_result(none), r_result(return값으로 치환)
print(p_result, r_result)

def plus(a,b):
    return a - b

result = plus(b=30, a=1)
print(result)

def say_hello(name, age, are_from):
    return f"Hello {name}you are {age} years old"

hello = say_hello("nh", "24")
print(hello)