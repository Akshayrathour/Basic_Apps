from tkinter import *
from PIL import Image, ImageTk
import glob
from pathlib import Path
import re
# def slideshow():
#     global counter
#     l=[]
#     for img in glob.glob(r"E:\projects\Text_Editor\Images_for_AniText\*"):
#         l.append(img)
#     add=r'"'+l[counter]+'"'
#     bgi=ImageTk.PhotoImage(add)
#     la.configure(image=bgi)
#     counter+=1
#     if(counter==len(l)):
#         counter=0
#     la.after(5000,slideshow)

counter=0
root=Tk()
root.geometry("900x500")
l=["E:\projects\Text_Editor\Images_for_AniText\7bd578c3566d211c5438141eaab9597f.jpg"]
# bgi=ImageTk.PhotoImage(file="E:\projects\Text_Editor\Images_for_AniText\7bd578c3566d211c5438141eaab9597f.jpg")
st=(l[0])
# st=re.sub(r"\\","/",st)
# add=Path(st)
i=Image.open(l[0])
bgi=ImageTk.PhotoImage(file=i)

# bgi2=ImageTk.PhotoImage(file=r"E:\projects\Text_Editor\864125.jpg")
# bgi3=ImageTk.PhotoImage(file=r"E:\projects\Text_Editor\Demon-slayer-entertainment-district-arc-episode-5-release-date.jpg")
# bgi4=ImageTk.PhotoImage(file=r"E:\projects\Text_Editor\Demon-slayer-entertainment-district-arc-episode-5-release-date.jpg")
# bgi5=ImageTk.PhotoImage(file=r"E:\projects\Text_Editor\Demon-slayer-entertainment-district-arc-episode-5-release-date.jpg")
# bgi6=ImageTk.PhotoImage(file=r"E:\projects\Text_Editor\Demon-slayer-entertainment-district-arc-episode-5-release-date.jpg")
# bgi7=ImageTk.PhotoImage(file=r"E:\projects\Text_Editor\Demon-slayer-entertainment-district-arc-episode-5-release-date.jpg")

la=Label(root,image=bgi)
la.pack()
# slideshow()
root.mainloop() 