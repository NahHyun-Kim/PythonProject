# 문자열 slice
a = "Life is too short, You need Python"
print(f"a[0] = {a[0]}")
print(f"a[-0] = {a[-0]}") # a[-0]은 a[0]과 같은 값을 가짐.
print(f"a[-1] = {a[-1]}")

print(f"a[-2] = {a[-2]}") # [-n]은 뒤에서 n번째 문자를 가리킴
b = a[0] + a[1] + a[2] + a[3]
print(b)

c = ""
for i in range(0,4):
    c = c + a[i]

print(c)

print(f"a[0:4]로 문자열 슬라이싱을 하면 {a[0:4]}") # 끝 번호는 포함되지 않음(4-1)
print(f"a[5:]의 형태로 시작 번호부터 문자열의 끝까지({a[5:]}) 뽑아낼 수 있다.")
print(a[:]) # 시작, 끝 번호 생략(전체 뽑아냄)
print(a[19:-7]) # a[19]부터 a[-8]까지를 의미(-7-1)

# 슬라이싱으로 문자열 나누기
date_weather = "20210310Sunny"
year = a[:4]
day = a[4:8]
weather = a[8:]

# 문자열 형태를 바꾸지 않고 바꾸기
wrong_string = "Pithon"
print(wrong_string[:1] + 'Y' + wrong_string[2:])

def rrm(user_rrm): # 주민번호 뒤의 4자리를 가려줌
    return user_rrm[:len(user_rrm)-4] + "****"

print(rrm("981022-2345678"))

# input() 함수를 입력받아 계산 결과 반환
# input() 함수는 문자열 형태로 받기 때문에, 숫자 계산이 필요한 경우 int() 형태로 형변환이 필요함
num1 = int(input("첫 번째 숫자를 입력하세요 : "))
num2 = int(input("두 번째 숫자를 입력하세요 : "))

result = a + b
print(result)
