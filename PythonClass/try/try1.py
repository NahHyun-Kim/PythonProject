# try, except문을 통해 예외 처리를 할 수 있다.
try:
    4/0
except ZeroDivisionError as e:
    print(e) # 0으로는 나눌 수 없기 때문에, except 블록을 실행해 에러 메시지 출력


# try, except, else 문을 통한 예외 처리
try:
    f = open('foo.txt', 'r', encoding="utf-8")
except FileNotFoundError as e:
    print(str(3))
else: # foo.txt 파일이 있다면 else 절 수행
    data = f.read()
    f.close()

f = open('foo.txt', 'w')
try:
    print("do something")
finally:
    f.close()

# finally 절은 예외 발생 여부 상관 없이 항상 수행된다(리소스 close 시 주로 사용)

try:
    f = open('없는 파일','r',encoding='utf-8')
except FileNotFoundError:
    pass # 오류가 발생하더라도(파일이 없더라도) 오류를 발생시키지 않고 통과함
