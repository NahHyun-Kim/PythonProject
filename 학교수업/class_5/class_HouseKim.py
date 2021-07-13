class HouseKim:
    lastname = "김" # HousePark 클래스에 의해서 생긴 인스턴스 nh와 yh 모두 lastname이 김으로 설정
    def __init__(self, name):
        # nh.lastname은 클래스 변수로 항상 '김'을 갖기 때문에, 김나현이 출력됨.
        self.fullname = self.lastname + name
    def travle(self, where):
        # self와 장소를 받아 여행지를 출력
        print("%s, %s 여행을 가다." % (self.fullname, where))
    def kind(self, other):
        print("%s, %s 친하네" % (self.fullname, other.fullname))
    def __add__(self, other): # self + 다른사람
        print("%s, %s 친하네" % (self.fullname, other.fullname))
    def __sub__(self, other): # self - 다른사람을 호출시, 함수 실행
        print("%s, %s 싸웠네" % (self.fullname, other.fullname))



nh = HouseKim('나현') # nh = HouseKim() 으로 인스턴스를 만드는 순간, __init__ 이 호출되므로 name값까지 전달해야 함
yh = HouseKim('예현')
# nh.travle('제주') 오류 발생 : travle 함수도 self.fullname이라는 변수를 필요로 함
# setname 함수가 실행되지 않아 오류가 발생하므로, nh 라는 객체를 만드는 순간 setname 메소드가 동작하게 바꿈
# __init__ 메소드 사용 : 인스턴스 만드는 동시에 초기값을 줄일 수 있음(편리)

nh.travle('제주')

# 클래스의 상속? '물려받다' 라는 뜻으로 '재산으르 상속받다'라고 할때와 같은 의미

class HousePark(HouseKim): # houstKim 클래스의 모든 기능을 상속받음
    lastname = "박"
    # HouseKim 을 상속받은 객체이나, 동일한 travle이라는 메소드를 동일하게 다시 구현(메소드 오버라이딩)
    # 상속받은 HouseKim의 travle 함수와 다르게 동작되도록 처리
    def travle(self, where, day):
        print("%s, %s여행 %d일 가네." % (self.fullname, where, day))

juliet = HousePark('줄리엣')
juliet.travle('독도', 3)

# 연산자 오버로딩(Overloading)
# 연산자(+,-,*,/)를 객체끼리 사용할 수 있게 하는 기법

nh.kind(yh)
nh + yh # __add__ 함수 호출
nh - yh
