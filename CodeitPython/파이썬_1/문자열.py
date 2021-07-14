# 리스트에서의 인덱싱
alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F']
print(alphabets_list[0:3]) # index 0부터 index 2까지(A,B,C)
print(alphabets_list[-1])
print(alphabets_list[2:]) # index 2부터 끝까지
print(alphabets_list[:2]) # 처음부터 index 2-1인 1까지(0,1)

# list의 연결이 가능하듯, 문자열도 연결이 가능
# len함수를 통해 문자열의 글자수를 셀 수 있음
alphabets_string = 'ABCDEF'
print(alphabets_string[0:5]) # list와 비슷하게 문자 출력(ABCDE)
print(alphabets_string[:4]) # list와 비슷하게 0,1,2,3번째 인덱스 출력(ABCD)
print(alphabets_string[2:]) # list와 비슷하게 2번째 인덱스(C)부터 끝까지 출력(CDEF)

for alphabet in alphabets_string:
    print(alphabet)
# list와 string의 차이?
# list는 list[0] = 'C'와 같이 인덱스에 해당하는 값을 수정이 가능하나(=Mutable), string 문자열은 불가능(Immutable)
# ex) name = 'codeit' , name[0]= 'C' 를 대입할 경우 오류 발생
# 오류 메시지 : TypeError: 'str' object does not support item assignment
# 문자열의 불변 보장에 대한 여러 가지 이유 때문에, 원소로 취급