# 모듈 불러옴(module.py 파일에서, sum 함수를 불러와라)
# 모듈 : 변수, 함수, 클래스 등을 모아둔 파일(재사용성)
from 계산기 import sum, square

print(sum(3,5))
print(square(3))

# 파이썬에 기본으로 내장된 random 모듈 사용
from random import randint, uniform

# 변수, 함수, 클래스 등을 모아 놓은 파일,
# from 모듈파일 이름 import 불러올 함수/변수/클래스명(모두 호출 시 * 사용)

print(randint(1,10)) # 두 수 사이의 정수를 임의로 리턴
print(uniform(0, 1)) # 두 수 사이의 소수를 임의로 리턴

age = int(input("숫자를 입력하세요.")) # input 함수는 문자혈 리턴(int 등으로 형변환 필요)
print(type(age), age)