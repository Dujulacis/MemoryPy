from re import A
from tkinter import*
from PIL import ImageTk, Image
import random
from tkinter import messagebox
mW=Tk()
mW.title("MemoryPy")

count=0
correctA=0
answers=[]
answer_dict={}
answCount=0

#func --------------------------------------------

def btnClick(btn, number):
    global count, correctA, answers, answer_dict, answCount
    if btn["image"]=="pyimage1" and count <2:
        btn["image"]=imageList[number]
        count+=1
        answers.append(number)
        answer_dict[btn]=imageList[number]
    if len(answers)==2:
        if imageList[answers[0]]==imageList[answers[1]]:
            for key in answer_dict:
                key["state"]=DISABLED
            correctA+=2
            if correctA==2:
                #messagebox.showinfo("MemoryPy", "Uzminēji")
                correctA=0
                answCount+=1
        else:
            messagebox.showinfo("MemoryPy", "Neuzminēji")
            for key in answer_dict:
                key["image"]="pyimage1"
        count=0
        answers=[]
        answer_dict={}

    if answCount==6:
        messagebox.showinfo("MemoryPy", "Tu uzvarēji!!! New game?")
        answCount=0


    return 0
    


#images ------------------------------------------

bgImg=ImageTk.PhotoImage(Image.open("img/bg.jpg"))
gImg1=ImageTk.PhotoImage(Image.open("img/1.png"). resize((200, 350), Image.Resampling.LANCZOS))
gImg2=ImageTk.PhotoImage(Image.open("img/2.png"). resize((200, 350), Image.Resampling.LANCZOS))
gImg3=ImageTk.PhotoImage(Image.open("img/3.png"). resize((200, 350), Image.Resampling.LANCZOS))
gImg4=ImageTk.PhotoImage(Image.open("img/4.png"). resize((200, 350), Image.Resampling.LANCZOS))
gImg5=ImageTk.PhotoImage(Image.open("img/5.png"). resize((200, 350), Image.Resampling.LANCZOS))
gImg6=ImageTk.PhotoImage(Image.open("img/6.png"). resize((200, 350), Image.Resampling.LANCZOS))

imageList=[gImg1, gImg1, gImg2, gImg2, gImg3, gImg3, gImg4, gImg4, gImg5, gImg5, gImg6, gImg6]
random.shuffle(imageList)
#buttons ------------------------------------------

btn0=Button(mW, width=200, height=350, image=bgImg, command=lambda:btnClick(btn0, 0))
btn1=Button(mW, width=200, height=350, image=bgImg, command=lambda:btnClick(btn1, 1))
btn2=Button(mW, width=200, height=350, image=bgImg, command=lambda:btnClick(btn2, 2))
btn3=Button(mW, width=200, height=350, image=bgImg, command=lambda:btnClick(btn3, 3))
btn4=Button(mW, width=200, height=350, image=bgImg, command=lambda:btnClick(btn4, 4))
btn5=Button(mW, width=200, height=350, image=bgImg, command=lambda:btnClick(btn5, 5))
btn6=Button(mW, width=200, height=350, image=bgImg, command=lambda:btnClick(btn6, 6))
btn7=Button(mW, width=200, height=350, image=bgImg, command=lambda:btnClick(btn7, 7))
btn8=Button(mW, width=200, height=350, image=bgImg, command=lambda:btnClick(btn8, 8))
btn9=Button(mW, width=200, height=350, image=bgImg, command=lambda:btnClick(btn9, 9))
btn10=Button(mW, width=200, height=350, image=bgImg, command=lambda:btnClick(btn10, 10))
btn11=Button(mW, width=200, height=350, image=bgImg, command=lambda:btnClick(btn11, 11))

btn0.grid(row=0, column=0, sticky=N+S+E+W)
btn1.grid(row=0, column=1, sticky=N+S+E+W)
btn2.grid(row=0, column=2, sticky=N+S+E+W)
btn3.grid(row=0, column=3, sticky=N+S+E+W)
btn4.grid(row=0, column=4, sticky=N+S+E+W)
btn5.grid(row=0, column=5, sticky=N+S+E+W)
btn6.grid(row=1, column=0, sticky=N+S+E+W)
btn7.grid(row=1, column=1, sticky=N+S+E+W)
btn8.grid(row=1, column=2, sticky=N+S+E+W)
btn9.grid(row=1, column=3, sticky=N+S+E+W)
btn10.grid(row=1, column=4, sticky=N+S+E+W)
btn11.grid(row=1, column=5, sticky=N+S+E+W)

mW.grid_columnconfigure(0, weight=1)
mW.grid_columnconfigure(1, weight=1)
mW.grid_columnconfigure(2, weight=1)
mW.grid_columnconfigure(3, weight=1)
mW.grid_columnconfigure(4, weight=1)
mW.grid_columnconfigure(5, weight=1)
mW.grid_rowconfigure(0, weight=1)
mW.grid_rowconfigure(1, weight=1)



mW.mainloop()