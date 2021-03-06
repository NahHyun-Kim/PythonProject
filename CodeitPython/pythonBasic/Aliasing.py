# Aliasing
x = [2, 3, 5, 7, 11]
y = x # y=x라는 명령에 의해, 같은 리스트에 y라는 이름표를 달음
# y는 x의 가명, Alias : 이름은 다르지만 같은 값이라는 뜻(같은 메모리 주소에 있는 값을 가리킴)
y[2] = 4
print(x)
print(y) # 둘 다 2,3,4,7,11 출력 : 2,3,4,7,11 의 리스트가 x,y의 이름표를 갖고 있기 때문에 둘다 같은 리스트를 출력

# y의 값은 바꾸면서, x의 값은 바꾸지 않으려면?
# list 함수 : 원본을 복사해 새로운 공간에 붙여넣고, 새로운 공간의 리스트를 리턴
y = list(x) # list 함수를 사용하여, 새로운 리스트를 복사하여 만들어 줌
y[2] = 4
print(x) # 2,3,5,7,11 (x 이름표가 달려 있음)
print(y) # 2,3,4,7,11 (y는 x의 alias가 아님)

# 실습과제(learn122) 리스트에 있는 데이터의 순서를 거꾸로 뒤집기
numbers = [2, 4, 6, 8, 10, 12, 14]

# 가운데 수를 제외한 왼쪽 인덱스를 기준으로 for문 돌림
for left_index in range(int(len(numbers)/2)):
    # ex) 0번째와 반대인 6번째를 구하려면? 또는 1과 5를 구하려면? 길이-왼쪽 인덱스-1 (7-0-1..)
    right_index = len(numbers) - left_index - 1

    # 기존 left_index의 값을 right_index로 보내야 하므로, 값을 보존하기 위해 임시 변수 temp에 값을 담음
    temp = numbers[left_index]
    # left_index의 자리에 반대편에 있는 right_index의 배열값을 담음
    numbers[left_index] = numbers[right_index]
    # 임시로 보존했던 값인 temp의 값을 right index에 대입
    numbers[right_index] = temp

print("뒤집어진 리스트: " + str(numbers))