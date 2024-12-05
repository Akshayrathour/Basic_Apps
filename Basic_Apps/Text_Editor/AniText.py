from tkinter import *
from PIL import Image, ImageTk
import time

def slideshow():
    global counter
    l=[bgi,bgi2,bgi3]
    la.configure(image=l[counter])
    counter+=1
    if(counter==3):
        counter=0
    la.after(5000,slideshow)

counter=0
root=Tk()
root.geometry("900x500")
bgi=ImageTk.PhotoImage(file=r"E:\projects\Text_Editor\7bd578c3566d211c5438141eaab9597f.jpg")
bgi2=ImageTk.PhotoImage(file=r"E:\projects\Text_Editor\864125.jpg")
bgi3=ImageTk.PhotoImage(file=r"E:\projects\Text_Editor\Demon-slayer-entertainment-district-arc-episode-5-release-date.jpg")
la=Label(root,image=bgi)
la.pack()
slideshow()
root.mainloop() 