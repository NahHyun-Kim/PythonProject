# 실습과제(learn126) sum_digit 함수 선언 후, 1000까지의 합 구하기
# 자리수 합을 리턴하는 sum_digit 함수 정의
def sum_digit(num):
    result = 0
    for i in str(num):
       result = result + int(i)
    return result

sum = 0
for number in range(1, 1001):
    sum = sum + sum_digit(number)

print(sum)

# 실습과제(learn128) 주민등록번호 가리기(마지막 숫자 4자리를 ****로 가린 주민번호 뒷자리 리턴)
# 주민번호를 가려주는 함수 선언
def mask_security_number(security_number):
    # Mutable(변환할 수 있는) 형태의 list로 변환
    num_list = list(security_number)

    # 마지막 네 개 값을 *로 대체
    for i in range(len(num_list)-4, len(num_list)):
        num_list[i] = '*'

    # 리스트를 문자열로 복구하는 "".join 사용
    # join() : 문자로 이루어진 iterable 객체를 하나의 문자열로 만들어 준다.
    # "".join 따옴표 사이에 문자를 쓸 경우, 각 객체를 연결해줄 연결자로 사용된다.
    total_string = "".join(num_list)
    return total_string

# 굉장히 쉬운 방법
# return security_number[:len(security_number)-4] + "****"

print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))



# 실습과제(learn130) 팔린드롬 - 거꾸로 읽어도 똑같은 함수(문자열이 팔린드롬인지 확인하는 함수)
# 문자열이 팔린드롬이면 True를, 아니면 False를 리턴하는 함수 생성

def is_palindrome(word):
    # 양쪽이 같을 경우를 카운팅하기 위한 true_cnt 변수 설정
    true_cnt = 0
    # 문자열의 길이가 홀수인 경우, 가운데 위치한 수는 비교하지 않아도 되기 때문에 len(world)의 2를 int형으로 형변환
    for left_index in range(int(len(word) / 2)):
        # 양쪽이 모두 같기 위해 만족해야하는 쌍의 개수(int(len(world)/2))
        need_cnt = int(len(word) / 2)
        # 왼쪽의 인덱스와 대응하여 같은 값을 가져야 하는 오른쪽 인덱스의 위치 지정
        right_index = len(word) - left_index - 1
        # 대응한 위치를 구한 왼쪽과 오른쪽 인덱스의 값이 같은 경우(팔린드롬의 조건 만족), true_cnt 를 1 올림
        if word[left_index] == word[right_index]:
            true_cnt = true_cnt + 1
    # for문을 통해 모든 자릿수 쌍의 true_cnt를 체크 후, 모두 같기 위해 만족해야하는 쌍의 갯수인 need_cnt와 같으면 True
    if true_cnt == need_cnt:
        return True
    # 그 외 true_cnt가 need_cnt와 1이라도 차이나면 대응하지 않는 자릿수가 있다는 뜻으로 팔린드롬이 아님. False 리턴
    else:
        return False

    tmp = list(reversed(word))
    string = ''.join(tmp)
    if (word == string):
        msg = True
    else:
        msg = False
    return msg

print(is_palindrome("racecar"))
print(is_palindrome("wasitacatisaw")) # ebs
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
print(is_palindrome("김나현"))
print(is_palindrome("lololol"))