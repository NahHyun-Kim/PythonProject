# 함수를 만들 때 사용하는 예약어 def 사용
# 공통 기능을 사용할 때 편리함
# 함수의 결과값을 돌려주는 return 명령어 사용

def sum(a,b):
    return a + b # sum 함수의 입력 파라미터로 a,b 2개의 값을 받으며 결과값은 더한값
print(sum(2,31))

# 입력값과 결과값에 따른 함수의 형태 1(일반적 함수-입력값, 결과값)

# 입력값과 결과값에 따른 함수의 형태 2(입력값이 없는 함수)
def say():
    return 'Hi'
a = say() # 함수 사용을 위해서는 괄호 안에 아무 값도 넣지 않음
print(a)

# 입력값과 결과값에 따른 함수의 형태 3(결과값이 없는 함수)
def sum(a,b):
    # print문은 수행할 문장에 해당하는 부분일 뿐, return 결과값이 없음 = 함수 호출시 None값 반환
    # 결과값은 오직 return 명령어로만 돌려받을 수 있음
    print("%d, %d의 합은 %d입니다." % (a,b, a+b))
a = sum(3,4)
print(a) # none 출력(결과값이 없으면 리턴값으로 None 반환)

# 입력값과 결과값에 따른 함수의 형태 4(입력값, 결과값 모두 없음)
def say():
    print('입력값과 결과값이 모두 없는 함수입니다.')
say()

# 입력값이 몇 개가 될 지 모를 때는 (*입력변수) 형태로 정의한다.
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i # *args에 입력 받은 모든 값을 더함
    return sum

print(sum_many(1,2,3,4,5))
print(sum_many(1,2,3,4,5,6,7,8,9,10))

# 문자열, 가변 인자를 동시에 받을 수 있다.
def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
        return result

result = sum_mul('sum', 1,2,3) # 'choice' == 'sum' 이면 모든 값을 더한 값 반환
result2 = sum_mul('mul',1,2,3) # elif('mul') 이면 모든 값을 곱한 값 반환
print(f"choice에 sum을 입력하면 합계값인 {result}가 출력됩니다.")
print(f"choice에 mul을 입력하면 곱한 값인 {result2}가 출력됩니다.")

# 함수의 결과값은 항상 하나
def sum_and_mul(a,b):
    # 함수는 return문을 만나는 순간 함수를 빠져나가게 됨
    return a+b, a*b

result = sum_and_mul(3,4)
print(result) # (a+b, a*b) 형태의 튜플값으로 반환

# return 문은 특정한 상황에 함수를 빠져나가고자 할 때도, 단독으로 사용해 즉시 빠져나갈 수 있음
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s입니다." % nick) # say_nick 함수에 "nick"을 입력할 경우 출력하지 않고 종료

# 입력 인수에 초기값 미리 설정(가장 맨 뒤쪽에 위치시켜야 함)
def say_myself(name, old, woman=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if woman:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("김나현", 24) # woman 변수에 입력값을 주지 않았지만, 초기값인 True 값을 반환