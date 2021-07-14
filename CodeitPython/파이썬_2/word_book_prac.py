# 단어장 만들기
# 단어, 뜻을 입력할 때마다 vocabulary.txt 에 단어가 정리됨
out_voca = open('vocabulary.txt', 'w', encoding='utf-8') # 쓰기 모드 지정

# 단어장에 단어 입력

while True:
    # 영어단어, 한국어 뜻 입력 받음
    eng = input("영어 단어를 입력하세요:")
    kor = input("한국어 뜻을 입력하세요:")

    # 종료를 나타내는 q를 입력 받으면, wirte를 하지 않고 반복문 종료
    if eng == 'q':
        break

    # 입력받은 영단어와 한국어 뜻을 out_voca를 통해 vocabulary.txt 파일에 기록
    out_voca.write(eng + ":" + kor + "\n")

# q를 입력하여 더 이상 단어 입력이 없을 경우, write 종료
out_voca.close()