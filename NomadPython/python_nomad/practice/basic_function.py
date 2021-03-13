a = (int(input("첫 번째 숫자를 입력하세요. : ")))
b = (int(input("두 번째 숫자를 입력하세요. : ")))

def plus(a,b):
    return a + b

def minus(a,b):
    return a - b

def multiplex(a,b):
    return a * b

def divide(a,b):
    return round(a / b,2)

def discard(a,b):
    return a // b

def remainder(a,b):
    return a % b

print(minus(a,b))