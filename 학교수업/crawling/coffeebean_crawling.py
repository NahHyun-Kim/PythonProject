from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

from selenium import webdriver
import time

def CoffeeBean_store(result):
    CoffeeBean_URL = "https://www.coffeebeankorea.com/store/store.asp"
    # Chrome WebDriver 객체 생성
    wd = webdriver.Chrome('../WebDriver/chromedriver.exe')

    for i in range(1, 300): # 매장 수 만큼 반복
        # 웹 페이지 연결
        wd.get(CoffeeBean_URL)
        time.sleep(1) # 웹 페이지 연결할 동안 1초 대기
        try:
                # 매장 정보 페이지를 열 때 실행되는 자바스크립트 함수 호출(storePop())
                wd.execute_script("storePop2(%d)" %i)
                time.sleep(1) # 스크립트 실행 할 동안 1초 대기
                html = wd.page_source # 수행된 페이지의 소스코드 저장
                soupCB = BeautifulSoup(html, 'html.parser') # BeautifulSoup 객체 생성
                store_name_h2 = soupCB.select("div.store_txt > h2")
                store_name = store_name_h2[0].string
                print(store_name) # 매장 이름 출력하기
                store_info = soupCB.select("div.store_txt > table.store_table > tbody > tr > td")
                store_address_list = list(store_info[2]) # 선택해온 store_info에서 0,1,2 중 2번 인덱스에 있는 주소값을 가져옴
                store_address = store_address_list[0] # 선택해온 store_address_list에서 첫번째 tr값인 주소값을 가져옴
                store_phone = store_info[3].string
                # 가져온 상점 정보를 result에 append
                result.append([store_name]+[store_address]+[store_phone])
        except:
            continue
        return

def main():
    result = []
    print('CoffeBean store crawling >>>>>>>>>>>>')
    CoffeeBean_store(result)

    CB_tbl = pd.DataFrame(result, columns=('store', 'address', 'phone'))
    CB_tbl.to_csv('./CoffeeBean.csv', encoding='cp949', mode='w', index=True)

if __name__ == '__main__':
    main()
