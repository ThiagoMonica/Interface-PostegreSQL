from banco import Banco


class Disciplina(object):

    def __init__(self, codigo=0, nome="", vagas=0, periodo="", sala="", cargahoraria=0,
                 fk_curso_numero=0):
        self.info = {}
        self.fk_curso_numero = fk_curso_numero
        self.cargahoraria = cargahoraria
        self.sala = sala
        self.periodo = periodo
        self.vagas = vagas
        self.codigo = codigo
        self.nome = nome

    def inseredisc(self):
        banco = Banco()
        try:
            cur = banco.conexao.cursor()

            sql = "insert into disciplina (codigo, nome, vagas, periodo, sala, cargahoraria, fk_curso_numero) " \
                  "values (" + str(self.codigo) + ", '" + self.nome + "', " + str(self.vagas) + \
                  ", '" + self.periodo + "', '" + self.sala + "', " + str(self.cargahoraria) + ", " + \
                  str(self.fk_curso_numero) + ")"

            cur.execute(sql)
            banco.conexao.commit()
            banco.conexao.close()

            return "Disciplina cadastrada com sucesso!"

        except:
            return "Ocorreu um erro na inserção da disciplina"

    def alteradisc(self):
        banco = Banco()
        try:
            cur = banco.conexao.cursor()

            sql = "update disciplina set nome = '" + self.nome + "', vagas = " + str(self.vagas) + \
                  ", periodo = '" + self.periodo + "', sala = '" + self.sala + \
                  "', cargahoraria = " + str(self.cargahoraria) + ", fk_curso_numero = " + str(self.fk_curso_numero) + \
                  " where codigo = " + str(self.codigo) + ";"

            cur.execute(sql)
            banco.conexao.commit()
            banco.conexao.close()

            return "Disciplina alterada com sucesso!"

        except:
            return "Ocorreu um erro na alteração da disciplina"

    def excluidisc(self):
        banco = Banco()
        try:
            cur = banco.conexao.cursor()

            sql = "delete from disciplina where codigo = " + str(self.codigo) + ";"

            cur.execute(sql)
            banco.conexao.commit()
            banco.conexao.close()

            return "Disciplina excluida com sucesso!"

        except:
            return "Ocorreu um erro na exclusão da disciplina"
