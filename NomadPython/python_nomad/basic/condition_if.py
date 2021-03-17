def plus(a,b):
    # 서로 다른 두개의 조건 chaining(연결) - or
    if type(b) is int or type(b) is float:
        return a + b
    else:
        return None

plus(12, "10")

def age_check(age):
    print(f"You are {age}")
    if age < 18:
        print("you cant drink")
    elif age == 18:
        print("you are new to this!")
    elif age > 20 and age < 25:
        print("you are still kind of young")
    else:
        print("enjoy your drink")

age_check(24)