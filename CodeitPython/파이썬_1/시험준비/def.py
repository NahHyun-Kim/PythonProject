def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    print(args) # *args 값을 모두 받아 변수에 튜플 형태로 담음
    return sum

print(sum_many(1,2,3,5,8))

def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result = result + i #args에 입력 받은 모든 값을 더함
    if choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = sum_mul("mul",1,2,3,4,5)
print(result) # choice가 mul로 전달되어, 모든 args 변수를 곱한 값 반환


def sum_and_mul(a,b):
    return a+b, a*b # 함수는 하나의 결과값을 반환하는데, 이 경우 튜플로 묶어서 하나의 결과로 리턴(7, 12)

result = sum_and_mul(3,4)
print(f"sum_and_mul의 실행 결과는 : {result}")

def say_yh(yh):
    if yh=="바보":
        return
    print("나의 별명은 %s입니다." % yh)

say_yh("바보") # 조건에 해당되기 때문에, return을 만나 빠져나옴