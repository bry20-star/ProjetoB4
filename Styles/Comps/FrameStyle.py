
# importações

import tkinter as tk
from Styles.StyleManager import StyleManager as sm
from Styles.Tema import Config

#---------------------- FrameStyle ---------------------------------------------------------------------/

class FrameStyle:

    @staticmethod
    def Bord(frm: tk.Frame):
        
        tema = Config.tema

        sm.Registra(comp=frm, met=FrameStyle.Bord)

        frm.config(
            
            bg=tema.segundario,
            highlightthickness=1,
            highlightbackground=tema.primario,
            highlightcolor=tema.primario
        )

    @staticmethod
    def Base(frm: tk.Frame):

        tema = Config.tema

        sm.Registra(comp=frm, met=FrameStyle.Base)

        frm.config(
            
            bg=tema.segundario,
       
        )
        
#------------------------------------------------------------------------------------\