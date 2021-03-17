# 집합 자료형은 set 키워드를 이용해 만들 수 있음
# 중복을 허용하지 않으며, 순서가 없음(=인덱싱으로 값을 얻을 수 없음)
s1 = set([1,2,3])
print(s1)
s2 = set("Hello")
print(s2) # e,l,o,H 반환

# set 자료형의 값에 인덱싱으로 접근하려면 리스트나 튜플로 변환 후 접근이 가능함
s1 = set([1,2,3])
l1 = list(s1) # list 형태로 형변환
print(l1)
print(l1[0]) # list 형태로 형변환 되었기 때문에, 인덱싱이 가능

t1 = tuple(s1)
print(t1)
print(t1[2]) # tuple 형태로 형변환 되었기 때문에, 인덱싱이 가능

# 집합 자료형 활용
# 교집(&)), 차집합(-), 합집합(|) 구하기
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1 & s2) # 교집합(&)
print(s1.intersection(s2)) # 동일한 결과 반환(&과 같음, &)

print(s1 | s2) # 합집합(|)
print(s2.union(s2))

print(s1 - s2) # 차집합(-)
print(s1.difference(s2)) # s1-s2 값 반환(1,2,3)
print(s2.difference(s1)) # s2-s1 값 반환(8,9,7)

# 집합 자료형 관련 함수
# 값을 1개 추가하는 add
s1 = set([1,2,3])
s1.add(4) # 이미 만들어진 set 자료형에 값을 추가
print(s1)

# 값을 여러개 추가하는 update
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1) # 기존 1,2,3에 4,5,6이 추가된 {1,2,3,4,5,6} 반환

# 특정 값을 제거하는 remove
s1 = set([1,2,3])
s1.remove(2)
print(s1)
