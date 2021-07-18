import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

# 최대 페이지를 추출하여 그 페이지까지 웹 스크래퍼를 실행
def get_last_page():
    result = requests.get(URL)

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

# 각각의 태그를 전달받아 필요한 회사정보를 추출하여 object 객체로 반환함
def extract_job(html):
    # select_one 메소드를 이용하면 리스트 형태로 저장되지 않고 가장 첫 태그를 호출(select: 리스트형태, for문으로 접근 필요)
    title = html.select_one('.jobTitle>span').string
    company = html.find("span", {"class" : "companyName"})
    company_anchor = company.find("a")

    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)

    location = html.select_one("pre > div").text
    # 속성이 data-jk인 내용을 가져옴(추후 회사정보 상세보기로 이동을 위함), slider-container를 감싸는 parent(a태그)의 data-jk 속성값
    job_id = html.parent['data-jk']

    # object 형태로 리턴
    return {
        'title' : title,
        'company' : company,
        'location' : location,
        'link' : f"https://www.indeed.com/viewjob?jk={job_id}&from=web&vjs=3"
    }

# print(range(max_page)) # range() : 넣은 수만큼 크기의 배열을 만들어줌
# for n in range(max_page):
#   print(f"start={n*50}") # page당 50개, 0~19까지 배열(1페이지는 ~50, 2페이지는 50부터 시작, 3페이지는 100부터 -> index * 50 과 같다)

# 최대 페이지를 받아 추출
def extract_indeed_jobs(last_page):
    jobs = []

    for page in range(last_page):
        # print(f"&start={page*LIMIT}")
        print(f"Scrapping page {page}")
        result = requests.get(f"{URL}&start={last_page * LIMIT}")
        soup = BeautifulSoup(result.text, 'html.parser')

        results = soup.find_all("div", {"class" : "slider_container"})

        for result in results:
            # 한개씩 추출한 html 태그를 전달하여 extract_job 함수를 통해 return 값을 object로 받아옴
            job = extract_job(result)
            jobs.append(job)

    return jobs

    # results = soup.find_all("h2", {"class": "jobTitle"})
    # for h2 in results:
    #     # h2 태그의 span title="" 부분의 직업을 가져옴
    #     all_spans = h2.find_all("span")
    #     for span in all_spans:
    #         # span 태그의 title 속성 값을 가져옴(None이 아닌 리스트만 배열에 append)
    #         if span.get("title") is not None:
    #             job = span.get("title")
    #             # print(job)
    #
    # # 회사명 : span class="companyName" 안에 존재
    # companies = soup.find_all("span", {"class": "companyName"})
    # for span in companies:
    #     company_name = span.text
    #     # print(company_name)



    # for h2_item in results:
    #     all_spans = h2_item.find("span")
    #     for span_item in all_spans:
    #         if span_item.get("title") is not None:
    #             print(span_item.get("title"))
    #             jobs.append(span_item.get("title"))
    # 변경전("a"태그가 있으면 -> company.find("a") is not None: company.find("a").string
    # ("a"태그가 없으면(else) -> company.string 으로 사용 가능

def get_jobs():
    last_page = get_last_page()
    jobs = extract_indeed_jobs(last_page)

    return jobs