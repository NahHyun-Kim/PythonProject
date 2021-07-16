import requests
from bs4 import BeautifulSoup # 데이터를 추출(Soup)
from indeed import extract_indeed_pages

max_indeed_pages = extract_indeed_pages()

print(max_indeed_pages)