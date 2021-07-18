import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"

def get_last_page():
    # request 요청
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')

    # <div class="s-pagination"> 안에 있는 "a" 태그를 모두 가져옴(.find_all("a"))
    pages = soup.find("div", {"class" : "s-pagination"}).find_all("a")
    # 마지막 페이지 추출(get_text() ,[-2] 인덱스로 마지막의 next 제외
    last_page = pages[-2].get_text(strip=True)

    return int(last_page)

# 각각의 회사정보를 추출하여 객체형태로 반환하는 extract_job
def extract_job(html):
    # class명이 mb4인 h2 태그의 a태그 중 "title" 속성값을 가져옴
    title = html.find("h2", {"class" : "mb4"}).find("a")["title"]

    # recursive=False(span 태그 안의 전부를 가져오지 않게 해줌 : 가장 첫 단계만 가져옴)
    # unpacking value(요소가 이미 2개인 것을 알고 있을때 사용) -> 첫번째 value는 compnay에, 두번째는 location에 담김
    company, location = html.find("h3", {"class": "mb4"}).find_all("span", recursive=False)

    company = company.get_text(strip=True)
    # .strip("-").strip("\n") 과 같이 여러번 strip을 통해 정제 작업이 가능함
    location = location.get_text(strip=True)
    # <div class="-job ..">인 태그의 data-jobid 속성을 가져온다.
    job_id = html['data-jobid']

    return {'title' : title,
            'company' : company,
            'location' : location,
            'apply_link' : f"https://stackoverflow.com/jobs/{job_id}"
            }

# 1페이지부터 last_page까지 range로 loop를 돌리며 가져옴(for문 안에서 세부 정보 추출 함수를 실행)
def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping SO: Page: {page}")
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("div", {"class" : "-job"})
        for result in results:
            job = extract_job(result)
            print(job)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs