from plyer import notification
from gtts import gTTS
import os

def text_to_speech():
    text = "take a break. It's been tweenty minutes you are working. Take care of your eyes"
    my_mp3 = gTTS(text, lang='en', slow= False)
    my_mp3.save('my_audio.mp3')
    os.system('my_audio.mp3')


text_to_speech()

