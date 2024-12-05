from tkinter import *
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer
import pyttsx3
import PyPDF2
import threading
from googletrans import Translator
from gtts import gTTS
from tkinter import ttk 
import time

engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    pass

def openfile():
    root.filename=filedialog.askopenfile(initialdir="\E:\projects\AudioBook",title="Your Pdf",filetypes=[("pdf files","*.pdf")])
    la=Label(root,text=f"File_Nmae: {root.filename.name}",bg="#ffbd59").place(x=550,y=0)
    pdf=tkPDFViewer.ShowPdf()
    viwe=pdf.pdf_view(root,pdf_location=open(root.filename.name),height=26,width=70)
    viwe.place(x=125,y=60)

def playaudio():
    book = open(root.filename.name, 'rb')
    start=int(pageentry.get())
    if pausethread:
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
        for num in range(start, pages):
            page = pdfReader.getPage(num)
            text = page.extractText()
            speak(text)
            engine.runAndWait()
def run():
    threading.Thread(target=playaudio).start()

def changevoice():
    val=v.get()
    engine.setProperty('voice', voices[val].id)

def download():
    global loaded
    translator=Translator()
    valu=dv.get()
    st=""
    if root.filename.name:
        book = open(root.filename.name, 'rb')
        start=int(pageentry.get())
        if pausethread:
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.numPages
            for num in range(start, pages):
                page = pdfReader.getPage(num)
                text = page.extractText()
                if valu==3:
                    spa=translator.translate(text,'es').text
                    st=st+spa
                elif valu==2:
                    hin=translator.translate(text,'hi').text  
                    st=st+hin
                else:
                    eng=translator.translate(text,'en').text  
                    st=st+eng        
            audio=gTTS(st)
            audio.save(f"{root.filename.name}.mp3")
            loaded=2
def downloadthread():
      blesslabel.configure(text="Download Started")
      threading.Thread(target=download).start()
def stop():
    global loaded
    if loaded==2:
        blesslabel.configure(text="Download complete")
    else:
        pass
    blesslabel.after(1,stop)

loaded=0
tt1=0
pausethread=1
root=Tk()
root.geometry("900x500")
root.maxsize("900","500")
root.configure(bg="white")
root.title("PDFAudio")
bimg=PhotoImage(file=r"E:\projects\AudioBook\Welcome to pdfaudio.png")
blabel=Label(root,image=bimg)
blabel.place(x=0,y=0,relheight=1,relwidth=1)
filebton=Button(root,text="File 📂",command=openfile,bg="#ffbd59",font="Georgia 13")
filebton.place(x=710,y=50)
playbton=Button(root,text="play ▶",command=run,bg="#ffbd59",font="Georgia 13")
playbton.place(x=780,y=50)
downbton=Button(root,text="Download mp3",command=downloadthread,bg="#ffbd59",font="Georgia 13")
downbton.place(x=710,y=190)
blesslabel=Label(root,bg="#ffbd59",font="Georgia 13")
blesslabel.place(x=710,y=480)
downvoicelabel=Label(root,text=" Dwnload Voices:",bg="#ffbd59",font="Georgia 13")
downvoicelabel.place(x=710,y=230)
v=IntVar()
dv=IntVar()
Radiobutton(root,text="Male",variable=v,value=0,command=(changevoice),bg="#ffbd59",font="Georgia 13").place(x=770,y=90)
Radiobutton(root,text="Female",variable=v,value=1,command=(changevoice),bg="#ffbd59",font="Georgia 13").place(x=770,y=120)
Radiobutton(root,text="English",variable=dv,value=1,bg="#ffbd59",font="Georgia 13").place(x=710,y=260)
Radiobutton(root,text="Hindi",variable=dv,value=2,bg="#ffbd59",font="Georgia 13").place(x=710,y=290)
Radiobutton(root,text="Spanish",variable=dv,value=3,bg="#ffbd59",font="Georgia 13").place(x=710,y=320)

voicelablel=Label(root,text="Voices:",bg="#ffbd59",font="Georgia 13").place(x=710,y=90)
pagelablel=Label(root,text="Starting Page:",bg="#ffbd59",font="Georgia 13").place(x=710,y=150)
pageentry=Entry(root,width=5,bg="#ffbd59")
pageentry.insert(0,'0')
pageentry.place(x=820,y=155)
# voicebton=Button(root,text="Change voice",command=changevoice)
# voicebton.pack()
# la=Label(root,text=root.filename.name).pack()
# pdf=tkPDFViewer.ShowPdf()
# viwe=pdf.pdf_view(root,pdf_location=open(root.filename.name),height=50,width=50)
# viwe.pack()
stop()
root.mainloop()