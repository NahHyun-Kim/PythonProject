# 사전 (dictionary) 단어와 뜻, 즉 key-value 쌍으로 구성

dict1 = {}
print(type(dict1))

dict1[5] = 25
dict1[2] = 4
dict1[3] = 9

print(dict1)
print(dict1[2]) # 4 출력(key 2에 해당하는 value값 2 출력)

me = {}

# 문자열과 숫자형 등 자료형을 섞어서 구성이 가능함
me['name'] = 'nh'
me['age'] = 24
me['hobby'] = ['coding', 'listening to music', 'piano']

print(me)