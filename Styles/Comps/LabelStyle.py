
# importações

import tkinter as tk
from Styles.Tema import Config
from Styles.StyleManager import StyleManager as sm

#-------------- LabelStyle ------------------------------------------------------------------------------------------------------------------------------/

class LabelStyle():

    #--------------------- Hide -----------------------------------------------------------/

    @staticmethod
    def Hide(lb: tk.Label):

        if not lb.master: return

        tema = Config.tema

        sm.Registra(comp=lb, met=LabelStyle.Hide)

        lb.config(

            bg=lb.master["bg"], 
            fg=tema.texto
            
        )

    #---------------------------------------------------------------\
       
#---------------------------------------------------------------------------------------------------------------------------\