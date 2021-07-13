import sys

# sys 모듈로 입력 인수 주기(import sys 상숑)
args = sys.argv[1:]
for i in args:
    print(i) # for문을 이용하여 하나씩 차례대로 출력
    
# sys_module.py 파일을 실행할 때 입력 인수를 함께 주어 실행시키면 그 값을 출력

args = sys.argv[1:]
for i in args:
    print(i.upper(),end='') # 입력된 소문자를 대문자로 변경
# 파일명과 함께 출력할 문자열 입력 시, 대문자로 변환된 문장 출력