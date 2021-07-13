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
