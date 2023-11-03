from tkinter import *
expression=""

def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)
    
def equalpress():
    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("Ërror")
        expression=""
        
def clear():
    global expression
    expression=""
    equation.set("")
    
    
tk=Tk()
tk.configure(background="black")
tk.title("Calculator")
tk.geometry("294x434")
equation=StringVar()
result=Entry(tk,textvariable=equation)
result.grid(columnspan=3,ipadx=30,rowspan=2)
result.place(height=100,width=250)

clear=Button(tk,text='AC',fg='white', bg='black',command=clear,height=5,width=9)
clear.grid(row=1,column=3)

button9=Button(tk,text='9',fg='white', bg='black',command=lambda: press(9), height=5,width=9)
button9.grid(row=2,column=0)

button8=Button(tk,text='8',fg='white', bg='black',command=lambda: press(8), height=5,width=9)
button8.grid(row=2,column=1)

button7=Button(tk,text='7',fg='white', bg='black',command=lambda: press(7), height=5,width=9)
button7.grid(row=2,column=2)

plus=Button(tk,text='+',fg='white', bg='black',command=lambda: press("+"), height=5,width=9)
plus.grid(row=2,column=3)

button4=Button(tk,text='4',fg='white', bg='black',command=lambda: press(4), height=5,width=9)
button4.grid(row=3,column=0)

button5=Button(tk,text='5',fg='white', bg='black',command=lambda: press(5), height=5,width=9)
button5.grid(row=3,column=1)

button6=Button(tk,text='6',fg='white', bg='black',command=lambda: press(6), height=5,width=9)
button6.grid(row=3,column=2)

minus=Button(tk,text='-',fg='white', bg='black',command=lambda: press("-"), height=5,width=9)
minus.grid(row=3,column=3)

button3=Button(tk,text='3',fg='white', bg='black',command=lambda: press(3), height=5,width=9)
button3.grid(row=4,column=0)

button2=Button(tk,text='2',fg='white', bg='black',command=lambda: press(2), height=5,width=9)
button2.grid(row=4,column=1)

button1=Button(tk,text='1',fg='white', bg='black',command=lambda: press(1), height=5,width=9)
button1.grid(row=4,column=2)

divide=Button(tk,text='/',fg='white', bg='black',command=lambda: press("/"), height=5,width=9)
divide.grid(row=4,column=3)

dot=Button(tk,text='.',fg='white', bg='black',command=lambda: press("."), height=5,width=9)
dot.grid(row=5,column=0)

button0=Button(tk,text='0',fg='white', bg='black',command=lambda: press(0), height=5,width=9)
button0.grid(row=5,column=1)

equal=Button(tk,text='=',fg='white', bg='black',command=equalpress, height=5,width=9)
equal.grid(row=5,column=2)

multiply=Button(tk,text='x',fg='white', bg='black',command=lambda: press("*"), height=5,width=9)
multiply.grid(row=5,column=3)

tk.mainloop()
