import tkinter as tk
from Styles.Style import Style
from Styles.Tema import Tema
from Componentes.ComponentesPersonalizados import FrameSuperio

class Form:

    def InicializarComponentes(self,master):

        self.F_NovaTurma = tk.Toplevel()
        self.frm_Conteudo = tk.Frame(self.F_NovaTurma)
        self.frm_Superio = FrameSuperio(self.frm_Conteudo)
        self.canva = tk.Canvas(self.frm_Conteudo)
        #
        # frm_Conteudo
        #
        self.frm_Conteudo.config(bg=Tema.primario)
        self.frm_Conteudo.pack(fill="both", expand=True)
        #
        # frm_Superio
        #
        self.frm_Superio.config(bg=Tema.primario)
        #
        #
        #
        self.canva.create_line(20,20,200,20)
        self.canva.pack(fill="y", expand=True)
        #
        # F_NovaTurma
        #
        #
        altura = 600
        lagura = 400
        x = (self.F_NovaTurma.winfo_screenwidth() - lagura)//2
        y = (self.F_NovaTurma.winfo_screenheight() - altura)//2
        self.F_NovaTurma.title("Nova Turma")
        self.F_NovaTurma.geometry(f"{lagura}x{altura}+{x}+{y}")
        self.F_NovaTurma.transient(master)
        self.F_NovaTurma.grab_set()
        self.F_NovaTurma.wait_window()
