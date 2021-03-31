# 사용자 입력
# input은 입력되는 모든 것을 문자열로 취급함

a = input()
print(a)

# input() 괄호 안에 질문을 입력하여 프롬프트를 띄워 줌
number = input("숫자를 입력하세요 : ")
print(f"입력받은 숫자는 {number} 입니다.")

# 큰 따옴표로 둘러싸인 문자열은 + 연산과 동일함
print("life" "is" "too short") # life is too short
print("life", "is", "too short") # 콤마를 이용하면 문자열 간에 띄어쓰기를 할 수 있음

# 한 줄에 결과값 출력하기
for i in range(10):
    print(i, end=' ')
