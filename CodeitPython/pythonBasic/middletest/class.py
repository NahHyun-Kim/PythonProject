class HousePark:
    lastname = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travle(self, where):
        print("%s, %s 여행을 가다." % (self.fullname, where))
    def __add__(self, other):
        print("%s, %s 결혼했네" % (self.fullname, other.fullname))

class HouseKim(HousePark):
    lastname = "김"
    def travle(self, where, day):
        print("%s ")