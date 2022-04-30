from tkinter import  *
root=Tk()
a=Canvas(root,width=500,height=500)
a.pack()
b=a.create_oval(500, 50,5,5)
root.mainloop()

