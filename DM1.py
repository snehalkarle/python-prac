from gtts import gTTS
import os
mytext = input("enter the text : ")
language = 'de'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("output.mp3")
os.system("start output.mp3")
