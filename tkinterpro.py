from tkinter import *
root=Tk()
a=Label(root,text="Username")
a1=Label(root,text="Contact Number")
a2=Label(root,text="Email ID")
a3=Label(root,text="Age")
a4=Label(root,text="Password")
a5=Label(root,text="re-enter password")
b1=Button(root,text="getin",fg="black")
b2=Button(root,text="cancel",fg="black")

c=Entry(root)
c1=Entry(root)
c2=Entry(root)
c3=Entry(root)
c4=Entry(root)
c5=Entry(root)
a.grid(row=0,column=0)
c.grid(row=0,column=3)
a1.grid(row=1,column=0)
c1.grid(row=1,column=3)
a2.grid(row=2,column=0)
c2.grid(row=2,column=3)
a3.grid(row=3,column=0)
c3.grid(row=3,column=3)
a4.grid(row=4,column=0)
c4.grid(row=4,column=3)
a5.grid(row=5,column=0)
c5.grid(row=5,column=3)

b1.grid(row=6,column=3)
b2.grid(row=6,column=4)

root.mainloop()


# from tkinter import *
# root = Tk()
# canvas = Canvas(root, width = 300, height = 300)
# canvas.pack()
# img = PhotoImage(file="ball.ppm")
# canvas.create_image(20,20, anchor=NW, image=img)
# mainloop()