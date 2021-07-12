# 튜플 (immutable-변경 불가능, sequence)
# 딕셔너리 (중괄호 사용, key-value 값으로 사용)
num = (1,2,3,4,5)

nh = {
    "name" : "Nh",
    "age" : 24,
    "korean" : True, # boolean 저장 가능, tuple....
    "fav_food" : ["감자튀김", "연어"] # list 저장 가능
}

print(nh)
nh["studying"] = True # dictionary에 데이터 추가 가능
print(nh)