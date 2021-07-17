# 공백 제거 함수 1) replace(기존 내용, 바꿀 내용) 2) l/r/strip
# requests 모듈 : Python에서 Http 요청을 보내는 모듈(.get(url)명으로, .status_code로 응답코드를 알 수 있음(200이면 정상)
import requests
import os

head_url = "http://"

print('Welcome to IsItDown.py!')
print('Please Write a URL or URLs you want to check. (seperated by comma)')

# url이 정상적으로 연결되었는지 체크
def get_check(url):
    try:
        result = requests.get(url)
        if result.status_code == 200:
            print(f"{url} is up!")
    # connection Error등 오류 캐치
    except:
        print(f"{url} is down!")

# url을 입력받고, 공백 제거, 소문자로 변경, http를 붙임 등 처리
def input_url():
    # url 입력받기(url이 여러 개일 경우 ,로 구분하여 입력 받음)
    url_list = []
    url_list.append(input().strip().lower().split(','))

    for url in url_list:
        if "." in ''.join(url):
            if head_url not in url:
                # ''.join(모든 요소를 합쳐 하나의 문자열을 반환 -> list to str)
                url = head_url + ''.join(url)
                get_check(url)
            else:
                get_check(url)
        else:
            print(f"{''.join(url)} is not a valid URL.")

while True:
    input_url()
    yes_or_no = input('Do you want to start over? y/n')
    if yes_or_no == 'n':
        print('ok, bye!')
        break
    elif yes_or_no == 'y':
        input_url()
    else:
        print('plz enter y/n.')
        break