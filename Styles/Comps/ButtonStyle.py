
# importações

import tkinter as tk
from Styles.Tema import Config
from Styles.StyleManager import StyleManager as sm

#------------------- ButtonStyle ------------------------------------------------------------------------------------------------------------------------------------------------------------/

class ButtonStyle():

    #------------- Flat -------------------------------------------------------------------------------------------------------------------------/

    @staticmethod
    def Flat(comp: tk.Button):

        tema = Config.tema

        sm.Registra(comp=comp, met=ButtonStyle.Flat)

        comp.config(
            
            bg=tema.botao,
            fg=tema.texto,
            activebackground=tema.click,
            highlightthickness=0,
            activeforeground=tema.destaque,
            relief="flat",
            bd=0,
            font=("Segoe UI",12),

        )

        comp.bind("<Enter>", lambda event: comp.config(bg=tema.hover, highlightthickness=2))
        comp.bind("<FocusIn>", lambda event: comp.config(bg=tema.hover, highlightthickness=2))
        comp.bind("<Leave>", lambda event: comp.config(bg=tema.botao, highlightthickness=0))
        comp.bind("<FocusOut>", lambda event: comp.config(bg=tema.botao, highlightthickness=0))

    #-----------------------------------------------------------------------------------------------------\

    #------------- Hide --------------------------------------------------------------------------------------------------/

    @staticmethod
    def Hide(comp: tk.Button):

        if not comp.master: return
        
        tema = Config.tema

        sm.Registra(comp=comp, met=ButtonStyle.Hide)

        comp.config(
            
            bg=comp.master["bg"],
            fg=tema.texto,
            activebackground=comp.master["bg"],
            activeforeground=tema.destaque,
            highlightthickness=0,
            relief="flat",
            padx=0,
            pady=0,
            bd=0,
            font=("Segoe UI",12),

        )

        comp.bind("<Enter>", lambda event: comp.config(bg=comp.master["bg"], fg=tema.hover, font=("Segoe UI",13)))
        comp.bind("<FocusIn>", lambda event: comp.config(bg=comp.master["bg"], fg=tema.hover))
        comp.bind("<Leave>", lambda event: comp.config(bg=comp.master["bg"], fg=tema.texto, font=("Segoe UI",12)))
        comp.bind("<FocusOut>", lambda event: comp.config(bg=comp.master["bg"], fg=tema.texto))

    #-------------------------------------------------------------------------------------------------------------------\

#----------------------------------------------------------------------------------------------\