# Key, Value 값으로 구성된 Dictionary 자료형

dic = {'name':'nh','phone':'01012345678','birth':'1022'}
print(dic)

# value에 list로 넣을 수 있음
a = {'a' : [1,2,3]}

# 딕셔너리 쌍 추가하기
a = {1:'a'}
a[2] = 'b'# key, value 한 쌍의 형태로 추가
print(a)
a['name'] = 'pey'
print(a)
a[3] = [1,2,3] # [1,2,3] 리스트를 가지는 한 쌍 추가
print(a)

# 딕셔너리에서 key를 사용해 value 얻기(grade)
grade = {'nh' : 10, 'yh' : 99}
print(grade['nh'])

# 딕셔너리에서의 key값은 고유한 값이므로, 중복되는 key값 설정 시 하나를 제외하고 모두 무시
a = {1 : 'a' , 1 : 'b'}
print(a) # 1:'b'만 출력되며, 다른 값은 무시됨(고유한 key값의 중복)

# key 리스트 만들기(keys)
# 리스트 고유함수인 append, insert, pop, remove, sort의 함수는 수행할 수 없음
dic = {'name':'nh','phone':'01012345678','birth':'1022'}
print(dic.keys()) # dic의 key값만을 모아서 dict_keys 반환

# for문을 이용하여 key값 모두 출력
for k in dic.keys():
    print(k)

# values 리스트 만들기(values)
print(dic.values()) # dic의 value값만을 모아서 dict_values 반환

# key:value 쌍 모두 지우기(clear)
print(a.clear())

# key로 value 얻기(get)
dic = {'name':'nh','phone':'01012345678','birth':'1022'}
print(dic.get('phone')) # x라는 key에 대응되는 value 값 반환(=dic['name'))
# 찾으려는 값이 없을 경우, 미리 정해둔 디폴트 값을 대신 가져오게 하려면?
print(dic.get('my','name')) # 가져오려는 my라는 key값이 없을 경우, 디폴드 값인 name을 출력

# 해당 key가 딕셔너리 안에 있는지 조사하기(in)
print('name' in dic) # 있으면 True, 없으면 False 반환

# 딕셔너리 자료형을 이용한 영한 사전 프로그램 작성
english_dict = dict()

english_dict['one'] = '하나'
english_dict['two'] = '둘'
english_dict['three'] = '셋'
english_dict['four'] = '넷'
english_dict['five'] = '다섯'
english_dict['six'] = '여섯'
english_dict['seven'] = '일곱'
english_dict['eight'] = '여덟'
english_dict['nine'] = '아홉'
english_dict['ten'] = '열'

word = input("단어를 입력하세요. ");
print(english_dict.get(word, "없음"))