from gtts import gTTS
import os
from tkinter import *
root=Tk()
canvas=Canvas(root,width=400,height=300)
canvas.pack()
def txttospeech():
    text=entry.get()
    output = gTTS(text=text, lang="en", slow=False)
    output.save("music.mp3")
    os.system("start music.mp3")
entry=Entry(root)
canvas.create_window(200,180,window=entry)
button=Button(text="start",command=txttospeech)
canvas.create_window(200,230,window=button)
root=mainloop()