from tkinter import * 
a = 0
b = 0
def chageText(num):
    lab["text"] = lab["text"] + num



window = Tk()
window.title("cool")
window.geometry("400x350+100+50")
window.config(bg="lightgreen")
window.rowconfigure(1,weight = 1)
window.rowconfigure(2,weight = 1)
window.rowconfigure(3,weight = 1)
window.rowconfigure(4,weight = 1)
window.columnconfigure(0,weight =1)
window.columnconfigure(1,weight =1)
window.columnconfigure(2,weight =1)

lab = Label(window, text='0' ,justify=RIGHT, anchor=E, font=("Monaco", 26, "bold"), bg="LIGHTblue")
lab.grid(row =0 ,column=0, columnspan=3 ,sticky=EW)




btn1 = Button(window, text="1", font=("Monaco", 30, "bold"),command=lambda:chageText('1'))
btn1.grid(row=1, column=0 , sticky=NSEW)
btn2 = Button(window, text="2", font=("Monaco", 30, "bold"),command=lambda:chageText('2'))
btn2.grid(row=1, column=1 , sticky=NSEW)
btn3 = Button(window, text="3",font=("Monaco", 30, "bold"),command=lambda:chageText('3'))
btn3.grid(row=1, column=2 , sticky=NSEW)

btn4 = Button(window, text="7", font=("Monaco", 30, "bold"),command=lambda:chageText('4'))
btn4.grid(row=2, column=0 , sticky=NSEW)
btn5 = Button(window, text="8", font=("Monaco", 30, "bold"),command=lambda:chageText('5'))
btn5.grid(row=2, column=1 , sticky=NSEW)
btn6 = Button(window, text="9",font=("Monaco", 30, "bold"),command=lambda:chageText('6'))
btn6.grid(row=2, column=2 , sticky=NSEW)

btn7 = Button(window, text="7", font=("Monaco", 30, "bold"),command=lambda:chageText('7'))
btn7.grid(row=3, column=0 , sticky=NSEW)
btn8 = Button(window, text="8", font=("Monaco", 30, "bold"),command=lambda:chageText('8'))
btn8.grid(row=3, column=1 , sticky=NSEW)
btn9 = Button(window, text="9",font=("Monaco", 30, "bold"),command=lambda:chageText('9'))
btn9.grid(row=3, column=2 , sticky=NSEW)
btn10 = Button(window, text="0",font=("Monaco", 30, "bold"),command=lambda:chageText('0'))
btn10.grid(row=4, column=0 , sticky=NSEW)
btn11 = Button(window, text="+",font=("Monaco", 30, "bold"),command=lambda:chageText('+'))
btn11.grid(row=4, column=1 , sticky=NSEW)
btn12 = Button(window, text="-",font=("Monaco", 30, "bold"),command=lambda:chageText('-'))
btn12.grid(row=4, column=2 , sticky=NSEW)
btn13 = Button(window, text="=",font=("Monaco", 30, "bold"),command=lambda:chageText('='))
btn13.grid(row=5, column=0 , sticky=NSEW)
btn14 = Button(window, text="*",font=("Monaco", 30, "bold"),command=lambda:chageText('*'))
btn14.grid(row=5, column=1 , sticky=NSEW)
btn15 = Button(window, text="/",font=("Monaco", 30, "bold"),command=lambda:chageText('/'))
btn15.grid(row=5, column=2 , sticky=NSEW)
window.mainloop()