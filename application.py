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
