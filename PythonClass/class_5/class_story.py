class Service:
    secret = "지금 샌드위치를 2개 먹을 수 있다."

    # 사용자에게 이름을 입력받아 서비스를 제공 시 앞부분에 이름을 넣어주기 위함
    def setname(self, name):
        self.name = name

    # 서비스를 이용하고 싶다고 요청했을 때, 가입을 한 사람인지 안 한 사람인지 가리기 위해
    # sum이라는 함수의 첫번째 입력값으로 self 를 넣음(인스턴스 함수로 사용하기 위해서는 무조건 self로 지정)
    def sum(self, a,b):
        result = a + b
        print("%s님 %s + %s = %s입니다." % (self.name, a,b,result))

# class 이름은 service
# service 클래스는 인터넷 서비스 제공 업체. 가입 고객에게만 정보 제공
# 회원이 되기 위해서는
# nh라는 아이디로 Service 클래스에 가입하여 이용할 수 있음
nh = Service()

# nh라는 아이디를 가진 사람이 자신의 이름은 김나현임을 서비스 업체에 알려줌
nh.setname("김나현")

# Service 업체가 제공하는 sercret 이란 변수를 .을 통한 접근으로 얻어냄
print(nh.secret)

# sum 함수는 (self, a,b)를 파라미터로 받아 첫 번째 입력값으로 가입한 사람인지 아닌지를 판단
# (1,1)만 전달해도, 호출 시 이용했던 인스턴스인 nh로 self가 바뀌게 되어 가능하다.

# setname을 통해 '김나현'으로 설정했기 때문에, 앞으로 nh로 접근하면 이름은 김나현으로 생각
# nh라는 아이디와 이름을 연결해 주는 것이 self
nh.sum(1,1)

# 1. nh라는 아이디를 가진 사람이 nh.setname('김나현') 을 통해 setname 함수에 입력
# 2. self.name = name 문장 수행, 3. self는 첫 번째 입력값으로 nh.name = name으로 바뀜
# 4. name은 두 번째로 입력 받은 '김나현'이라는 값이므로 위의 문장은 nh.name = '김나현'으로 바뀜

