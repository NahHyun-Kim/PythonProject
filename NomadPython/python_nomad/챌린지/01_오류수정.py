days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


# day(요일)이 리스트에 있는지 확인하여 T/F 반환
def is_on_list(days, day):
    if day in days:
        return True
    else:
        return False


# days 리스트의 번째수를 반환(0부터 시작, 인덱스 [3])
def get_x(days, index):
    return days[index]


# days 리스트에 요소를 추가(append)
def add_x(days, day):
    days.append(day)
    return day


# days 리스트에 지정한 요소를 제거(remove)
def remove_x(days, day):
    days.remove(day)
    return day


print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)



# 2차원 연습
lsts = [['a','b'], ['c','a'], ['e','f']]

for lst in lsts:
    if 'a' in lst: # lst[0]이라면 각 요소의 첫번째 값만 확인한다(['a','b']의 [0])
        print("a가 포함됩니다")
    else:
        print("미포함")