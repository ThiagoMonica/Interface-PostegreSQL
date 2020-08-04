from interface_prof import ProfApplication
from interface_disc import DiscApplication
from interface_lec import LecApplication
from tkinter import *


root = Tk()
root.title("Sistema de Graduação")

var = StringVar(root)
var.set("Professor")  # initial value

option = OptionMenu(root, var, "Professor", "Disciplina", "Leciona")
option.pack()


def ok():
    if var.get() == "Professor":
        ProfApplication(root)
    if var.get() == "Disciplina":
        DiscApplication(root)
    if var.get() == "Leciona":
        LecApplication(root)


button = Button(root, text="OK", command=ok)
button.pack()

root.mainloop()

