# 파이썬에 기본으로 내장된 random 모듈 사용
from random import randint, uniform

# 변수, 함수, 클래스 등을 모아 놓은 파일,
# from 모듈파일 이름 import 불러올 함수/변수/클래스명(모두 호출 시 * 사용)

print(randint(1,10)) # 두 수 사이의 정수를 임의로 리턴
print(uniform(0, 1)) # 두 수 사이의 소수를 임의로 리턴
