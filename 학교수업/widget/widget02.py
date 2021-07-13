from tkinter import *
window = Tk()

# label 함수로 레이블을 만듬
# bg(백그라운드 약어) fg(글자색 지정)
# anchor(위젯이 어떤 위치에 자리 잡을지 결정, ex) SE : South East의 약어, 기본값은 CENTER이다.)
label1 = Label(window, text = "COOKBOOK~~Python을")
label2 = Label(window, text = "열심히", font = ("궁서체, 30"), fg="blue") # 폰트(글꼴, 크기) , fg(forground-color : 글자색)
label3 = Label(window, text = "공부 중입니다.", bg = "magenta", width=20, height=5, anchor = SE)

# pack 함수로 해당 레이블을 화면에 표시(레이블 같은 위젯은 pack() 함수를 호출해야 화면에 표시됨)
label1.pack()
label2.pack()
label3.pack()

window.mainloop()

# PhotoImage() 를 통해, file명="경로"를 입력하여 gif 파일을 넣을 수 있음.(jpeg, bmp는 지원하지 않음)
window2 = Tk()
photo = PhotoImage(file="../gif/dog.gif")
label4 = Label(window2, image=photo) # label()의 옵션인 image에서 photo 변수를 사용

label4.pack()

window2.mainloop()