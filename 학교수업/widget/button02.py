# 체크버튼, 라디오

from tkinter import *
from tkinter import messagebox

window = Tk()

# 함수 선언 부분
def myFunc() :
    if chk.get() == 0:
        messagebox.showinfo("", "체크버튼이 꺼졌어요.")
    else:
        messagebox.showinfo("", "체크버튼이 켜졌어요.")

# 메인 코드 부분
# chk 변수를 준비하는데 IntVar() 함수 사용 -> 정수형 타입의 변수
chk = IntVar()
# "클릭하세요" 문구를 클릭하면, 그 값은 chk로 정수형 변수에 들어가며, 누를 시 myFunc 호출하여 실행
cb1 = Checkbutton(window, text="클릭하세요", variable=chk, command=myFunc)