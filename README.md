# Agendamento-AVC
código em python com sqlite.

#CONEXAO
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

#ETAPA
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

#ETAPA_VIEW
from etapa import Cadastro
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb

class CadastroView:

    def __init__(self, win):
        self.id_selected = None
        self.cadastroCRUD = Cadastro()

        # COMPONENTES DA TABELA
        self.nomeLabel = tk.Label(win, text='Nome')
        self.idadeLabel = tk.Label(win, text='Idade')
        self.cpfLabel = tk.Label(win, text='''CPF''')
        self.sexoLabel = tk.Label(win, text='''Sexo''')
        self.datacLabel = tk.Label(win, text='''Data''')
        self.localcLabel = tk.Label(win, text='''Local''')

        self.nomeEdit = tk.Entry(win, width = 32, bd=3)
        self.idadeEdit = tk.Entry(win, width = 32, bd=3)
        self.cpfEdit = tk.Entry(win, width = 32, bd=3)
        self.sexoEdit = tk.Entry(win, width = 32, bd=3)
        self.datacEdit = tk.Entry(win, width = 32, bd=3)
        self.localcEdit = tk.Entry(win, width = 32, bd=3)

        self.btnCadastrar = tk.Button(win, text='Cadastrar', width = 8, command=self._on_cadastrar_clicked) 
        self.btnAlterar = tk.Button(win, text='Alterar', width = 8, command=self._on_atualizar_clicked) 
        self.btnExcluir = tk.Button(win, text='Excluir', width = 8, command=self._on_deletar_clicked)   
        
        self.etapaList = ttk.Treeview(win, columns=(1, 2, 3, 4, 5, 6, 7), show='headings')
        self.verscrlbar = ttk.Scrollbar(win, orient="vertical", command=self.etapaList.yview)  
        self.verscrlbar.pack(side ='right', fill ='x')
        self.etapaList.configure(yscrollcommand=self.verscrlbar.set)

        self.etapaList.heading(1, text="ID")
        self.etapaList.heading(2, text="Nome")  
        self.etapaList.heading(3, text="Idade")
        self.etapaList.heading(4, text="CPF")
        self.etapaList.heading(5, text="Sexo")
        self.etapaList.heading(6, text="Data")
        self.etapaList.heading(7, text="Local")
        

        self.etapaList.column(1, minwidth=0, width=50)
        self.etapaList.column(2, minwidth=0, width=200)
        self.etapaList.column(3, minwidth=0, width=200)
        self.etapaList.column(4, minwidth=0, width=200)
        self.etapaList.column(5, minwidth=0, width=200)
        self.etapaList.column(6, minwidth=0, width=200)
        self.etapaList.column(7, minwidth=0, width=200)

        self.etapaList.pack()
        self.etapaList.bind("<<TreeviewSelect>>",self._on_mostrar_clicked)
       
        # Posições
        self.nomeLabel.place(x=10, y=1)
        self.idadeLabel.place(x=10, y=31)
        self.cpfLabel.place(x=10, y=61)
        self.sexoLabel.place(x=10, y=91)
        self.datacLabel.place(x=10, y=121)
        self.localcLabel.place(x=10, y=151)


        self.nomeEdit.place(x=107, y=1)
        self.idadeEdit.place(x=107, y=31)
        self.cpfEdit.place(x=107, y=61)
        self.sexoEdit.place(x=107, y=91)
        self.datacEdit.place(x=10, y=121)
        self.localcEdit.place(x=10, y=151)


        self.etapaList.place(x=420, y=0)
        self.verscrlbar.place(x=1423, y=0, height=225)
        self.btnCadastrar.place(x=335, y=10)
        self.btnAlterar.place(x=335, y=50)  
        self.btnExcluir.place(x=335, y=90)

        self.carregar_dados_iniciais_treeView()
        

    def _on_mostrar_clicked(self, event):
        #Seleção da linha que o usuário clicou
        selection = self.etapaList.selection()[0]
        item = self.etapaList.item(selection, "values")
        self.id_selected = item[0]
        

        # Limpar dados
        self.nomeEdit.delete(0, tk.END)
        self.idadeEdit.delete(0, tk.END)
        self.cpfEdit.delete(0, tk.END)
        self.sexoEdit.delete(0, tk.END)
        self.datacEdit.delete(0, tk.END)
        self.localcEdit.delete(0, tk.END)


        # pegar dados selecionados
        selection = self.etapaList.focus()
        item = self.etapaList.item(selection, "values")

        # inserir dados again
        self.nomeEdit.insert(0, item[1])
        self.idadeEdit.insert(0, item[2])
        self.cpfEdit.insert(0, item[3])
        self.sexoEdit.insert(0, item[4])
        self.datacEdit.insert(0, item[5])
        self.localcEdit.insert(0, item[6])


    def carregar_dados_iniciais_treeView(self):
        registros = self.cadastroCRUD.consultar() 

        count = 0
        for item in registros:
            id = item[0]
            nome = item[1]
            idade = item[2]
            cpf = item[3]
            sexo = item[4]
            datac = item[5]
            localc = item[6]

            self.etapaList.insert('','end',iid=count,values=(str(id), nome, idade, cpf, sexo, datac, localc))
            count = count + 1


    def _on_cadastrar_clicked(self):
        nome = self.nomeEdit.get()
        idade = self.idadeEdit.get()
        cpf = self.cpfEdit.get()
        sexo = self.sexoEdit.get()
        datac = self.datacEdit.get()
        localc = self.localcEdit.get()
        
        if  self.cadastroCRUD.cadastrar(id, nome, idade, cpf, sexo, datac, localc):

            for i in self.etapaList.get_children():
                self.etapaList.delete(i)
            self.carregar_dados_iniciais_treeView()
    
            mb.showinfo("Mensagem", "Cadastro executado com sucesso.")    

            # Limpar campos   
            self.nomeEdit.delete(0, tk.END)
            self.idadeEdit.delete(0, tk.END)
            self.cpfEdit.delete(0, tk.END)
            self.sexoEdit.delete(0, tk.END)
            self.datacEdit.delete(0, tk.END)
            self.localcEdit.delete(0, tk.END)

        else:
            mb.showinfo("Mensagem", "Erro no cadastro.") 
            self.nomeEdit.focus_set()
            self.idadeEdit.focus_set()
            self.cpfEdit.focus_set()
            self.sexoEdit.focus_set()
            self.datacEdit.focus_set()
            self.localcEdit.focus_set()


    def _on_atualizar_clicked(self):
        id = self.id_selected
        nome = self.nomeEdit.get()
        idade = self.idadeEdit.get()
        cpf = self.cpfEdit.get()
        sexo = self.sexoEdit.get()
        datac = self.datacEdit.get()
        localc = self.localcEdit.get()

        # cadastra no banco
        self.cadstroCRUD.atualizar(id, nome, idade, cpf, sexo, datac, localc)

        # Pegar dados selecionados
        itemSelecionado = self.etapaList.focus()

        # Atualizar os dados

        self.etapaList.item(itemSelecionado, values=(str(id), nome, idade, cpf, sexo, datac, localc))

        # Limpar os campos texto
        self.nomeEdit.delete(0, tk.END)
        self.idadeEdit.delete(0, tk.END)
        self.cpfEdit.delete(0, tk.END)
        self.sexoEdit.delete(0, tk.END)
        self.datacEdit.delete(0, tk.END)
        self.localcEdit.delete(0, tk.END)



    def _on_deletar_clicked(self):
        # Pega o id do item selecionado
        itemSelecionado = self.etapaList.selection()[0]
        valores = self.etapaList.item(itemSelecionado, "values")
        id = valores[0]

        # Atribui o id para outra variavel
        id_etp = id

        # Exclui a linha toda DA TREEVIEW
        self.etapaList.delete(itemSelecionado)

        # Exclui o item selecionado do banco
        self.cadastroCRUD.excluir(id_etp)

        # Atualiza a TreeView
        for i in self.etapaList.get_children():
            self.etapaList.delete(i)
        self.carregar_dados_iniciais_treeView()



"""janela=tk.Tk()
principal=CadastroView(janela)
janela.title('Agendamento')
janela.geometry("1440x230+0+0")
janela.mainloop()"""

#MENUBAR
import tkinter as tk
import os
from etapa_view import CadastroView
from conexao import Conexao

class MenuBar:
    def __init__(self, window):
        self.window = window

        menuBar = tk.Menu(window)

        vacinaMenu = tk.Menu(menuBar, tearoff = False)
        vacinaMenu.add_command(label = "Cadastro", command=self._open_cadastro)
        vacinaMenu.add_command(label = "Sair", command=window.destroy)
        menuBar.add_cascade(menu = vacinaMenu, label = "Cadastro")

  
        """bancoMenu = tk.Menu(menuBar, tearoff = False)
        bancoMenu.add_command(label = "Criar DB", command=self._criar_banco)
        menuBar.add_cascade(menu = bancoMenu, label = "Banco")"""

        
        window.config(menu=menuBar)

    def _open_cadastro(self):
        janela=tk.Toplevel(self.window)
        janela.title('Cadastro de Vacinação COVID-19')
        janela.geometry("1440x230+0+0")
        principal= CadastroView(janela)
        janela.mainloop()


    """def _criar_banco(self):
        file = 'projeto.db'
        location = os.path.dirname(os.path.abspath("projeto.db"))
        path = os.path.join(location, file)
        os.remove(path)



        conn = Conexao()
        conn.createTables()"""

#APPLICATION
import tkinter
from menuBar import MenuBar
  
class Application:
    def __init__(self):
        window = tkinter.Tk()
        window.minsize(1024, 1024)
        mb = MenuBar(window)
        window.title('Agendamento Vacinação contra COVID-19 (AVC-19))')
        window.geometry('{}x{}+0+0'.format(*window.maxsize()))
        window.configure(background='#e65353')
        window.mainloop()
 
if __name__ == '__main__': 
    Application()
