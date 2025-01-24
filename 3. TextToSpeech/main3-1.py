#need gtts and soundcloud lib.

from gtts import gTTS
text = "Hi, my name is Taebin. I am a 3rd year UBC student majoring Mathematic. I am trying to study Python with small Python projects!"

tts = gTTS(text=text, lang='en')
tts.save("3. TextToSpeech\\TTSaudio.mp3")