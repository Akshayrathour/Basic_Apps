from tkinter import *
from tkinter import ttk

root=Tk()
root.geometry("400x400")
ye=ttk.Scrollbar(root,orient=VERTICAL)
rata=Text(root,height=400,width=400)
ye.configure(command=rata.yview)
rata.configure(yscrollcommand=ye.set)
ye.place(y=0,x=390)
rata.place(x=0,y=0)

root.mainloop()