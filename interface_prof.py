from Professor import Professor
from tkinter import *


class ProfApplication:
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
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
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

        self.titulo = Label(self.container1, text="Informe os dados do Professor:")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lblidprofessor = Label(self.container2,
                                    text="ID Professor:", font=self.fonte, width=10)
        self.lblidprofessor.pack(side=LEFT)

        self.txtidprofessor = Entry(self.container2)
        self.txtidprofessor["width"] = 10
        self.txtidprofessor["font"] = self.fonte
        self.txtidprofessor.pack(side=LEFT)

        self.lblnome = Label(self.container3, text="Nome:",
                             font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lblidade = Label(self.container4, text="Idade:",
                              font=self.fonte, width=10)
        self.lblidade.pack(side=LEFT)

        self.txtidade = Entry(self.container4)
        self.txtidade["width"] = 25
        self.txtidade["font"] = self.fonte
        self.txtidade.pack(side=LEFT)

        self.lblemail = Label(self.container5, text="Email:",
                              font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(self.container5)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)

        self.lbllinhapesquisa = Label(self.container6, text="Linha de Pesquisa:",
                                      font=self.fonte, width=20)
        self.lbllinhapesquisa.pack(side=LEFT)

        self.txtlinhapesquisa = Entry(self.container6)
        self.txtlinhapesquisa["width"] = 25
        self.txtlinhapesquisa["font"] = self.fonte
        self.txtlinhapesquisa.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir",
                                font=self.fonte, width=12)
        self.bntInsert["command"] = self.insereprof
        self.bntInsert.pack(side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar",
                                 font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alteraprof
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir",
                                 font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluiprof
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def insereprof(self):
        user = Professor()

        user.idprofessor = self.txtidprofessor.get()
        user.nome = self.txtnome.get()
        user.idade = self.txtidade.get()
        user.email = self.txtemail.get()
        user.linhapesquisa = self.txtlinhapesquisa.get()

        self.lblmsg["text"] = user.insereprof()

        self.txtidprofessor.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtidade.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtlinhapesquisa.delete(0, END)

    def alteraprof(self):
        user = Professor()

        user.idprofessor = self.txtidprofessor.get()
        user.nome = self.txtnome.get()
        user.idade = self.txtidade.get()
        user.email = self.txtemail.get()
        user.linhapesquisa = self.txtlinhapesquisa.get()

        self.lblmsg["text"] = user.altertaprof()

        self.txtidprofessor.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtidade.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtlinhapesquisa.delete(0, END)

    def excluiprof(self):
        user = Professor()

        user.idprofessor = self.txtidprofessor.get()

        self.lblmsg["text"] = user.excluiprof()

        self.txtidprofessor.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtidade.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtlinhapesquisa.delete(0, END)
