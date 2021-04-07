# 사칙연산 클래스 만들기

# a = FourCal() a라는 객체를 만들고, a.setdata(4,2) 로 지정, print(a.sum()) 으로 함수 실행 과같은 형태

class FourCal:
    # 입력하지 않고, a = FourCal() 을 변수에 지정하여 type(a)로 확인하면 class '_main_.FourCal 로 나옴 -> 객체 a의 타입은 FourCal 클래스
    # 클래스 함수, method
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        # a.sum과 같은 형태로 입력 시 a가 첫 번째 입력 인수로 들어감, 이미 first 와 second 지정되어서 그 값을 더함
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


a = FourCal()
a.setdata(4,2) # FourCal 클래스의 setdata 메소드 호출, 첫 번째 인수에는 자동으로 a라는 인스턴스가 입력
# self의 값을 입력하지 않더라도, self에는 객체가 대입 setdata(a, 4, 2) 가 전달됨
# FourCal.setdata(a,4,2) 의 형태처럼 객체 a를 입력 인수로 직접 넣는 방법도 있음(잘 사용하지는 않음)
# self.first = 4, self.second = 2가 되며, self는 a 객체이므로 a.first, a.second에 값 지정

print(a.first)
print(a.second)

b = FourCal()
b.setdata(3,7)
print(b.first) # b객체의 first 변수에 값을 대입하더라도, a와 b는 다른 객체기 때문에 값이 변경되지 않음
print(b.second)

print(f"a 객체에서 4,2를 전달한 sum 함수의 실행 결과는 {a.sum()} 입니다.")
print(f"b 객체에서 3,7을 전달한 sum 함수의 실행 결과는 {b.sum()} 입니다.")

print(a.mul())
print(b.mul())