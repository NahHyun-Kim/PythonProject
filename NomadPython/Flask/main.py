# html을 렌더링하기 위한 render_template
from flask import Flask, render_template, request

# Flask 앱 생성(앱 이름)
app = Flask("SuperScrapper")

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
    # return f"You ard lokking for a job {word}"
    # html 파일로 리턴 시, 전달할 인자를 함께 정의
    return render_template("report.html", searchingBy=word)

@app.route("/contact")
def contact(): # url과 함수명은 달라도됨(requestMapping 처럼)
    return "Contact me!"

# placeholder < >, 입력받은 이름을 인자로(username) 전달해 실행화면에 표시
@app.route("/<username>")
def hello(username):
    return f"Hello, Your name is {username}!"

# 서버 실행, host = 0.0.0.0
app.run(host="0.0.0.0")