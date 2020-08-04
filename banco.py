import psycopg2


class Banco:

    def __init__(self):
        self.conexao = psycopg2.connect(host='host', database='database',
                                        user='user', password='password')

