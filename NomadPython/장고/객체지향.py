# class(설계도), instance
# class 안의 함수 : method
class Car():
    # wheels = 4
    # doors = 4
    # windows = 4
    # seats = 4

    # __init__ : (self): method를 호출하는 instance 자신, *args, **kwargs 인자
    def __init__(self, *args, **kwargs):
        print(kwargs) # 전달한 keyword 변수가 출력됨(ex. color, price), dictionary 자료형
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        # dictionary 자료형에서 .get을 통해 원하는 변수를 가져옴
        # kwargs에서 전달된 값이 있는 경우, color 또는 price를 전달받은 값으로 override
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")

    # override : 기존 기능 재정의
    def __str__(self):
        return f"Car with {self.wheels} wheels"

# 상속을 통해 기존 부모의 속성을 그대로 가져옴(extend)
class Convertible(Car):
    # 원하는 메소드 재정의(__init__ 포함)

    def __init__(self, **kwargs):
        super().__init__(**kwargs) # 부모 클래스 호출(super().로 부모 클래스(Car)에 접근)
        self.time = kwargs.get("time", 10)
        # __init__ 에서 정의한 color를 잃어버림(대체함)

    def take_off(self):
        return "taking off"

    def __str__(self):
        return f"Car with no roof"

class Something(Convertible):
    pass


# car class의 instance
porche = Car()
# 확장 porche.color = "Red"
# __init__ + 새로운 keyword 변수 정의 + 상속받은 클래스
porche = Convertible(color="Red", price="540$")
print(f"porche : {porche.color}, {porche.price}")

ferrari = Car()
# ferrari.color = "Yellow"
print(ferrari.color)
# print시 porche.__str__호출, 해당 함수(__str__)을 재정의하여 override


mini = Car()
# default value 출력
print(f"mini car : {mini.color}, {mini.price}")