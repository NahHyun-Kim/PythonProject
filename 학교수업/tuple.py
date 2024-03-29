# 튜플(tuple)은 ()로 둘러싸며, 리스트와 달리 그 값을 바꿀 수 없음
t1 = 1,2,3 # 괄호를 생략 할 수 있음
t2 = ()
t3 = ('a','b',('ab','cd'))
# del 함수로 지우려고 하면 오류 발생, 변경하려고 해도 오류 발생(값 변경 불가)

# 튜플 인덱싱
t1 = (1,2,'a','b')
print(t1[0])

# 튜플 슬라이싱
print(t1[1:]) # t1[1]부터 리스트의 마지막까지 슬라이싱

# 튜플 더하기, 곱하기
t2 = (3,4)
print(t1 + t2)
print(t2 * 3)