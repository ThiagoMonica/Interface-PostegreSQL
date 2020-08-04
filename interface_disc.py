from Disciplina import Disciplina
from tkinter import *


class DiscApplication:
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
        self.container8["pady"] = 5
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["padx"] = 20
        self.container9["pady"] = 5
        self.container9.pack()
        self.container10 = Frame(master)
        self.container10["padx"] = 20
        self.container10["pady"] = 10
        self.container10.pack()
        self.container11 = Frame(master)
        self.container11["pady"] = 15
        self.container11.pack()

        self.titulo = Label(self.container1, text="Informe os dados da Disciplina:")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lblcodigo = Label(self.container2,
                                    text="Código Disciplina:", font=self.fonte, width=25)
        self.lblcodigo.pack(side=LEFT)

        self.txtcodigo = Entry(self.container2)
        self.txtcodigo["width"] = 10
        self.txtcodigo["font"] = self.fonte
        self.txtcodigo.pack(side=LEFT)

        self.lblnome = Label(self.container3, text="Nome:",
                             font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lblvagas = Label(self.container4, text="Vagas:",
                              font=self.fonte, width=10)
        self.lblvagas.pack(side=LEFT)

        self.txtvagas = Entry(self.container4)
        self.txtvagas["width"] = 25
        self.txtvagas["font"] = self.fonte
        self.txtvagas.pack(side=LEFT)

        self.lblperiodo = Label(self.container5, text="Período:",
                              font=self.fonte, width=10)
        self.lblperiodo.pack(side=LEFT)

        self.txtperiodo = Entry(self.container5)
        self.txtperiodo["width"] = 25
        self.txtperiodo["font"] = self.fonte
        self.txtperiodo.pack(side=LEFT)

        self.lblsala = Label(self.container6, text="Sala:",
                                      font=self.fonte, width=20)
        self.lblsala.pack(side=LEFT)

        self.txtsala = Entry(self.container6)
        self.txtsala["width"] = 25
        self.txtsala["font"] = self.fonte
        self.txtsala.pack(side=LEFT)

        self.lblcargahoraria = Label(self.container7, text="Carga Horária:",
                             font=self.fonte, width=20)
        self.lblcargahoraria.pack(side=LEFT)

        self.txtcargahoraria = Entry(self.container7)
        self.txtcargahoraria["width"] = 25
        self.txtcargahoraria["font"] = self.fonte
        self.txtcargahoraria.pack(side=LEFT)

        self.lblfkcurso = Label(self.container8, text="Código do Curso:",
                             font=self.fonte, width=20)
        self.lblfkcurso.pack(side=LEFT)

        self.txtfkcurso = Entry(self.container8)
        self.txtfkcurso["width"] = 25
        self.txtfkcurso["font"] = self.fonte
        self.txtfkcurso.pack(side=LEFT)

        self.bntInsert = Button(self.container10, text="Inserir",
                                font=self.fonte, width=12)
        self.bntInsert["command"] = self.inseredisc
        self.bntInsert.pack(side=LEFT)

        self.bntAlterar = Button(self.container10, text="Alterar",
                                 font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alteradisc
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(self.container10, text="Excluir",
                                 font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluidisc
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container11, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def inseredisc(self):
        user = Disciplina()

        user.codigo = self.txtcodigo.get()
        user.nome = self.txtnome.get()
        user.vagas = self.txtvagas.get()
        user.periodo = self.txtperiodo.get()
        user.sala = self.txtsala.get()
        user.cargahoraria = self.txtcargahoraria.get()
        user.fk_curso_numero = self.txtfkcurso.get()

        self.lblmsg["text"] = user.inseredisc()

        self.txtcodigo.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtvagas.delete(0, END)
        self.txtperiodo.delete(0, END)
        self.txtsala.delete(0, END)
        self.txtcargahoraria.delete(0, END)
        self.txtfkcurso.delete(0, END)

    def alteradisc(self):
        user = Disciplina()

        user.codigo = self.txtcodigo.get()
        user.nome = self.txtnome.get()
        user.vagas = self.txtvagas.get()
        user.periodo = self.txtperiodo.get()
        user.sala = self.txtsala.get()
        user.cargahoraria = self.txtcargahoraria.get()
        user.fk_curso_numero = self.txtfkcurso.get()

        self.lblmsg["text"] = user.alteradisc()

        self.txtcodigo.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtvagas.delete(0, END)
        self.txtperiodo.delete(0, END)
        self.txtsala.delete(0, END)
        self.txtcargahoraria.delete(0, END)
        self.txtfkcurso.delete(0, END)

    def excluidisc(self):
        user = Disciplina()

        user.codigo = self.txtcodigo.get()

        self.lblmsg["text"] = user.excluidisc()

        self.txtcodigo.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtvagas.delete(0, END)
        self.txtperiodo.delete(0, END)
        self.txtsala.delete(0, END)
        self.txtcargahoraria.delete(0, END)
        self.txtfkcurso.delete(0, END)