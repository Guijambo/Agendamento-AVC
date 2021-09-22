import sqlite3


class Conexao:

    def conectar(self):
        conexao = None
        db_path = 'avc.db'
        try:
            conexao = sqlite3.connect(
                db_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)

        except sqlite3.DatabaseError as err:
            print(f"Erro ao conectar o banco de dados {db_path}.")
        return conexao


    def createTableCadVacina(self, conexao, cursor):
        cursor.execute('DROP TABLE IF EXISTS CadVacina')

        sql = """CREATE TABLE "cadastro" (
            "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "nome"	TEXT NOT NULL,
            "idade"	INTEGER NOT NULL,
            "cpf"	INTEGER NOT NULL UNIQUE,
            "sexo"	TEXT NOT NULL,
            "datac" TEXT NOT NULL,
            "localc" TEXT NOT NULL
        );"""

        cursor.execute(sql)
        conexao.commit()


    


    """def createTables(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        self.createTableCadVacina(conexao, cursor)


Conexao().createTables()"""
