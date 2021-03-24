in_file = open("readfile.txt","r",encoding="utf-8") # open 내장함수를 사용하여 파일을 읽음, 'r'은 읽는다는 뜻

# <class '_io.TextIOWrapper'>, 리스트와 비슷하게 for문으로 사용이 가능
print(type(in_file))

for line in in_file:
    print(line.strip()) # 각 줄을 모두 출력 + 빈 줄 제거

in_file.close() # open 후에는 꼭 닫아주어야 함(메모리 낭비 우려)

# strip(문자열 앞 뒤의 공백, \n 제거)
# 중간에 있는 공백은 제거하지 않음음print("    abc   def    ".strip())
print("    \n    abc  \n\n  ".strip())