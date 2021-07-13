def safe_sum(a,b):
    if type(a) != type(b):
        print("더할 수 있는 것이 아닙니다.")
        return # None값을 반환(타입이 일치하지 않는 경우)
    else:
        result = sum(a,b) # a,b 자료형이 같지 않을때만 두 객체를 더해서 return result
    return result

# mod1.py 모듈을 만들었다면, import mod1
# print(mod1.safe_sum(3,4)와 같이 호출 (모듈명.함수명 으로 호출 가능하다)

# sum, safe_sum으로 직접 함수를 호출하고 싶을 경우 from 모듈명 import 함수로 사용
# from mod1 import sum(,다른 함수명 또는 * 로 여러개 함수 사용 가능)

# 5-2 pt 10p~
PI = 3.141492
class Math:
    def solv(self, r):
        return PI * (r ** 2) # 반지름 계산하는 클래스(반지름 제곱 * 파이값)

    def sum(a,b):
        return a + b

# 만약 다른 파일에서 import mod2를 하더라도, __name__ == "__main__"이 거짓이 되어 출력 X
if __name__ == "__main__": # 파일을 직접 실행시켰을때만 수행, 모듈을 부를때는 실행되지 않음
    print(PI)
    a = Math()
    print(a.sum(2))
    print(sum(PI, 4.4))

# a = mod2.Math(), print(a.solv(인자값)) 형태로 실행 가능능