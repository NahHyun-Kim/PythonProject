# *args를 통해 무한으로 인자 전달 가능
# positional argument : 1,2,3... (*args)
# keyword argument : hello=True... (**kwargs)
def plus(a, b, *args, **kwargs):
    print(args) # tuple 형태로 출력
    print(kwargs) # keyword 형태로 출력
    return a + b

plus(1,2,1,1,1,1,23123,12, nh=True, hi=True)

# 무한 인자 계산기
def calculator(*args):
    result = 0
    for number in args:
        result += number
    print(result)

calculator(1,2,1,2,1,2,3)