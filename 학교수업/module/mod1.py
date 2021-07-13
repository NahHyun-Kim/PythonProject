def sum(a,b):
    return a + b

def safe_sum(a,b):
    if type(a) != type(b):
        print("더할 수 있는 것이 아닙니다.") # 자료형이 같지 않으면 문구 출력
        return # None 값 반환
    else: # 자료형이 같다면 연산 수행
        result = sum(a,b)
    return result # 두 객체를 더함

if __name__ == "__main__":
    print(safe_sum(3, 4))
    print(safe_sum(1, 'a')) # 직접 mod1.py 파일을 메인으로 실행 시켰을 때만 참이 되어 실행
    # 다른 대화영 인터프리터나 다른 파일에서 모듈을 불러서 사용할 때는 거짓이 되어 다음 문장이 수행되지 않음