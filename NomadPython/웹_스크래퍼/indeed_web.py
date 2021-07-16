import requests
from bs4 import BeautifulSoup

INDEED_URL = "https://www.indeed.com/jobs?q=python&limit=50"

def extract_indeed_pages():
    result = requests.get(INDEED_URL)

    # print(indeed__result.text) # 홈페이지로부터 가져온 텍스트 출력(html)

    # 필요한 정보만 추출하여 출력하기(bs4)
    # 사용할 html_doc을 넣고, html.parser를 사용할 것이라고 알려줌
    soup = BeautifulSoup(result.text, 'html.parser')  # print(indeed__soup)

    # 페이지에 해당하는 태그를 찾아 지정(.pagination)
    # .find() 메소드로 "찾을 태그", "속성 json 형태" 지정
    pagination = soup.find("div", {"class": "pagination"})  # print(pagination)

    # 페이지를 표시하는 a태그인 모든 것을 가져옴(find_all)
    links = pagination.find_all('a')

    pages = []
    # 마지막 페이지 Next를 나타내는 부분 제외하고 가져옴(리스트 슬라이싱)
    for link in links[:-1]:
        # span 태그를 찾은 후 안에 있는 string만 가져옴 link.find("span").string -> a 요소 안에 string이 하나만 있다면 .string으로 접근 가능
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


# print(range(max_page)) # range() : 넣은 수만큼 크기의 배열을 만들어줌
# for n in range(max_page):
#   print(f"start={n*50}") # page당 50개, 0~19까지 배열(1페이지는 ~50, 2페이지는 50부터 시작, 3페이지는 100부터 -> index * 50 과 같다)