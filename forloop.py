import speech_recognition as sr
aud_file = ("voice.wav")
r = sr.Recognizer()
with sr.AudioFile(aud_file) as source:
    audio = r.record(source)
try:
    print("Audio file contents are:\n"+r.recognize_google(audio))
    f = open("pp.txt","w")
    f.write(r.recognize_google(audio))
    f.close()


except sr.UnknownValueError:
    print("Google couldn't read audio")
except sr.RequestError:
    print("Google is not responding")

