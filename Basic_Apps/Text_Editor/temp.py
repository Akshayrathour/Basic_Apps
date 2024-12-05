import tkinter
from tkinter import font

root = tkinter.Tk()  # Start Tk instance
your_font = font.nametofont("TkDefaultFont")
a=(font.families())
print(a)
root.mainloop()