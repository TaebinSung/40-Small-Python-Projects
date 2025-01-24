# convert text from file to audio and play !!

from gtts import gTTS
from playsound import playsound
import os

#set .py execution path, to current path 

os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = 'myText.txt'
with open(file_path, 'rt', encoding='UTF8') as f :
    read_file = f.read()

tts = gTTS(text=read_file, lang='en')

audio_name = "TextFiletoTTS.mp3" 
tts.save(audio_name)

playsound(audio_name)