# 함수 안에서 선언된 변수의 효력 범위
# def vartest(a)에서 입력 인수를 뜻하는 변수 a는 함수 안에서 사용되는 변수임.
a = 1
def vartest(a):
    a = a + 1

vartest(3) # vartest의 입력값으로 3을 주고,
print(a) # a를 출력하면 1이 나온다.(변수의 scope - a+1이 아닌 1 출력)

def vartest2(a):
    a = a+1

print(vartest(a)) # None 출력(vartest 함수 내의 a는 3+1=4가 되지만
# print(a) 에러 발생 - 함수 안에서만 사용되는 a이기 때문에 함수 밖에서는 사용되지 않음

# 함수 밖의 변수를 변경하는 방법(vartest 함수 이용)
a = 1
def vartest3(a):
    a = a + 1
    return a

a = vartest3(a)
print(a) # vartest(a) 의 값을 a에 대입하여 출력 가능(함수 안의 a변수와 밖의 a변수는 여전히 다름)

# global 명령어 이용
# global a라는 문장은 함수 안에서 함수 밖의 a 변수를 직접 사용하겠다는 의미
# 함수는 독립적으로 존재하는 것이 좋기 때문에 프로그래밍을 할 때 global 명령어는 사용하지 않는 것이 좋음

# def vartest():
# global a
# a = a+ 1
# vartest()
# print(a)

