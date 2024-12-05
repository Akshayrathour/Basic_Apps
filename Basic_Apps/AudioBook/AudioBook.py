import pyttsx3
import PyPDF2

engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    pass
if __name__=="__main__":
   # y=input("enter your text for which you want audio: ")
    #speak(y)
    book = open('The fourth level chapter 1.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    for num in range(0, pages):
        page = pdfReader.getPage(num)
        text = page.extractText()
        speak(text)
        engine.runAndWait()