# days tuple
days = ("Mon", "Tue", "Wed", "Thur", "Fri")

# for문이 실행될 때, sep_day라는 변수가 만들어져 각자의 아이템을 가리킴
for sep_day in days:
    if sep_day is "Wed":
        break # break 반복문 종료(loop를 빠져나감)
    else:
        print(sep_day) # 수요일이 될때까지 요일을 출력

for letter in "nahyeon": # string도 배열이기 때문에, 글자 하나하나 출력됨
    print(letter)