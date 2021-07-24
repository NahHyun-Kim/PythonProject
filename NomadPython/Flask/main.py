# html을 렌더링하기 위한 render_template
from flask import Flask, render_template, request, send_file
from scrapper import get_jobs
from exporter import save_to_file

# Flask 앱 생성(앱 이름)
from werkzeug.utils import redirect

app = Flask("SuperScrapper")

# 가상의 db역할을 하는 dictionary 생성(검색 키워드의 직업정보를 저장하고, 있으면 불러옴)
db = {}

# "/" url에 접속할 때 실행할 함수 선언(기본)
# @ : decorate(함수를 찾아 실행시킴 : / url 접근 -> @ -> 바로 아래의 home 함수를 찾아 실행)
# GET 메소드로 접근
@app.route("/")
def home():
    # <h1> 태그의 html 코드 반영하여 return(필요한 파일을 html 파일 내에서 읽어온다.)
    return render_template("main.html")

@app.route("/report")
def report():
    # get 방식으로 전달받은 name값 word의 값을 보여줌
    # 모든 args로 출력 시 dictionary 형태로 모든 인자 반환
    word = request.args.get("word")
    if word:
        word = word.lower()

        existingJobs = db.get(word)
        # 키워드 정보가 db에 존재한다면, 새로 스크래퍼를 실행하지 않고 기존 내용을 가져옴(True)
        if existingJobs:
            jobs = existingJobs
        else:
            # 존재하지 않으면, word를 param으로 검색 호출
            jobs = get_jobs(word)
            # 가짜 db에 저장! 기존 검색 키워드(ex. db['react'] )가 db에 저장되어 있다면, 또 scrapper를 돌리지 않아도 됨
            db[word] = jobs
    else:
        # redirect(word 존재하지 않을때)
        return redirect("/")

    # return f"You ard looking for a job {word}"
    # html 파일로 리턴 시, 전달할 인자를 함께 정의
    # 1) html 파일에서 전달받은 searchingBy 인자(word를 담은 변수)를 출력, {{}} 문법 사용
    # 2) html 파일에서 flask python 코드를 작성할 때는 {% for job in jobs %} {% endfor %} 형식으로 사용
    return render_template("report.html",
                           searchingBy=word,
                           resultsNumber=len(jobs),
                           jobs=jobs)

# 검색결과 파일 csv 파일로 내보내기
@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        # 단어가 존재하지 않으면(word=None) exception 발생 -> except문 실행
        if not word:
            raise Exception()
        # 단어가 존재하면, db{} 에서 해당 단어의 데이터를 가져와 export 진행
        word = word.lower()
        # 가져온 jobs가 존재하지 않으면 except문 실행
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        # send_file 메소드로 jobs.csv 파일 리턴
        return send_file("jobs.csv")
    except:
        return redirect("/")

@app.route("/contact")
def contact(): # url과 함수명은 달라도됨(requestMapping 처럼)
    return "Contact me!"

# placeholder < >, 입력받은 이름을 인자로(username) 전달해 실행화면에 표시
@app.route("/<username>")
def hello(username):
    return f"Hello, Your name is {username}!"

# 서버 실행, host = 0.0.0.0
app.run(host="0.0.0.0")