from tkinter import *
class student:
    def __init__(self,showmark):
        # showmark=Frame(showmark)
        # showmark.pack()
        self.l1=Label(showmark,text="click here to continue",bg="red")
        self.l1.pack()
        self.a=Button(showmark,text="OK",fg="red",command=self.display)
        self.a.pack()
        self.b=Button(showmark,text="cancel",fg="yellow",command=self.display2)
        self.b.pack()
        self.c=Button(showmark,text="exit",fg="green",command=showmark.quit)
        self.c.pack()

    def display(self):
        print("you clicked OK")
    def display2(self):
        print("cancled")

root=Tk()
obj=student(root)
root.mainloop()
