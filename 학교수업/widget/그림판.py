# 7-1 응용프로그램
from tkinter import *
from tkinter.colorchooser import *
from tkinter.simpledialog import *

# 함수 선언 부분

# 전역 변수 선언 부분
window = None
canvas = None
x1, y1, x2, y2 = None, None, None, None # 전역 시작점과 끝점
penColor = 'black'
penWidth = 5

# 메인 코드 부분
if __name_ == "__main__" :
    window = Tk()
    window.title("그림판 비슷한 프로그램")
    canvas = Canvas(window, height = 300, width = 300)
    canvas.bind("<Button-1>", mouseClick)
    canvas.bind("<ButtonRelease-1>", mouseDrop)
    canvas.pack()

    mainMenu = Menu(window)
    window.config(menu = mainMenu)
    fileMenu = Menu(mainMenu)

