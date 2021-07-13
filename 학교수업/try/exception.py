# 오류 강제 구현
# Bird라는 클래스를 상속받는 자식 클래스는 반드시 fly 라는 함수를 구현하도록 만들고 싶다면?

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird): # Eagle 클래스는 Bird 클래스를 상속 받음
    def fly(self):
        print("very fast") # 상속받은 Bird 객체에서 반드시 fly를 구현하도록 지정해주었으므로, fly 함수 구현한다.

eagle = Eagle()
eagle.fly() # Eagle 문에서 fly를 구현하지 않은 경우, Bird 클래스의 fly가 호출된다.
# eagle 함수에서 fly 함수를 구현하지 않았기 때문에, Traceback.. NotImplementedError가 발생함
# 오류 발생을 방지하려면, Eagle 클래스에도 fly 함수를 반드시 구현해야 함.

