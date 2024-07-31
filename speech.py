import speech_recognition as speech_recog
from gtts import gTTS
import os

ttslang = 'es'
def speech():
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()
    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        return recog.recognize_google(audio, language="es-ES")
mic = speech_recog.Microphone()
recog = speech_recog.Recognizer()
with mic as audio_file:
    print("Por favor, hable")
    recog.adjust_for_ambient_noise(audio_file)
    audio = recog.listen(audio_file)
    print("Conversión de voz a texto...")
    ttstext = recog.recognize_google(audio, language="es-ES")
    myobj = gTTS(text=ttstext, lang=ttslang, slow=False)
    myobj.save("welcome.mp3")
    os.system("start welcome.mp3")
