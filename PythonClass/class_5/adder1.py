result = 0

def adder(num):
    # 이전에 계산된 결과값을 유지하기 위해 result라는 전역변수 global 사용
    global result
    result += num
    return result


print(adder(3))
print(adder(4))