import tkinter
import cinematics
from tkinter import PanedWindow, font
import pygame

def prueba():
    pygame.init()
    # grav = float(entries[0].get())
    # vel = float(entries[1].get())
    # ang = float(entries[2].get())
    # if grav != " " and vel != " " and ang != " ":

    cinematics.game()

# root window
root = tkinter.Tk()
root.geometry("600x400")
root.title('Login')
root.resizable(0, 0)

labels = ["Gravity", "Initial Velocity", "Angle"]
entries = []
lbl1 = tkinter.Label(root, text="Parabolic motion simulator", bg="#01579b", fg="white", font="none 24 bold")
lbl1.config(anchor=tkinter.CENTER)
lbl1.pack(fill=tkinter.BOTH)


for label in labels:
    tkinter.Label(root, text=label, font="Arial 16",pady=10).pack()
    entry = tkinter.Entry(root, highlightthickness=0, borderwidth=0)
    entry.pack()
    entries.append(entry)

boton = tkinter.Button(text="Simulate", highlightthickness=0,borderwidth=1,command=prueba)
boton.pack()


root.mainloop()
