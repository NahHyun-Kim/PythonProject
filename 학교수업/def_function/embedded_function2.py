# filter 함수 : 첫 번째 인수로 함수이름, 두번째 인수로 차례로 들어갈 반복 가능한 자료형
# 두 번째 인수인 반복 가능한 자료형 요소들이 함수에 입력되었을 때, 리턴값이 참인 것만 묶어서 돌려줌
def positive(numberList):
    result = [] # 리턴값이 참인 것만 걸러내서 저장할 변수
    for num in numberList:
        if num > 0:
            result.append(num) # num이 0보다 클 때 리스트에 추가
    return result

print(positive([1, -3, 2, 0, -5, 6]))

# --> filter 함수를 이용하여 간단하게 작성
# 함수에 입력되었을 때, 리턴값이 참인 것만 묶어서 돌려줌
def filterpositive(x):
    return x > 0

print(list(filter(filterpositive, [1, -3, 2, 0, -5, 6])))


# hex(x) : 정수값을 입력 받아 16진수로 변환하여 리턴하는 함수
hexnum = hex(234)
print(f"hexnum : {hexnum}") # 234를 16진수 형태인 0xea 형태로 반환하여 출력함


# id(object) : 객체를 입력 받아 객체의 고유 주소값(레퍼런스)를 리턴하는 함수
# 셋 다 같은 객체를 가리키고 있기 때문에, 같은 고유 주소값 출력됨.
a = 3
print(id(3))
print(id(a))
b = a
print(id(b))

print(f"id(4)를 출력할 경우, 다른 객체이므로 다른 고유 주소값인 {id(4)}이 출력된다.")


# input([prompt]) : 사용자 입력을 받는 함수. 입력 인수로 문자열을 주는 예시
# a = input() # 사용자가 hi를 입력할 경우, 그 정보를 변수 a에 저장
# b = input("Enter String : ")


# int(x) : 문자열 형태의 숫자나, 소수점이 있는 숫자들을 정수 형태로 리턴하는 함수
print(int('3'))
print(int(3.4)) # 모두 3 출력

# int(x, radix) : radix 진수로 표현된 문자열 x를 10진수로 변환하여 리턴함
print(f"int('11', 2) --> 2진수로 표현된 11을 10진수로 바꾸어 출력 : {int('11', 2)}") # 2진수 11을 10진수 3으로 나타낸다.
print(f"int('1A','16')  --> 16진수로 표현된 1A를 10진수로 바꾸어 출력 : {int('1A', 16)}")


# isinstance(object, class) : 인스턴스, 클래스 이름을 받아 입력받은 인스턴스가 그 클래스의 인스턴스인지를 판단
# ex) Person클래스에서 a인스턴스를 생성할 때, isinstance(a, Person) 형태로 입력
# a는 (1번째 인수) --> Person (2번째 인수)의 인스턴스인가 ? True
class Person : pass # 테스트를 위해 아무 기능이 없는 Person 클래스 생성
a = Person()
print(f"a is instance of Person ? : {isinstance(a, Person)}")
b = 3
print(isinstance(b, Person)) # False출력. b는 Person의 인스턴스가 아니다.


# lambda : 함수를 생성할 때 사용하는 예약어로(=def)와 같다. 한 줄로 간결하게 함수를 만들 때 사용
sum = lambda a,b : a + b # 간단하게 함수 생성
print(sum(3,4))
# 리스트 각각의 요소에 lambda 함수를 만들어 바로 사용할 수 있다.
myList = [lambda  a,b:a+b, lambda a,b:a*b]
print(f"List에 담은 함수 둘 : {myList}")
print(f"myList[0](3,4) --> myList에 담긴 첫번째 lambda함수를 (3,4)를 인수르 받아 실행 : {myList[0](3,4)}")
print(myList[1](3,4)) # 두번째 myList에 담긴 lambda함수(return a*b)를 싫행


# len(s) : 입력값 s의 길이(요소의 전체 개수)를 리턴
print(len("python"))
print(len([1,2,3]))
print(len((1,'a'))) # 튜플 형태로 된 (1, 'a')의 요소의 개수(2)를 반환


# list(s) : 반복 가능한 자료형 s를 받아 리스트로 리턴하는 함수
print(list("python"))
print(list((1,2,3)))
a = [1,2,3]
b = list(a)
print(b)


# map(f, iterable) : 함수 f와 반복 가능한 iterable 자료형을 입력으로 받음
# 입력 받은 자료형의 각 요소가 함수 f에 의해 수행된 결과를 묶어서 리턴하는 함수
def two_times(x): return x*2
# 리스트의 첫 번째 요소인 1이 two_times 함수의 입력값으로 들어가고, 1*2의 과정을 거쳐 2가 됨(반복)
print(f"list(map(two_times, [1,2,3,4]) : {list(map(two_times, [1,2,3,4]))}")
# 한 줄로 작성(lambda식 사용 + map으로 호출)
print(list(map(lambda a: a*2, [1,2,3,4])))
print(list(map(lambda a: a+1, [1,2,3,4,5])))


# max(iterable) : 인수로 반복 가능한 자료형을 입력 받아 그 최대값을 리턴하는 함수
print(f"max value : {max([1,2,3])}")

# min(iterable) : 인수로 반복 가능한 자료형을 입력 받아 그 최소값을 리턴하는 함수
print(min("python"))


# open(filename, [model]) : 파일이름, 읽기 방법을 입력 받아 파일 객체를 리턴
# w(쓰기 모드), r(읽기 모드), a(추가 모드), b(바이너리 모드), ex) "rb" : 바이너리 읽기 모드


# ord(c) : 문자의 아스키 코드 값을 리턴하는 함수
print(f"ord('a') : {ord('a')}")
print(f"ord('0') : {ord('0')}")


# pow(x,y) : x의 y제곱 결과값을 리턴하는 함수
print(f"pow(2,4)는 2의 4제곱이다 : {pow(2,4)}")
print(pow(3,3)) # 3의 3제곱, 3*3*3과 같다.


# range([start,]stop[,step]) : for 문과 함께 자주 사용되는 함수
# range 함수 - 1) 인수가 하나일 경우(시작 숫자를 지정해주지 않으면 0부터 시작함)
print(f"range 함수의 시작 숫자를 지정하지 않으면, 0부터 n-1까지 반환된다. {list(range(5))}")
# range 함수 - 2) 인수가 2개일 경우(시작 숫자, 끝 숫자를 지정이며 n-1까지 반환된다.)
print(list(range(5,10)))
# range 함수 - 3) 인수가 3개일 경우(시작 숫자, 끝 숫자, 숫자 사이의 거리-step)
print(f"range(l,10,2)는 1부터 n-1인 9까지 숫자 안에서, 2씩 증가한다는 뜻이다. {list(range(1,10,2))}")
print(list(range(0, -10, -1)))


# sorted(iterable) : 입력값을 정렬한 후, 그 결과를 리스트로 리턴하는 함수
print(f"sorted([3,1,2] : {sorted([3,1,2])}") # 입력값을 순서대로 정렬하여 리턴한다. 알파벳도 정렬이 가능함(a~z)
print(sorted("zero"))

# 리스트 자료형의 sort와 차이점? : 객체 자체를 정렬할 분, 정렬 결과를 리턴하지는 않는다.
# sorted 함수와 리스트 자료형의 sort 함수의 차이점 확인!
a = [3,1,2]
result = a.sort()
print(result) # none이 반환된다(객체 자체는 1,2,3 으로 정렬하나, 결과값을 반환하지 않음)
print(a) # 원래의 객체.sort 를 통해 객체가 정렬되어 저장된다.


# str(object) : 문자열 형태로 객체를 반환하여 리턴하는 함수
print(str(3))
print('hi'.upper())


# tuple(iterable) : 반복 가능한 자료형을 입력 받아 튜플 형태로 바꾸어 리턴하는 함수
# 튜플이 입력으로 들어오면 그대로 리턴함
print(tuple("abc"))
print(tuple((1,2,3))) # 튜플 함수 안에 튜플이 그대로 들어와, 튜플 자체를 리턴함.


# type(object) : 입력값의 자료형이 무엇인지 알려주는 함수
print(type("abc")) # <class 'str'> 반환
print(type([])) # [] 리스트 자료형 : <class 'list'>


# zip(iterable*) : 동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수
# 아마도 동일한 개수를 가진 자료형 사이에서 같은 번째수끼리 묶는다고 보면 될 듯 하다.
print(list(zip([1,2,3], [4,5,6])))
print(list(zip([1,2,3],[4,5,6],[7,8,9])))
print(list(zip("abc", "def")))