import parser
from tkinter import *
root=Tk()
root.title("CALCULATOR")
display=Entry(root)
display.grid(row=1,columnspan=7,sticky=W+E)
# get input
i=0
def number(num):
    global i
    display.insert(i,num)
    i+=1
def delete():
    display.delete(0, 'end')
def backspace():
    x=display.get()
    if len(x):
        new1=x[:-1]
        delete()
        display.insert(0,new1)
    else:
        delete()
        display.insert(0,"ERROR")
# operator adding
def operator(opr):
    global i
    y=len(opr)
    display.insert(i,opr)
    i+=y
#calculation
def calculation():
    entire_string=display.get()
    try:
        ab=parser.expr(entire_string).compile()
        result=eval(ab)
        delete()
        display.insert(0,result)
    except EXCEPTION:
        delete()
        display.insert(0,"error")
# Display numbers
Button(root,text="AC",command=delete,fg="red").grid(row=2,column=0)
Button(root,text="clear",command=backspace,fg="orange").grid(row=2,column=1)
Button(root,text="%",command=lambda :operator("/100")).grid(row=2,column=2)
Button(root,text="/",command=lambda :operator("/")).grid(row=2,column=3)

Button(root,text="   1 ",command=lambda :number(1)).grid(row=3,column=0)
Button(root,text=" 2  ",command=lambda :number(2)).grid(row=3,column=1)
Button(root,text=" 3 ",command=lambda :number(3)).grid(row=3,column=2)
Button(root,text="*",command=lambda :operator("*")).grid(row=3,column=3)

Button(root,text="   4",command=lambda :number(4)).grid(row=4,column=0)
Button(root,text="  5 ",command=lambda :number(5)).grid(row=4,column=1)
Button(root,text=" 6 ",command=lambda :number(6)).grid(row=4,column=2)
Button(root,text="  -",command=lambda :operator("-")).grid(row=4,column=3)

Button(root,text="   7 ",command=lambda :number(7)).grid(row=5,column=0)
Button(root,text="  8 ",command=lambda :number(8)).grid(row=5,column=1)
Button(root,text=" 9 ",command=lambda :number(9)).grid(row=5,column=2)
Button(root,text="+",command=lambda :operator("+")).grid(row=5,column=3)

Button(root,text="exit",command=display.quit,fg="red").grid(row=6,column=0)
Button(root,text="  0 ",command=lambda :number(0)).grid(row=6,column=1)
Button(root,text="  . ").grid(row=6,column=2)
Button(root,text="=",command=calculation,fg="green").grid(row=6,column=3)


root.mainloop()