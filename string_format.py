# 문자열 포매팅(문자열 내 특정 값 삽입)
# 1. 숫자 바로 대입
print("I eat %d apples" % 3) # 숫자를 넣고 싶은 자리에 %d, % 뒤에 넣을 숫자(%d : 포맷 코드)

# 2. 문자열 바로 대입
print("I eat %s apples." % "five") # 문자열 내의 또 다른 문자열 삽입은 %s 사용

# 3. 숫자/문자 값을 나타내는 변수로 대입
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days" % (number, day))

# 포매팅 코드(%s : 문자열, %c : 캐릭터, %d : 정수 , %f : 부동 소수, %o : 8진수, %x : 16진수, %% : Literal %)
# %s 포맷 코드는 어떤 형태의 값이든 변환해서 넣을 수 있음 (자동으로 문자열 형태로 바꿔서 출력)
print("rate is %s" % 3.234)
print("Error is %d%%" % 98) # Literal %%

# 1. 포맷 코드를 이용한 정렬과 공백
