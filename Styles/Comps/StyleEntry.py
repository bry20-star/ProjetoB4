
# importações

import tkinter as tk
from Styles.Tema import Config
from Styles.StyleManager import StyleManager as sm

#--------------------- EntryStyle -------------------------------------------------------------------------------------------------------------------------/

class StyleEntry():

    #------------------ Bord ---------------------------------------------------------------------------------------------------/

    @staticmethod
    def Bord(ent: tk.Entry):

        tema = Config.tema
        
        sm.Registra(comp=ent, met=StyleEntry.Bord)

        ent.config(
            
            bg=tema.primario,
            fg=tema.hover,
            relief="flat",
            highlightthickness=1,
            highlightbackground=tema.primario,
            highlightcolor=tema.destaque,
            readonlybackground=tema.primario

        )

        textInicial = ent.get()

        ent.bind("<Enter>", lambda event: StyleEntry.__Enter_Bord(textInicial,  event))
        ent.bind("<FocusIn>", lambda event: StyleEntry.__Enter_Bord(textInicial, event))
        ent.bind("<Leave>", lambda event: StyleEntry.__Leave_Bord(textInicial, event))
        ent.bind("<FocusOut>", lambda event: StyleEntry.__Leave_Bord(textInicial, event))

    def __Enter_Bord(textInicial: str, event):

        ent: tk.Entry = event.widget

        if ent.get() == textInicial:

            ent.delete(0,tk.END)

        ent.config(bg=Config.tema.hover, fg=Config.tema.texto)

    def __Leave_Bord(textInicial: str, event):

        ent: tk.Entry = event.widget

        if ent.winfo_toplevel().focus_get() == ent: return

        if ent.get() == "":

            ent.insert(0, textInicial)

        ent.config(bg=Config.tema.primario, fg=Config.tema.hover)

    #----------------------------------------------------------------------------------------------------\

#--------------------------------------------------------------------------------------------------------------------------------------\
