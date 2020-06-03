import speech_recognition as sr
aud_file = ("symbol.wav")
r = sr.Recognizer()
with sr.AudioFile(aud_file) as source:
    audio = r.record(source)
try:
    #print("Audio file contents are:\n"+r.recognize_google(audio))
    f = open("audio.txt","w")
    f.write(r.recognize_google(audio))
    f.close()
    f = open("audio.txt", "r")
    f1 = open("mod_audio.txt", "w")

    with f as file:

        # reading each line
            for line in file:

                # reading each word
                for word in line.split():
                    # displaying the words
                    if (word == "exclamation"):
                        f1.write("!\n")
                    elif (word == "modulus"):
                        f1.write("%\n")
                    elif (word == "ampersand"):
                        f1.write("&")
                    elif (word == "star"):
                        f1.write("*")
                    elif (word == "dollar"):
                        f1.write("$")
                    else:
                        f1.write(word)
                        f1.write("\n")


    f.close()
    f1.close()
    f1 = open("mod_audio.txt", "r")
    print(f1.read())


except sr.UnknownValueError:
    print("Google couldn't read audio")
except sr.RequestError:
    print("Google is not responding")
