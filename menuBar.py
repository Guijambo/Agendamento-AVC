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
