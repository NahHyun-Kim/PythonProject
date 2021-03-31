f = open("새파일.txt",'r',encoding="utf-8")
line = f.readline()
print(line) # 가장 첫번째 줄만 출력
while True:
    line = f.readline()
    if not line: break
    print(line)

# readlines 함수를 이용하여 각각의 줄을 요소로 갖는 리스트로 리턴
lines = f.readlines()
for line in lines:
    print(line)
f.close()

