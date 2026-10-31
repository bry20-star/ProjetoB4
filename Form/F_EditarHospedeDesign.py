# arquivo de desiner

import tkinter as tk
from typing import TYPE_CHECKING
from Styles.Style import Style
from Styles.Style import TemaConfig

if TYPE_CHECKING:

    from F_EditarHospede import F_EditarHospede

class Form():

    def InicializarComponentes(self: "F_EditarHospede", master):

        self.F_EditarHosp = tk.Toplevel()

        #
        # F_EditarHosp
        #

        altura = 500
        lagura = 600
        x = (self.F_EditarHosp.winfo_screenwidth() - lagura)//2
        y = (self.F_EditarHosp.winfo_screenheight() - altura)//2
        self.F_EditarHosp.title("Editar Hóspede")
        self.F_EditarHosp.geometry(f"{lagura}x{altura}+{x}+{y}")
        self.F_EditarHosp.transient(master)
        self.F_EditarHosp.grab_set()
        self.F_EditarHosp.wait_window()