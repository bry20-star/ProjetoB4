import tkinter as tk
from Styles.Style import TemaConfig

class Form:

    def InicializarComponentes(self,master):

        self.F_Hosp = tk.Toplevel()
        self.frm_Conteudo = tk.Frame(self.F_Hosp)
        self.frm_Superio = tk.Frame(self.frm_Conteudo)
        self.canva = tk.Canvas(self.frm_Conteudo)
        #
        # frm_Conteudo
        #
        self.frm_Conteudo.config(bg=TemaConfig.tema.primario)
        self.frm_Conteudo.pack(fill="both", expand=True)
        #
        # frm_Superio
        #
        self.frm_Superio.config(bg=TemaConfig.tema.primario)
        self.frm_Superio.pack_propagate(False)
        self.frm_Superio.pack(side="top", fill="x")
        #
        #
        #
        self.canva.create_line(20,20,200,20)
        self.canva.pack(fill="y", expand=True)
        #
        # F_NovoHospede
        #
        #
        altura = 600
        lagura = 400
        x = (self.F_Hosp.winfo_screenwidth() - lagura)//2
        y = (self.F_Hosp.winfo_screenheight() - altura)//2
        self.F_Hosp.title("Novo Hóspede")
        self.F_Hosp.geometry(f"{lagura}x{altura}+{x}+{y}")
        self.F_Hosp.transient(master)
        self.F_Hosp.grab_set()
        self.F_Hosp.wait_window()
