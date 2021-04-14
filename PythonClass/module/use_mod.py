# 함수나 변수 또는 클래스를 모아 놓은 파일, 다른 파이썬 프로그램에서 불러와 사용 가능
import mod1, mod2 # mod1.py 함수를 불러옴
# from mod1 import sum, safe_sum 또는 모든 함수 import 시 from mod1 import * 로 사용 가능
print(mod1.sum(3,4))
print(mod1.safe_sum(1,'a')) # 자료형이 다른 두 수를 넘김(문구 출력), None값 반환

a = mod2.Math() # mod2 모듈에 있는 클래스를 불러옴
print(a.solv(2))
print(mod2.sum(mod2.PI,4.4))

result = mod2.sum(3,4)
print(result) # 동일한 디렉터리에 있다면, 단순 import mod2를 통해 모듈을 불러와서 사용 할 수 있음
