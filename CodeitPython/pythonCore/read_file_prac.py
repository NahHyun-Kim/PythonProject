in_file = open("readfile.txt","r",encoding="utf-8")

# n일 : 숫자 형태에서 숫자 부분만 가져와서 저장
# 줄을 제거하는 stripg함수를 이용하여 각 줄에 줄을 제거 후,
# 그 결과 값에서 split(: )을 통해 앞의 일수와 뒤의 숫자로 나눈다.
# 더하려는 숫자값이 배열의 [1] 에 위치하므로, [1]을 사용하며 int형으로 형 변환 후 합을 계산한다.
sum = 0
for i in in_file:
    sum = sum + int((i.strip().split(": "))[1])

print(sum)