import requests
from bs4 import BeautifulSoup # 데이터를 추출(Soup)
from indeed_web import extract_indeed_jobs, extract_indeed_pages

last_indeed_page = extract_indeed_pages()

# 가져온 최대 페이지까지의 범위로 start-page를 구함(request 생성)
indeed_jobs = extract_indeed_jobs(last_indeed_page)

print(indeed_jobs)