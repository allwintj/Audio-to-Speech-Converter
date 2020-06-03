from fpdf import FPDF

import speech_recognition as sr
aud_file = ("voice.wav")
r = sr.Recognizer()
with sr.AudioFile(aud_file) as source:
    audio = r.record(source)
try:
    print("Audio file contents are:\n"+r.recognize_google(audio))
    # save FPDF() class into a
    # variable pdf
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size=15)

    # create a cell
    pdf.cell(200, 10, txt=r.recognize_google(audio),
             ln=1, align='C')
    # save the pdf with name .pdf
    pdf.output("my.pdf")


except sr.UnknownValueError:
    print("Google couldn't read audio")
except sr.RequestError:
    print("Google is not responding")

