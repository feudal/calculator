from tkinter import *

window=Tk()
window.wm_title("Calculator")
window.resizable(width=0, height=0)
window.call('wm', 'attributes', '.', '-topmost', '1')

global op,var1,var2
op=None
var1=0
var2=None

def set_digit(digit):
    global var1,var2
    # this condition not allow that number to begin with 0, like 06546
    if str(e1_value.get())=="0" and digit != ".":
        e1.delete(0, END)
    # this condition not allow double imput of a dot
    if digit=="." and "." in str(e1_value.get()):
        return
    # insert digit in the console
    if op==None:
        e1.insert(END,digit)
        var1=e1_value.get()
        print("first")
    else:
        print("second")
        # delte first var1 before we put second var2
        if var2==None:
            e1.delete(0,END)
        e1.insert(END,digit)
        var2=e1_value.get()


def delete():
    e1.delete(0, END)
    e1.insert(END,"0")

    global op,var1,var2
    op=None
    var1=0
    var2=None

def operation(oper):
    global op,var1,var2
    op=oper
    var1=e1_value.get()
    var2=None

def result():
    global var1,var2
    if var2==None:
        return
    if op=="-":
        value=float(var1)-float(var2)
    if op=="+":
        value=float(var1)+float(var2)
    if op=="/":
        value=float(var1)/float(var2)
    if op=="*":
        value=float(var1)*float(var2)
    # transfrom float in int, exemple 21.0 to 21
    if value==int(value):
        value=int(value)
    e1.delete(0, END)
    e1.insert(END,value)
    # in case that user will press equal many times
    var1=value


e1_value=StringVar()
e1=Entry(window,textvariable=e1_value,width=40,justify=RIGHT)
e1.grid(row=0,column=0,columnspan=3)
# e1.insert(0, '0')

b_del=Button(window,text="C",width=10,bg="red",command=delete)
b_del.grid(row=0,column=3)

b7=Button(window,text="7",width=10,command=lambda:set_digit("7"))
b7.grid(row=2,column=0)
b8=Button(window,text="8",width=10,command=lambda:set_digit("8"))
b8.grid(row=2,column=1)
b9=Button(window,text="9",width=10,command=lambda:set_digit("9"))
b9.grid(row=2,column=2)
b_divide=Button(window,text="/",width=10,bg="yellow",command=lambda:operation("/"))
b_divide.grid(row=2,column=3)
b4=Button(window,text="4",width=10,command=lambda:set_digit("4"))
b4.grid(row=3,column=0)
b5=Button(window,text="5",width=10,command=lambda:set_digit("5"))
b5.grid(row=3,column=1)
b6=Button(window,text="6",width=10,command=lambda:set_digit("6"))
b6.grid(row=3,column=2)
b_multiply=Button(window,text="x",width=10,bg="yellow",command=lambda:operation("*"))
b_multiply.grid(row=3,column=3)
b1=Button(window,text="1",width=10,command=lambda:set_digit("1"))
b1.grid(row=4,column=0)
b2=Button(window,text="2",width=10,command=lambda:set_digit("2"))
b2.grid(row=4,column=1)
b3=Button(window,text="3",width=10,command=lambda:set_digit("3"))
b3.grid(row=4,column=2)
b_minus=Button(window,text="-",width=10,bg="yellow",command=lambda:operation("-"))
b_minus.grid(row=4,column=3)
b0=Button(window,text="0",width=10,command=lambda:set_digit("0"))
b0.grid(row=5,column=0)
b_dot=Button(window,text=".",width=10,command=lambda:set_digit("."))
b_dot.grid(row=5,column=1)
b_equal=Button(window,text="=",bg="orange",width=10,command=result)
b_equal.grid(row=5,column=2)
b_plus=Button(window,text="+",width=10,bg="yellow",command=lambda:operation("+"))
b_plus.grid(row=5,column=3)

window.mainloop()
