from Leciona import Leciona
from tkinter import *


class LecApplication:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados do Relacionamento:")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lblfkdisc = Label(self.container2,
                                    text="Código da Disciplina:", font=self.fonte, width=25)
        self.lblfkdisc.pack(side=LEFT)

        self.txtfkdisc = Entry(self.container2)
        self.txtfkdisc["width"] = 25
        self.txtfkdisc["font"] = self.fonte
        self.txtfkdisc.pack(side=LEFT)

        self.lblfkprof = Label(self.container3, text="Código do Professor:",
                             font=self.fonte, width=25)
        self.lblfkprof.pack(side=LEFT)

        self.txtfkprof = Entry(self.container3)
        self.txtfkprof["width"] = 25
        self.txtfkprof["font"] = self.fonte
        self.txtfkprof.pack(side=LEFT)

        self.lblnewdisc = Label(self.container4, text="Código da nova Disciplina:",
                              font=self.fonte, width=25)
        self.lblnewdisc.pack(side=LEFT)

        self.txtnewdisc = Entry(self.container4)
        self.txtnewdisc["width"] = 25
        self.txtnewdisc["font"] = self.fonte
        self.txtnewdisc.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir",
                                font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserelec
        self.bntInsert.pack(side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar",
                                 font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alteralec
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir",
                                 font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluilec
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def inserelec(self):
        user = Leciona()

        user.fk_disciplina_codigo = self.txtfkdisc.get()
        user.fk_professor_id = self.txtfkprof.get()

        self.lblmsg["text"] = user.inserelec()

        self.txtfkdisc.delete(0, END)
        self.txtfkprof.delete(0, END)
        self.txtnewdisc.delete(0, END)


    def alteralec(self):
        user = Leciona()

        user.fk_disciplina_codigo = self.txtfkdisc.get()
        user.fk_professor_id = self.txtfkprof.get()
        user.fk_disciplina_codigo_new = self.txtnewdisc.get()

        self.lblmsg["text"] = user.alteralec()

        self.txtfkdisc.delete(0, END)
        self.txtfkprof.delete(0, END)
        self.txtnewdisc.delete(0, END)

    def excluilec(self):
        user = Leciona()

        user.fk_disciplina_codigo = self.txtfkdisc.get()
        user.fk_professor_id = self.txtfkprof.get()

        self.lblmsg["text"] = user.excluilec()

        self.txtfkdisc.delete(0, END)
        self.txtfkprof.delete(0, END)
        self.txtnewdisc.delete(0, END)
