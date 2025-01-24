from gtts import gTTS
from playsound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = "This is a program to play the audio right away after creating it!"

tts = gTTS(text=text, lang="en")
tts.save( "main3-2.mp3" )

playsound( "main3-2.mp3" )