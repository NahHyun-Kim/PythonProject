# if 조건문(참과 거짓) 표현
# elif문은 이전 조건문이 거짓일 때 수행, 개수에 제한 없이 사용 가능
money = 1
if money == 1:
    print("택시를 타고 가라")
else:
    print("돈이 없으니 걸어가라")

# 비교 연산자(>=, ==, <=, !=...) 이용
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# 돈이 3000원 이상 있거나, 카드가 있으면 참일 때
money = 2000
card = 1
if money >= 3000 or card:
    print("택시를 타고 가라") # 둘 중 하나만 참이여도 True를 반환하는 or

# not in (리스트/튜플/문자열)
print(1 in [1,2,3])
print(1 not in [1,2,3])
print('j' not in 'python')

pocket = ['paper', 'money', 'card']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("카드를 꺼내라")

