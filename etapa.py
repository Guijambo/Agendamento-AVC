from os import error
import sqlite3
from sqlite3.dbapi2 import Error
from conexao import Conexao


class Cadastro:

    def cadastrar(self, id, nome, idade, cpf, sexo, datac, localc):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'INSERT INTO cadastro (nome, idade, cpf, sexo, datac, localc) VALUES (?, ?, ?, ?, ?, ?)'
            cursor.execute(sql, [nome, idade, cpf,
                           sexo, datac, localc])

            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro no cadastro do agendamento: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False

    def consultar(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:
            resultset = cursor.execute('SELECT * FROM cadastro').fetchall()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset

    def atualizar(self, id, nome, idade, cpf, sexo, datac, localc):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'UPDATE cadastro SET nome = ?, idade = ?, cpf = ?, sexo = ?, datac = ?, localc = ? WHERE id = (?)'
            cursor.execute(sql, [nome, idade, cpf, sexo, datac, localc, id])

            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na atualização do Cadastro: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False

    def excluir(self, id):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'DELETE FROM cadastro WHERE id = (?)'
            cursor.execute(sql, [id])

            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na exclusão da Etapa: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de inegridade: {}".format(e))
            return False
