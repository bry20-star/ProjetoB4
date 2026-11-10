
# importações

from Comps.CustomComps import NumericUpDown
from Styles.StyleManager import StyleManager as sm
from Styles.Tema import Config 

#----------------------- NumericUpDownStyle -----------------------------------------------------------------------------------------------------------------------------/

class NumericUpDownStyle():

    #---------------- Flat ------------------------------------------------------------------------------------------------------------------------/

    @staticmethod
    def Flat(nud: NumericUpDown):

        tema = Config.tema

        sm.Registra(comp=nud, met=NumericUpDownStyle.Flat)

        nud.config(
            
            bg=tema.primario

        )

        nud.ent_box.config(
            
            bg=tema.primario,
            fg=tema.hover,
            relief="flat",
            highlightthickness=1,
            highlightbackground=tema.primario,
            highlightcolor=tema.destaque,
            readonlybackground=tema.primario

        )

        nud.ent_box.bind("<Enter>", lambda event: nud.ent_box.config(bg=tema.hover, fg=tema.texto))
        nud.ent_box.bind("<FocusIn>", lambda event: nud.ent_box.config(bg=tema.hover, fg=tema.texto))
        nud.ent_box.bind("<Leave>", lambda evetn: nud.ent_box.config(bg=tema.primario, fg=tema.hover))
        nud.ent_box.bind("<FocusOut>", lambda evetn: nud.ent_box.config(bg=tema.primario, fg=tema.hover))

        for txt, btn in (("-", nud.btn_Down), ("↑",nud.btn_Up)):

            btn.config(
                    
                bg=tema.primario,
                fg=tema.texto,
                text=txt,
                activebackground=tema.click,
                highlightthickness=2,
                activeforeground=tema.destaque,
                relief="flat",
                bd=0,
                font=("Segoe UI",12)

            )

            btn.bind("<Enter>", lambda event, b=btn: b.config(bg=tema.hover))
            btn.bind("<FocusIn>", lambda event, b=btn: b.config(bg=tema.hover))
            btn.bind("<Leave>", lambda event, b=btn: b.config(bg=tema.primario))
            btn.bind("<FocusOut>", lambda event, b=btn: b.config(bg=tema.primario))

    #-----------------------------------------------------------------------------------------------------------------\

#------------------------------------------------------------------------------------------------------------------------------------------\