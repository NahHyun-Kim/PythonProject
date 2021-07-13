import urllib.request
import bs4

# 웹에서 데이터를 받아오기 위해 http request라는 요청을 보내서 받아와야 함
# 파이썬에서 웹의 특정 주소로 요청을 보내는 기능이 urllib.request
# urllib.urlrequest.urlopen 함수로 네이버의 첫 페이지를 불러옴
url = "https://www.naver.com"
html = urllib.request.urlopen(url)

# 뷰티솝에 데이터를 넣은 후, 파이썬에서 가공할 수 있는 형태로 만들어줌
bs_obj = bs4.BeautifulSoup(html, "html.parser")

# 찾아내려는 단어가 위치한 service_area라는 클래스명을 가진 div 부분을 추출하여 출력
# = <div class="service_area">
# .find() 명령어를 사용해 div 태그 중 class가 service_area인 첫 번째 태그를 찾음
top_right = bs_obj.find("div", {"class" : "service_area"})

# .find() 명령어를 사용해 a태그를 찾은 뒤, a태그 안에 있는 text만 뽑아 냄
first_a = top_right.find("a")

print(first_a.text) # a태그 안의 text만 뽑아냄(first_a.text)