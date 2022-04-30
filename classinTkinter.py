from tkinter import *
class myfun:
    def __init__(self,student):
        frame=Frame(student)
        frame.pack()
        self.label1=Label(frame,text="click here to continue").pack()
        self.pbutton=Button(frame, text="ok",command=self.pmsg)
        self.pbutton.pack()
        self.nbutton=Button(frame,text="cancel",command=self.display)
        self.nbutton.pack()
        self.gbutton=Button (frame, text="exit",command=frame.quit)
        self.gbutton.pack(side=LEFT)

    def pmsg(self):
        self.a=print("you clicked ok")
    def display(self):
        self.pbutton.delete()

root=Tk()
obj=myfun(root)
root.mainloop()