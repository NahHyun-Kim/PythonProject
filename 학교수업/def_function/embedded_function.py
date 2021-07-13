# 내장 함수
# 외부 모듈과 달리 import 가 필요하지 않음(자체 내장 함수, 바로 사용 가능)

# abs(x)는 어떤 숫자를 입력 받았을 때 절대값을 돌려줌
print(abs(-1.2))

# all(x)는 반복 가능한 자료형 x를 입력 인수로 받으며, 모두 참이면 True, 하나라도 거짓이면 False 반환
res = all([1,2,3])
print(res) # 리스트 자료형 [1,2,3]은 모든 요소가 참이므로 True를 리턴
print(all([1,2,3,0])) # 0은 거짓이므로 False를 리턴

# any(x)는 all(x)의 반대로, 하나라도 참이 있을 경우 True 리턴, 모두 거짓일 때만 False 리턴
res = any([1,2,3,0])
print(res)
res = any([0,""]) # 0과 ""은 모두 거짓이므로, False를 리턴
print(res)

# chr(i)는 아스키 코드값을 입력 받아, 그 코드에 해당하는 문자를 출력함
asc_res = chr(97)
print(asc_res)
asc_res = chr(48)
print(asc_res)

# divmod(a,b)는 2개 숫자를 입력 받아서 a/b를 나눈 몫과 나머지를 튜플 형태로 리턴
res = divmod(7,3)
print(res) # 튜플 형태로 몫과 나머지 형태 반환 (2,1)

# enumerate(순서 있는 자료형)는 인덱스를 포함하는 enumerate 객체를 리턴 - for문, 위치 알려줄 때 유용
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name) # 0 body, 1 foo, 2 bar와 같은 인덱스를 달은 형태 출력

# eval(expression)은 실행 가능한 문자열을 입력으로 받아 문자열을 실행한 결과값 리턴
# 입력 받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶은 경우에 사용됨
res = eval('1+2') # 3 출력
print(res)
res = eval("'hi' + 'a'") # hia 출력
print(res)