from banco import Banco


class Leciona(object):

    def __init__(self, fk_professor_id=0, fk_disciplina_codigo=0, fk_disciplina_codigo_new=0):
        self.info = {}
        self.fk_disciplina_codigo_new = fk_disciplina_codigo_new
        self.fk_disciplina_codigo = fk_disciplina_codigo
        self.fk_professor_id = fk_professor_id


    def inserelec(self):
        banco = Banco()
        try:
            cur = banco.conexao.cursor()

            sql = "insert into leciona (fk_professor_id, fk_disciplina_codigo) " \
                  "values (" + str(self.fk_professor_id) + ", " + str(self.fk_disciplina_codigo) + ")"

            cur.execute(sql)
            banco.conexao.commit()
            banco.conexao.close()

            return "Relacionamento cadastrado com sucesso!"

        except:
            return "Ocorreu um erro na inserção do relacionamento"

    def alteralec(self):
        banco = Banco()
        try:
            cur = banco.conexao.cursor()

            sql = "update leciona set fk_disciplina_codigo = " + str(self.fk_disciplina_codigo_new) + \
                  " where fk_professor_id = " + str(self.fk_professor_id) + \
                  " and fk_disciplina_codigo = " + str(self.fk_disciplina_codigo) + ";"

            cur.execute(sql)
            banco.conexao.commit()
            banco.conexao.close()

            return "Relacionamento alterado com sucesso!"

        except:
            return "Ocorreu um erro na alteração do relacionamento"

    def excluilec(self):
        banco = Banco()
        try:
            cur = banco.conexao.cursor()

            sql = "delete from leciona where fk_professor_id = " + str(self.fk_professor_id) + \
                  " and fk_disciplina_codigo = " + str(self.fk_disciplina_codigo) + ";"

            cur.execute(sql)
            banco.conexao.commit()
            banco.conexao.close()

            return "Relacionamento excluido com sucesso!"

        except:
            return "Ocorreu um erro na exclusão do relacionamento"
