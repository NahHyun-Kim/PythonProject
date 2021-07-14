# while문(초기화, while문 조건: 출력할 문장, 증감식)
i = 1

#  while True: 사용시 무한루프로 출력 가능
while i <= 3:
    print("I can code too!")
    i = i + 1

# 100 이상의 자연수 중 가장 작은 23의 배수 출력
j = 100
while True: # while True: 혹은 while 1: 사용 가능(우선 계속 실행)
    if j % 23 == 0:
        print(f"{j}")
        break
    j = j + 1

k = 100
while k % 23 != 0:
    k = k + 1
print(k)


# 100이하의 자연수 중 8의 배수이지만 12의 배수는 아닌 것
num = 1
while num <= 100:
    if (num % 8 == 0 and num % 12 != 0):
        print(num)
    num += 1