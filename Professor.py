from banco import Banco


class Professor(object):

    def __init__(self, idprofessor=0, idade=0, linhapesquisa="", email="", nome=""):
        self.info = {}
        self.linhapesquisa = linhapesquisa
        self.idade = idade
        self.idprofessor = idprofessor
        self.email = email
        self.nome = nome

    def insereprof(self):
        banco = Banco()
        try:
            cur = banco.conexao.cursor()

            sql = "insert into professor (id, idade, linhapesquisa, email, nome) " \
                  "values (" + str(self.idprofessor) + ", " + str(self.idade) + ", '" + self.linhapesquisa + \
                  "', '" + self.email + "', '" + self.nome + "' )"

            cur.execute(sql)
            banco.conexao.commit()
            banco.conexao.close()

            return "Professor cadastrado com sucesso!"

        except:
            return "Ocorreu um erro na inserção do professor"

    def altertaprof(self):
        banco = Banco()
        try:
            cur = banco.conexao.cursor()

            sql = "update professor set nome = '" + self.nome + "', idade = " + str(self.idade) + \
                  ", linhapesquisa = '" + self.linhapesquisa + "', email = '" + self.email + \
                  "' where id = " + str(self.idprofessor) + ";"

            cur.execute(sql)
            banco.conexao.commit()
            banco.conexao.close()

            return "Professor alterado com sucesso!"

        except:
            return "Ocorreu um erro na alteração do professor"

    def excluiprof(self):
        banco = Banco()
        try:
            cur = banco.conexao.cursor()

            sql = "delete from professor where id = " + str(self.idprofessor) + ";"

            cur.execute(sql)
            banco.conexao.commit()
            banco.conexao.close()

            return "Professor excluido com sucesso!"

        except:
            return "Ocorreu um erro na exclusão do professor"

