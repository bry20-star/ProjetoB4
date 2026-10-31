import tkinter as tk
from Styles.Style import TemaConfig

class Form:

    def InicializarComponentes(self,master):

        self.F_Hosp = tk.Toplevel()

        #
        # F_NovoHospede
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
