# Immutable Sequence(수정할 수 없음)
# Tuple - list의 [] 대신 ()로 감싸준다.
days = ("Mon", "Tue", "Wed", "Thur", "Fri");
print(f"(Mon...)의 출력 형식은 {type(days)}입니다.")

# Dictionary - Key:value {} 중괄호를 통해 만듬
# 안에 list형식 저장 가능(다양한 형식) - list, tuple..
nh = {
    "name" : "nh",
    "age" : 24,
    "korean" : True,
    "fav_food" : ["salmon",
                  "potato"]
}

print(f'좋아하는 음식 : {nh["fav_food"]}') # dictionary의 key값으로 value를 가져올 수 있다.
print(nh)
print(type(nh))

# dictionary의 key값 출력(dict.keys()) , value값 출력(dict.values()), key-value값 출력(dict.items())
# dictionary의 value값 변경 : dict['key값'] = '바꿀 value값'
# dictionary에 data 추가 : dict['새로운 key값'] = '넣을 value값'
# dictionary 요소 삭제 : del dict[key값]
# dictionary key를 사용하여 value값 얻기 : dict[key값], dict.get('key값')