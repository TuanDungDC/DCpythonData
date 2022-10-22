#Chương trình chuyển text sang audio
from gtts import gTTS
from playsound import playsound
audio = 'speech.mp3'
language = 'en'
sp = gTTS(text = "Would you please give me some salt? I’d like to put it in my coffee.", lang= language,slow=False)
sp.save(audio)
playsound(audio)