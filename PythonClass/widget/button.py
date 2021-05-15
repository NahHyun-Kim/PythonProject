# 버튼
from tkinter import *
from tkinter import messagebox

# window = Tk()

# Button에 옵션을 주어 생성하며, "파이썬 종료"라는 문구를 누르면 command 옵션에 quit 명령이 내려져 클릭 시 종료됨
# button1 = Button(window, text="파이썬 종료", fg="red", command=quit)
# button1.pack()
# window.mainloop()

# 함수 선언하기
# messagebox를 활용하여, 화면에 메세지 박스(alert와 비슷한 확인창)를 출력한다.
def myFunc():
    # 제목, 표시할 내용
    messagebox.showinfo("강아지 버튼", "강아지가 귀엽죠? ^^")

# 메인 코드 부분
window2 = Tk()

photo = PhotoImage(file="../gif/dog2.gif")
# Button 옵션에 gif파일을 담은 photo 변수를 넣어 이미지를 표시하고, 클릭 시 myFunc을 호출하여 실행
button2 = Button(window2, image=photo, command=myFunc)

button2.pack()
window2.mainloop()