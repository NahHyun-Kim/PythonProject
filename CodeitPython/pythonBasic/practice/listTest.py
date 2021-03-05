# 실습과제(learn92) greeting의 원소를 모두 출력하는 프로그램 작성
greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]
i = 0
while i < len(greetings): # greetings 배열의 길이만큼 출력(while 반복문 실행)
    print(greetings[i])
    i = i + 1



# 실습과제(learn96) 화씨 온도를 섭씨 온도로 바꿔주는 프로그램
# 섭씨와 화씨의 관계씩 섭씨 = (화씨 - 32) * 5 / 9

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9 # 섭씨 온도로 변환하여 celsius 변수에 저장
    return round(celsius, 2) # 소수 둘째 자리까지만 표기하기 위해 round 함수 사용

sample_temperature_list = [40, 15, 32, 64, -4, 11]

# 리스트의 while문을 통해 전체 값 변환
k = 0
while k < len(sample_temperature_list):
    sample_temperature_list[k] = fahrenheit_to_celsius(sample_temperature_list[k])
    k = k + 1

# 화씨 온도 출력하기
print(f"화씨 온도 리스트: {str(sample_temperature_list)}")



# 실습과제(learn98) 환율에 따라 화폐를 교환해 주는 서비스
# 원에서 달러로 바꿔주는 함수
def krw_to_usd(won):
    usd = won / 1000
    return usd

# 달러에서 엔으로 바꿔주는 함수
def usd_to_jpy(dollars):
    jpy = dollars * 125
    return jpy

# 원으로 각각 얼마인가요? (합 출력 후, 프린트))
amounts = [1000, 2000, 3000, 5000, 8000, 13000, 21000, 34000]
print(f"한국 화폐 : " + str(amounts))

# 달러로 각각 얼마인가요? (달러로 변환 후, 프린트)
i = 0
while i < len(amounts):
    amounts[i] = krw_to_usd(amounts[i])
    i = i + 1

print(f"미국 화폐: {str(amounts)}")

# 엔으로 각각 얼마인가요? (엔으로 변환 후, 프린트)
# i값을 초기화 해주는 경우, 계속 i값을 활용할 수 있다.
i = 0
while i < len(amounts):
    amounts[i] = usd_to_jpy(amounts[i])
    i = i + 1

print(f"일본 화폐: {str(amounts)}")


# 실습과제(learn100) 리스트 함수를 활용하여 지시사항대로 출력
# 1. numbers라는 빈 리스트를 만들어 준다.
numbers = []

# 2. append를 이용해서 numbers에 자연수 1~10까지의 값을 추가하고, 출력한다.
i = 1
while i <= 10:
    numbers.append(i)
    i = i + 1

print(numbers)

# 3. numbers 리스트의 원소들 중에 홀수는 모두 제거 후, 출력한다.
i = 0
while i < len(numbers):
    if (numbers[i] % 2 == 1):
        del numbers[i]
    i = i + 1
print(numbers)

# 4. numbers 리스트 인덱스 0 자리에 20이라는 수를 삽입한 후, 출력한다.
numbers.insert(0, 20)
print(numbers)

# 5. 정렬이 되어있지 않으므로, numbers라는 리스트를 정렬한 후 출력한다.
print(sorted(numbers))