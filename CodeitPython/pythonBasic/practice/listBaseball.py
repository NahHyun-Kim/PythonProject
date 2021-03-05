from random import randint

# 실습과제(leanr102) 숫자 야구 게임(값과 위치를 맞추려고 함)
# 컴퓨터는 스트라이크(S)와 볼(B)의 개수를 알려준다.
# 숫자, 값이 모두 일치하면 S, 숫자와 값은 일치하지만 위치가 틀렸으면 8
# ex 1,3,5 생성하였는데 사용자가 1,3,5를 입력하면 1s(위치 값 일치), 1b(3의 값만 일치)
# 기회는 무제한이며, 몇 번의 시도 끝에 맞췄는지 기록된다.
# 게임은 3S일 때 끝난다.

def generate_numbers():
    # 숫자 생성 후, 리스트에 넣음
    list = []
    # 첨자변수 i를 선언하지 않고, list의 길이만큼 반복하며 확인 & 랜덤 숫자 배열에 추가
    while len(list) < 3:
        num = randint(0, 9) # 0과 0 사이의 서로 다른 세 숫자 생성
        # list에 숫자가 없을 경우에만 추가(중복 제거)
        if num not in list:
            list.append(num)

    # 함수 사용 후 리스트 리턴
    return list

ANS = generate_numbers()
print(ANS)
print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")

cnt = 0  # 총 몇 번만에 값과 위치를 모두 맞추었는지(strike = 3) 횟수를 저장
s = 0
b = 0
print("세 수를 하나씩 차례대로 입력하세요.")
# strike가 3이 나올때 까지 무한 반복
while s < 3:
    guess = []
    # 0,1,2번째 세 개의 수를 guess에 입력받아 저장
    while len(guess) < 3:
        # 새로 입력한 수가 guess에 없을 경우만 추가
        # 여기서 input 은 무조건 문자열 형태로 입력되니, 꼭 int형으로 형 변환이 필요함
        guess_numbers = int(input(f"{len(guess) + 1}번째 수를 입력하세요: "))

        # 범위를 벗어나는 경우
        if guess_numbers < 0 or guess_numbers > 9:
            print("0에서 9까지의 수를 입력해 주세요!")
        # 중복된 수를 입력하면 설명 메시지 출력
        elif guess_numbers in guess:
            print("중복되지 않은 새로운 수를 입력해 주세요!")
        # 두 문제에 해당하지 않는 경우 guess 리스트에 추가
        else:
            guess.append(guess_numbers)

    # Strike 혹은 Ball 횟수 체크를 위한 변수 선언

    s = 0
    b = 0
    i = 0
    # guess[0]번째부터 guess[2]까지 값 검사
    while i < 3:
        if guess[i] == ANS[i]: # 추측한 guess의 i번째 값과 list의 i번째 값이 같을 경우(=strike)
            s = s + 1
        elif guess[i] in ANS: # 값과 위치는 일치하지 않지만, list안에 있는 값일 때(Ball)
            b = b + 1
        i = i + 1

    print("%dS %dB" % (s,b))

    cnt = cnt + 1

# 모두 맞춘 경우(s가 3일 경우 축하 메시지)
print(f"축하합니다. {cnt}번만에 세 숫자의 값과 위치를 모두 맞추셨습니다.")