# 문자열 관련 함수
# 문자의 개수를 세는 count()
name = "nahyeon"
print(name.count('n')) # 문자열에서 n이 포함된 갯수 카운팅

# 문자의 위치를 알려주는 find()
string = "Python is best choice"
print(string.find('b')) # b가 처음으로 나온 위치를 반환, 존재하지 않는다면 -1을 반환
print(string.find('k'))

# 문자의 위치를 알려주는2 index()
print(string.index('t')) # find()와 달리, 찾는 문자나 문자열이 존재하지 않는다면 오류 발생

# 문자열 삽입하는 join()
a = ","
print(a.join('abcd')) # 각각의 문자 사이에 변수 a의 값인 ','를 삽입

# 소문자를 대문자로 바꿔주는 upper(), 대문자를 소문자로 바꿔주는 lower()
print(string.upper()) # 소문자 -> 대문자(이미 대문자라면, 아무 변화도 일어나지 않음)
print(string.lower()) # 대문자 -> 소문자

# 왼쪽 공백 지우기(lstrip), 오른쪽 공백 지워주기(rstrip), 양쪽 공백 지우기(strip)
string = "    hi"
print(string.lstrip()) # 가장 왼쪽에 있는 한 칸 이상의 연속된 공백을 모두 지움(l=left)
string = "hi    "
print(string.rstrip()) # 가장 오른쪽에 있는 한 칸 이상의 연속된 공백을 모두 지움(r=right)
string = "      hi       "
print(string.strip()) # 한 칸 이상의 연속된 공백을 모두 지움

# 문자열을 바꿔주는 replace
a = "Python is hard"
replace_string = a.replace("hard", "easy")
print(replace_string)

# 문자열을 나누는 split (리스트에 하나씩 들어가며 출력)
a = "Life is too short"
split_string = a.split() # 아무 값을 넣지 않으면 공백을 기준으로 문자열을 나누어줌
print(split_string)
b = "string1, string 2"
print(b.split(","))

# 고급 문자열 포맷팅(문자열의 format 함수 이용)
number_format = "I eat {0} apples".format(3) # 문자열 {0}부분을 3으로 바꿔라
print(number_format) # I eat 3 apples. 출력
string_format = "I eat {0} apples.".format("five") # five라는 문자열로 바뀜
print(string_format) # I eat five apples. 출력

# 고급 문자열 포맷팅2(변수로 대입 가능, 이름으로 대입 가능)
number = 10
day = "three"
# 문자열의 {0}, {1}, {2}...의 순서대로 포맷팅
print("I ate {0} apples. So I was sick for {1} days.".format(number, day))
print("I ate {num} apples. So I was sick for {day} days.".format(num=10, day="three")) # 인덱스{0}와 이름{day}을 혼용해서 넣기

# 왼쪽 정렬, 오른쪽 정렬, 가운데 정렬
print("{0:<10}".format("hi")) # :<10 표현식을 통해 왼쪽 정렬 + 10을 통해 총 자릿수를 맞춤
print("{0:>10}".format("hi")) # :>10 오른쪽으로 정렬, + 10을 통해 총 자릿수를 맞춤
print("{0:^10}".format("hi")) # ^기호를 이용한 가운데 정렬

print("{0:=^10}".format("hi")) # 정렬 시 공백 문자 대신, 지정한 문자값으로 채움

# 소수점 표현하기
y = 3.42344
print("{0:10.4f}".format("y")) # 자릿수를 10으로 맞추어 표현

# {나 }와 같은 문자 표현
print("{{and}}".format())

