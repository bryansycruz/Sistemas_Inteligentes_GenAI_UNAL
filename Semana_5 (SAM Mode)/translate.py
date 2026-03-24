from gtts import gTTS

text = "There is a dog and a cat"
tts = gTTS(text=text, lang='en')

tts.save("audio.mp3")