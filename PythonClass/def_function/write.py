# 파일에 새로운 내용 추가하기
# with 문을 사용하면 with 블록을 벗어나는 순간 열린 파일 객체  f가 자동으로 close됨.
# with open 파일명, 모드, 인코딩 as f
with open("새파일.txt",'a',encoding="utf-8") as f: # 추가 모드(a)로 열기
    for i in range(11,20): # 11부터 19까지 i에 대입
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
f.close()