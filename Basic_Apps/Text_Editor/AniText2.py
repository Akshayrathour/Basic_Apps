'''
this is the complete text editor using python with all functionalities such as blod,italic,underline,font change,size change,colorchange,undo,redo,navbar,theme changer,new file creation,updation,deletion and images slideshow as the background and home screen. there is only one problem that is the functionalities only work one at a time nad only for a selected text that is a word cannot be clored abd bold at the same time and such is the case for other functionalities. this problem is not solved yet but will be solved in the future. 
'''
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
from tkinter import ttk

def slideshow():
    global counter,bgi,bgi2,bgi3,bgi4,bgi5,bgi6
    l=[bgi,bgi2,bgi3,bgi4,bgi5,bgi5,bgi6]
    la.configure(image=l[counter])
    counter+=1
    if(counter==len(l)):
        counter=0
    la.after(5000,slideshow)

# setting switch state:
btnState = False

# setting switch state:
themeState = False

# setting switch function:
def switch():
    navRoot.place(x=-300, y=0)
    global btnState
    if btnState is True:
        # create animated Navbar closing:
        for x in range(301):
            navRoot.place(x=-x, y=0)
            topFrame.update()

        # resetting widget colors:
        homeLabel.config(bg="#ff8700")
        topFrame.config(bg="#ff8700")
        root.config(bg="gray17")

        # turning button OFF:
        btnState = False
    else:
        # make root dim:
        homeLabel.config(bg="#252726")
        topFrame.config(bg="#252726")
        root.config(bg="#252726")

        # created animated Navbar opening:
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True

def NewFileOpener():
    switch()
    txt.delete('1.0','end')
    txt.place(x=300,y=50,relheight=1,relwidth=0.8)

def OpenFileOption():
    root.filename=filedialog.askopenfile(initialdir="E:\projects\Text_Editor\Files Created by AniText",filetypes=[('Text Files','*.*')],title='Ani_Text_Files')
    fil=open(root.filename.name,"r")
    content=fil.read()
    fil.close()
    txt.delete('1.0','end')
    txt.insert('1.0',content)
    txt.place(x=300,y=50)

def SaveAsOption():
    root.savefile=filedialog.asksaveasfile(initialdir="E:\projects\Text_Editor\Files Created by AniText",filetypes=[('Text Files','*.txt'),('All Files','*.*')],defaultextension=[('Text Files','*.txt')])
    content2=txt.get('1.0','end')
    fil=open(root.savefile.name,"a")
    fil.write(content2)
    fil.close()

def HomeOption():
    txt.place_forget()
    switch()

def SaveOption():
    filer=open(root.filename.name,"w")
    updatedcontent=txt.get('1.0','end')
    filer.write(updatedcontent)
    filer.close()

def MakeBold():
    bold_font=font.Font(txt,txt.cget('font'))
    bold_font.configure(weight="bold")
    txt.tag_configure("bold",font=bold_font)
    
    cur_tags=txt.tag_names("sel.first")
    if "bold" in cur_tags:
        txt.tag_remove("bold","sel.first","sel.last")
    else:
        txt.tag_add("bold","sel.first","sel.last")

def MakeItalic():
    italic_font=font.Font(txt,txt.cget('font'))
    italic_font.configure(slant="italic")
    txt.tag_configure("italic",font=italic_font)

    cur_tags=txt.tag_names("sel.first")
    if "italic" in cur_tags:
        txt.tag_remove("italic","sel.first","sel.last")
    else:
        txt.tag_add("italic","sel.first","sel.last")

def MakeUnderline():
    underline_font=font.Font(txt,txt.cget('font'))
    underline_font.configure(underline=True)
    txt.tag_configure("underline",font=underline_font)

    cur_tags=txt.tag_names("sel.first")
    if "underline" in cur_tags:
        txt.tag_remove("underline","sel.first","sel.last")
    else:
        txt.tag_add("underline","sel.first","sel.last")

def MakeColored():
    color=colorchooser.askcolor()[1]
    if color:
        color_font=font.Font(txt,txt.cget('font'))
        txt.tag_configure("colored",font=color_font,foreground=color)

        cur_tags=txt.tag_names("sel.first")
        if "colored" in cur_tags:
            txt.tag_remove("colored","sel.first","sel.last")
        else:
            txt.tag_add("colored","sel.first","sel.last")

def MakeSize(x):
    size_font=font.Font(txt,txt.cget('font'))
    size_font.configure(size=size.get())
    txt.tag_configure("mysize",font=size_font)

    txt.tag_add("mysize","sel.first","sel.last")

def ChangeTheme():
    global themeState
    if themeState:
        txt.configure(bg="white",fg="black",insertbackground="black")
        themeState=False
    else:
        txt.configure(bg="gray17",fg="white",insertbackground="white")
        themeState=True

def ChangeFont(x):
    font_font=font.Font(txt,txt.cget('font'))
    print(fontCombo.get())
    font_font.configure(family=fontCombo.get())
    txt.tag_configure("fontstyle",font=font_font)

    txt.tag_add("fontstyle","sel.first","sel.last")

counter=0
root=Tk()
root.title("Ani Text Editor")
root.iconbitmap(r"E:\projects\Text_Editor\Images_for_AniText\Martz90-Circle-Addon2-Notepad.ico")
root.geometry("900x540")
root.configure(bg="gray17")
bgi=ImageTk.PhotoImage(file=r"E:\projects\Text_Editor\Images_for_AniText\7bd578c3566d211c5438141eaab9597f.jpg")
bgi2=ImageTk.PhotoImage(file=r"E:\projects\Text_Editor\Images_for_AniText\864125.jpg")
bgi3=ImageTk.PhotoImage(file=r"E:\projects\Text_Editor\Images_for_AniText\Demon-slayer-entertainment-district-arc-episode-5-release-date.jpg")
bgi4=ImageTk.PhotoImage(file=r"E:\projects\Text_Editor\Images_for_AniText\EvZyiVcXAAklTfD.png")
bgi5=ImageTk.PhotoImage(file=r"E:\projects\Text_Editor\Images_for_AniText\fate_stay_night_wallpaper_by_desert_soul_d2vod71-fullview.jpg")
bgi6=ImageTk.PhotoImage(file=r"E:\projects\Text_Editor\Images_for_AniText\violet-evergarden-leaning-on-tree-cloyon6f2axoyje3.jpg")

# loading Navbar icon image:
navIcon = PhotoImage(file=r"E:\projects\Text_Editor\Images_for_AniText\Untitled design (21).png")
closeIcon = PhotoImage(file=r"E:\projects\Text_Editor\Images_for_AniText\Untitled design (20).png")

la=Label(root)
topFrame =Frame(root, bg="#ff8700")
topFrame.pack(side="top", fill=X)

# Header label text:
homeLabel = Label(topFrame, text="Ani Text Editor", font="arvo 15 italic underline bold", bg="#ff8700", fg="black", height=2, padx=20)
homeLabel.pack(side="right")

# Navbar button:
navbarBtn = Button(topFrame, image=navIcon, bg="#ff8700", activebackground="#ff8700", bd=0, padx=20, command=switch)
navbarBtn.place(x=10, y=10)

# setting Navbar frame:
navRoot = Frame(root, bg="gray17", height=1000, width=300)
navRoot.place(x=-300, y=0)
Label(navRoot, font="Bahnschrift 15", bg="#ff8700", fg="black", height=2, width=300, padx=20).place(x=0, y=0)

# set y-coordinate of Navbar widgets:
y = 80
# option in the navbar:
options = ["New File", "Open File", "Save As","Save", "Home"]
co=[NewFileOpener,OpenFileOption,SaveAsOption,SaveOption,HomeOption]
# Navbar Option Buttons:
for i in range(5):
    Button(navRoot, text=options[i], font="BahnschriftLight 15", bg="gray17", fg="#ff8700", activebackground="gray17", activeforeground="green", bd=0,command=co[i]).place(x=25, y=y)
    y += 40

# Navbar Close Button:
closeBtn = Button(navRoot, image=closeIcon, bg="#ff8700", activebackground="#ff8700", bd=0, command=switch)
closeBtn.place(x=250, y=10)

bold_bton=Button(topFrame,text="B",command=MakeBold,bg="#ff8700",activebackground="green",font="helvetica 8 bold")
bold_bton.place(x=430,y=23)

italic_bton=Button(topFrame,text="I",command=MakeItalic,bg="#ff8700",activebackground="green",font="helvetica 8 bold")
italic_bton.place(x=470,y=23)

underline_bton=Button(topFrame,text="U",command=MakeUnderline,bg="#ff8700",activebackground="green",font="helvetica 8 bold")
underline_bton.place(x=450,y=23)

txt=Text(root,width=1,height=5,bd=0,selectforeground="black",undo=True)

und0_bton=Button(topFrame,text="Undo",command=txt.edit_undo,bg="#ff8700",activebackground="green",font="helvetica 8 bold")
und0_bton.place(x=490,y=23)

redo_bton=Button(topFrame,text="Redo",command=txt.edit_redo,bg="#ff8700",activebackground="green",font="helvetica 8 bold")
redo_bton.place(x=530,y=23)

color_bton=Button(topFrame,text="Color",command=MakeColored,bg="#ff8700",activebackground="green",font="helvetica 8 bold")
color_bton.place(x=570,y=23)

sizeLabel = Label(topFrame, text="Size", font="arvo 10 italic bold", bg="#ff8700", fg="black")
sizeLabel.place(x=165,y=23)

FontLabel = Label(topFrame, text="Font", font="arvo 10 italic bold", bg="#ff8700", fg="black")
FontLabel.place(x=165,y=3)

theme_bton=Button(topFrame,text="Theme☀🌙",command=ChangeTheme,bg="#ff8700",activebackground="green",font="helvetica 8 bold")
theme_bton.place(x=350,y=23)

fonts=font.families()
fontCombo=ttk.Combobox(topFrame,values=fonts)
fontCombo.current(0)
fontCombo.bind('<<ComboboxSelected>>',ChangeFont)
fontCombo.place(x=200,y=3)

sizes=[]
for i in range(1,60):
    sizes.append(i)
size=ttk.Combobox(topFrame,values=sizes)
size.current(10)
size.bind('<<ComboboxSelected>>',MakeSize)
size.place(x=200,y=23)

la.pack()
slideshow()
root.mainloop() 