numbers = "1. 2. 3. 4. 5. 6"
print(numbers.split(". ")) #strip() 또는 공백을 포함한 .을 기준으로 나눔

full_name = "Kim, NaHyeon"
name_data = full_name.split(", ")

last_name = name_data[0]
first_name = name_data[1]

number_data = numbers.split(". ")
print(number_data[0] + number_data[1]) # 3이 아닌 12로 (문자열의 연결로 출력)
print(int(number_data[0]) + int(number_data[1]))

some_string = "  abd csdfa sd   dsf "
print(some_string.split()) # split 조건을 지정하지 않으면 공백을 기준으로 나누어서 반환함