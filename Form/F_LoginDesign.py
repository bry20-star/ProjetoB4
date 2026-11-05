# arquivo de desiner

import tkinter as tk
from typing import TYPE_CHECKING
from Styles.Style import Style
from Componentes.ComponentesPersonalizados import ComboBox

if TYPE_CHECKING:

    from F_Login import F_Login

class Form():

    def InicializarComponentes(self: "F_Login"):

        self.F_Login = tk.Tk()


        #
        # F_Login
        #

        altura = 400
        lagura = 400
        x = (self.F_Login.winfo_screenwidth() - lagura)//2
        y = (self.F_Login.winfo_screenheight() - altura)//2
        self.F_Login.title("Login")
        self.F_Login.geometry(f"{lagura}x{altura}+{x}+{y}")
        self.F_Login.resizable(False,False)
