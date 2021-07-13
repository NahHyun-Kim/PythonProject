PI = 3.141592
class Math:
    def solv(self, r):
        return PI * (r ** 2) # r의 제곱을 의미함(반지름을 계산하는 클래스)

def sum(a,b):
    return a + b # 두 값을 더하는 함수

if __name__ == "__main__":
    print(PI)
    a = Math()
    print(a.solv(2))
    print(sum(PI, 4.4))