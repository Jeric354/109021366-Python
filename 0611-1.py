from tkinter import *

flag = True

def setBtnText(num):
    global flag
    if num ==0:
        if flag:
            Btn0.config(text ="0")
        else:
            Btn0.config(text="x")  
        Btn0.config(state=DISABLED)     
    elif num ==1:
        if flag:
            Btn1.config(text ="0")
        else:
            Btn1.config(text="x")
        Btn1.config(state=DISABLED)    
    elif num ==2:
        if flag:
            Btn2.config(text ="0")
        else:
            Btn2.config(text="x")
        Btn2.config(state=DISABLED)    
    elif num ==3:
        if flag:
            Btn3.config(text ="0")
        else:
            Btn3.config(text="x")
        Btn3.config(state=DISABLED)    
    elif num ==4:
        if flag:
            Btn4.config(text ="0")
        else:
            Btn4.config(text="x")
        Btn4.config(state=DISABLED)    
    elif num ==5:
        if flag:
            Btn5.config(text ="0")
        else:
            Btn5.config(text="x")
        Btn5.config(state=DISABLED)    
    elif num ==6:
        if flag:
            Btn6.config(text ="0")
        else:
            Btn6.config(text="x")
        Btn6.config(state=DISABLED)    
    elif num ==7:
        if flag:
            Btn7.config(text ="0")
        else:
            Btn7.config(text="x")
        Btn7.config(state=DISABLED)    
    elif num ==8:
        if flag:
            Btn8.config(text ="0")
        else:
            Btn8.config(text="x")
        Btn8.config(state=DISABLED)      
    flag = not flag            

    if Btn0.cget('text') == Btn1.cget('text') and Btn0.cget('text')  == Btn3.cget('text'):
        if Btn0.cget('text') == '0':
            print('play1 win')
        elif Btn0.cget("text") == "x":
            print("play2 win")
    elif Btn3.cget('text') == Btn4.cget('text') and Btn3.cget('text')  == Btn5.cget('text'):
        if Btn3.cget('text') == '0':
            print('play1 win')
        elif Btn3.cget("text") == "x":
            print("play2 win")         
    elif Btn6.cget('text') ==Btn7.cget('text') and Btn6.cget('text')  == Btn8.cget('text'):
        if Btn6.cget('text') == '0':
            print('play1 win')
        elif Btn6.cget("text") == "x":
            print("play2 win")
    elif Btn0.cget('text') ==Btn4.cget('text') and Btn4.cget('text')  == Btn8.cget('text'):
        if Btn0.cget('text') == '0':
            print('play1 win')
        elif Btn0.cget("text") == "x":
            print("play2 win")
    elif Btn2.cget('text') ==Btn4.cget('text') and Btn2.cget('text')  == Btn6.cget('text'):
        if Btn2.cget('text') == '0':
            print('play1 win')
        elif Btn2.cget("text") == "x":
            print("play2 win")
    elif Btn1.cget('text') ==Btn4.cget('text') and Btn1.cget('text')  == Btn7.cget('text'):
        if Btn1.cget('text') == '0':
            print('play1 win')
        elif Btn1.cget("text") == "x":
            print("play2 win")
    elif Btn0.cget('text') ==Btn3.cget('text') and Btn2.cget('text')  == Btn6.cget('text'):
        if Btn2.cget('text') == '0':
            print('play1 win')
        elif Btn2.cget("text") == "x":
            print("play2 win")
    elif Btn2.cget('text') ==Btn5.cget('text') and Btn2.cget('text')  == Btn8.cget('text'):
        if Btn2.cget('text') == '0':
            print('play1 win')
        elif Btn2.cget("text") == "x":
            print("play2 win")


                              
window = Tk()
window.title("cool")
window.geometry("400x400+200-100")
window.rowconfigure(0,weight = 1)
window.rowconfigure(1,weight = 1)
window.rowconfigure(2,weight = 1)
window.columnconfigure(0,weight =1)
window.columnconfigure(1,weight =1)
window.columnconfigure(2,weight =1)

Btn0 =Button(window, text="",command=lambda:setBtnText(0))
Btn0.grid(row=0,column=0, sticky=NSEW)
Btn1 =Button(window, text="",command=lambda:setBtnText(1))
Btn1.grid(row=0,column=1, sticky=NSEW)
Btn2 =Button(window, text="",command=lambda:setBtnText(2))
Btn2.grid(row=0,column=2, sticky=NSEW)

Btn3 =Button(window, text="",command=lambda:setBtnText(3))
Btn3.grid(row=1,column=0, sticky=NSEW)
Btn4 =Button(window, text="",command=lambda:setBtnText(4))
Btn4.grid(row=1,column=1, sticky=NSEW)
Btn5 =Button(window, text="",command=lambda:setBtnText(5))
Btn5.grid(row=1,column=2, sticky=NSEW)

Btn6 =Button(window, text="",command=lambda:setBtnText(6))
Btn6.grid(row=2,column=0, sticky=NSEW)
Btn7 =Button(window, text="",command=lambda:setBtnText(7))
Btn7.grid(row=2,column=1, sticky=NSEW)
Btn8 =Button(window, text="",command=lambda:setBtnText(8))
Btn8.grid(row=2,column=2, sticky=NSEW)

window.mainloop()