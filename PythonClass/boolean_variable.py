import sys
from copy import copy

# 자료형의 참과 거짓
# 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어 있으면 "", [], (), {} (숫자는 0일 때) 거짓이 됨
a = [1,2,3,4]
while a:
    print(a.pop()) # while문은 조건문이 참인 동안 문장을 반복해서 수행(a가 참인 경우 계속 수행)

if []:
    print("True")
else:
    print("False") # 비어있는 리스트(거짓 = False 출력)

if [1,2,3]:
    print("True")
else:
    print("False") # [1,2,3] 이라는 요소값이 있는 리스트(참 = True 출력)

# 파이썬에서 변수를 만들 때는 =(assignment, 할당) 기호를 사용 (자료형은 python에서 자동으로 판단)
# 변수는 파이썬에서 사용하는 객체

# 내장함수 is 를 사용하여 동일한 객체를 가리키고 있는지 판단
a = 3
b = 3
print(a is b) # 동일한 객체를 가리키고 있기 때문에, True 반환(레퍼런스 카운트는 2개)

# a,b가 같은 객체를 가리키는지 참조 개수를 알려주는 sys.getrefcount 함수 사용
# import sys 모듈 사용
print(sys.getrefcount(3))
c = 3
print(sys.getrefcount(3))
d = 3
e = 3
print(sys.getrefcount(3)) # 3을 가리키는 변수를 늘리면 참조 개수가 계속 증가함

# 변수형 만들기
a,b = ('python', 'life') # 튜플로 대입
print(a,b)

(a,b) = 'python', 'life' # 튜플은 괄호 생략 가능
[a,b] = ['python', 'life'] # 리스트로 변수 만들 수 있음
a = b = 'python' # 여러 개의 변수에 같은 값 대입 가능

# 두 변수의 값 바꾸기
a = 3
b = 5
a, b = b, a # (두 변수의 값 변경)
print(f"변경된 a의 값은 {a}이고, 변경된 b의 값은 {b}입니다.")

# 메모리에 생성된 변수 없애기(del)
# 리스트를 변수에 넣고 복사하기(a의 값이 바뀌면 b의 값이 같이 변함)
a = [1,2,3]
b = a
a[1] = 4
print(a)
print(b) # b의 값도 같이 1,4,3으로 바뀌어 출력된다(a,b 모두 같은 리스트를 가리킴)

# a와 같은 값을 가지도록 복사하면서 a가 가리키는 리스트와 다른 리스트를 가리키게 하려면?
a = [1,2,3]
b = a[:] # 전체를 가리키는 [:]를 이용하여 복사
a[1] = 4
print(a)
print(b) # 1,2,3 이 출력

# copy 모듈 이용하기(from copy import copy) 모듈 사용
b = copy(a)
print(f"copy(a)를 한 b의 값은 {b}") # b = a[:}와 동일

# 두 변수가 같은 값을 가지며 다른 객체를 제대로 생성했는지 확인하려면 is 함수 이용
print(b is a)