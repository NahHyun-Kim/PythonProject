import math
from calculator import plus, minus # 다른 py 파일과 함수를 import 하여 사용
# from math import ceil, sum, fabs as floatabs (이름 변경 가능)

# 파이썬 모듈을 사용하기 위한 math import가 필요함
print(math.ceil(1.2)) # math.ceil(값을 올림하여 반환)
print(math.fabs(-1.2)) # float 형태의 절대값 반환
print(math.fabs(-7))

# 함수명을 import 하지 않는 경우는 파일명.함수로 접근
print(plus(1,2), minus(50,1))