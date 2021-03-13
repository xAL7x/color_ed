from tkinter import *
from tkinter import colorchooser
color=Tk()
color.title("color")
color.geometry("400x400")
color.configure(bg="#00074a")
hassan=Label(color,text="created by hassan alharbi").pack(pady=5)
def color2():
    
    color3=colorchooser.askcolor()[1]
    lab2=Label(color,text=color3,font=("Helvetica",32),bg=color3).pack(pady=15)
button=Button(color,text="choose color",command=color2).pack()
color.mainloop()