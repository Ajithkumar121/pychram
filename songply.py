from gtts import gTTS
import os
text=open("song.txt","r",encoding="utf-8").read()
output=gTTS(text=text,lang="ml",slow=False)
output.save("newsong.mp3")
os.system("start newsong.mp3")


