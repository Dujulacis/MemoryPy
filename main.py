from re import A
from tkinter import*
from PIL import ImageTk, Image
import random
from tkinter import messagebox
mW=Tk()
mW.title("MemoryPy")

bgImg=ImageTk.PhotoImage(Image.open("img/bg.jpg"))

gImg1=ImageTk.PhotoImage(Image.open("img/1.png"))
gImg2=ImageTk.PhotoImage(Image.open("img/2.png"))
gImg3=ImageTk.PhotoImage(Image.open("img/3.png"))
gImg4=ImageTk.PhotoImage(Image.open("img/4.png"))
gImg5=ImageTk.PhotoImage(Image.open("img/5.png"))
gImg6=ImageTk.PhotoImage(Image.open("img/6.png"))


btn0=Button(mW, width=22, height=22)
btn1=Button(mW, width=22, height=22)
btn2=Button(mW, width=22, height=22)
btn3=Button(mW, width=22, height=22)
btn4=Button(mW, width=22, height=22)
btn5=Button(mW, width=22, height=22)
btn6=Button(mW, width=22, height=22)
btn7=Button(mW, width=22, height=22)
btn8=Button(mW, width=22, height=22)
btn9=Button(mW, width=22, height=22)
btn10=Button(mW, width=22, height=22)
btn11=Button(mW, width=22, height=22)

btn0.grid(row=0, column=0)
btn1.grid(row=0, column=1)
btn2.grid(row=0, column=2)
btn3.grid(row=0, column=3)
btn4.grid(row=0, column=4)
btn5.grid(row=0, column=5)
btn6.grid(row=1, column=0)
btn7.grid(row=1, column=1)
btn8.grid(row=1, column=2)
btn9.grid(row=1, column=3)
btn10.grid(row=1, column=4)
btn11.grid(row=1, column=5)

mW.mainloop()