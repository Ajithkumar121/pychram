from gtts import gTTS
import os
text="every day is good"
output=gTTS(text=text,lang="ml",slow=False)
output.save("output.mp3")
os.system("start output.mp3")

