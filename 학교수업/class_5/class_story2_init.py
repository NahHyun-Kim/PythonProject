class Service:
    secret = "지금 샌드위치를 2개 먹을 수 있다."

    # __init__ 함수 사용
    def __init__(self, name):
        self.name = name

    # 서비스를 이용하고 싶다고 요청했을 때, 가입을 한 사람인지 안 한 사람인지 가리기 위해
    # sum이라는 함수의 첫번째 입력값으로 self 를 넣음(인스턴스 함수로 사용하기 위해서는 무조건 self로 지정)
    def sum(self, a,b):
        result = a + b
        print("%s님 %s + %s = %s입니다." % (self.name, a,b,result))

# __init__ 함수 때문에 nh라는 아이디를 부여 받을 때 이름까지 함께 입력함
nh = Service('김나현')

# class란 인스턴스를 만들어내는 공장과도 같음
# class 이름, class 함수 여러개 선언 가능(self, 인수 1,2,..) 