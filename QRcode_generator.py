from tkinter import *
import pyqrcode
from PIL import ImageTk,Image
root=Tk()
canvas=Canvas(root,width=400,height=650)
canvas.pack()
app_label=Label(root,text="QR Code Generator",fg="black",font=("Arial",30))
canvas.create_window(200,50,window=app_label)

def ajosh():
    link_name=a.get()
    link=b.get()
    file_name=link_name+".png"
    c=pyqrcode.create(link)
    c.png(file_name,scale=5)
    pic=ImageTk.PhotoImage(Image.open(file_name))
    image=Label(image=pic)
    image.image=pic
    canvas.create_window(200,450,window=image)

# creating text Label
name_label=Label(root,text="Link name")
link_label=Label(root,text="Link")
canvas.create_window(200,100,window=name_label)
canvas.create_window(200,170,window=link_label)
# creating box for input
a=Entry(root)
b=Entry(root)
canvas.create_window(200,122,window=a)
canvas.create_window(200,200,window=b)
# QR code generator button
button=Button(text="Generate QR Code",command=ajosh)
canvas.create_window(200,230,window=button)



root=mainloop()
