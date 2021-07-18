import requests
from bs4 import BeautifulSoup # 데이터를 추출(Soup)
from indeed_web import get_jobs as get_indeed_jobs
from stackoverflow_web import get_jobs as get_so_jobs

# stackoverflow, indeed 사이트의 취업정보 가져오기
indeed_jobs = get_indeed_jobs()
so_jobs = get_so_jobs()

jobs = so_jobs + indeed_jobs
print(jobs)