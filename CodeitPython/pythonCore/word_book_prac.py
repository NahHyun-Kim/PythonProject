# 단어장 만들기
# 단어, 뜻을 입력할 때마다 vocabulary.txt 에 단어가 정리됨
out_voca = open('vocabulary.txt', 'w', encoding='utf-8') # 쓰기 모드 지정

# 단어장에 단어 입력

while True:
    # 영어 단어 입력
    eng = input("영어 단어를 입력하세요:")
    if eng == 'q':
        break

    # 한국어 뜻 입력
   kor = input("한국어 뜻을 입력하세요:")
   out_voca.write(eng + ":" + kor + "\n")

# q를 입력하여 더 이상 단어 입력이 없을 경우, wirte 종료
out_voca.close()