from tkinter import *
# GUI 관련 모듈을 제공하는 표준 윈도우 라이브러리

window = Tk() # 기본이 되는 윈도우 반환, 루트 윈도우(=베이스 윈도우)
window.title("윈도우창 연습") # 윈도우 창에 제목 지정
window.geometry("400x100") # 윈도우 창의 크기 설정
window.resizable(width=FALSE, height=FALSE) # 설정한 크기가 변환되지 않도록 고정

window.mainloop() # 베이스 윈도우를 window 변수에 넣고, mainloop 함수로 실행


