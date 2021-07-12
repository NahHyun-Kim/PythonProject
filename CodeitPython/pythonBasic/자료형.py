# 숫자형
# 덧셈, 뺄셈, 곱셈, 나머지(%), 거듭제곱(**), 소수형은 정수형보다 더 쎄다(나눗셈은 항상 소수형)
print(7 % 3) # 7을 3으로 나눈 나머지 구하기
print(2 ** 3)

# floor division (버림 나눗셈)
print(8.0 // 3) # 둘 중 하나가 소수형이면 둘다 소수형, 버림 나눗셈(2 출력)
print(round(3.14234234, 2)) # 정수로 반올림(round), 자릿수 지정(소수 둘째까지)

# String 문자열
name = "김나현"
print(name * 3)
# "" 안에 '나 "를 사용해야 할 경우 : (\)역슬래시 사용
print("my name is NH. I\'m 24 years old")

# 형 변환(Type Conversion)
print(int(3.8)) # 3 출력
print(float(3)) # 3.0
print(str(2) + str(5)) # 25 출력(문자열로 변환된 2+5 연결)
age = 24
print("제 나이는" + str(age) + "살 입니다.") # 그냥 int형으로 붙일 경우 오류

# format 메소드를 이용해 문자열 포맷팅하여 편리하게 출력
year = 2021
month = 2
day = 29
# 출력할 문자열 틀 잡기 (or 변수에 String 값을 넣은 후, .format 메소드 이용)
date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year, month, day + 1))

# {}안에 0,1,2와 같이 숫자를 지정하여 출력순서를 지정 가능 (순서 : .2f와 같이 포맷형식 표현)
num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1/num_2))

# formating 방식 - 2 (f-string) python 3.6버전부터 출시
my_name = "김나현"
my_age = 24
print(f"제 이름은 {my_name}이고 {my_age}살입니다.")


# 불 대수(진리값 true / false)
# and연산(논리곱, x,y 모두 참일때만 참) , or연산(논리합, x,y 하나만 참이면 참)
print(True and True)
print(False and True) # and연산(소문자 and)
print(False or True)
print(False or False) # or연산(소문자 or)
print(not True) # true를 false, false를 true로
print(2 == 2) # ==등호, != 같지 않다
print("Hello" != "Hello")
x = 3
print(x > 4 or not(x == 3 or x == 4))

#type 함수를 통해 자료형 확인
print(type(3)) # <class 'int'>
print(type("3")) # <class 'str'>

def hello2():
    print("Hello World")
print(type(hello2)) # <class 'function'>
print(type(print)) # <class 'builtin_function_or_method'> 내장함수