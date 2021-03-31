# 파일을 생성하기 위해 open이라는 파이썬 내장 함수를 사용함
# 파일 객체 = open(파일 이름, 파일 열기 모드)
# 'r' : read(읽기 모드), 'w' : write(쓰기 모드), 'a' : 추가 모드(마지막에 새로운 내용 추가)
f = open("새파일.txt", 'w', encoding="utf-8")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 프로그램 종료 시 자동으로 close를 하나, 직접 닫아 주는 것 권장(닫지 않고 사용하려 하면 오류 발생)
