
# Importações 

import tkinter as tk
from typing import TYPE_CHECKING
from Comps.CustomComps import ComboBox, NumericUpDown
from Styles.Style import Style
from Modelos.Tabelas import Tabelas as tb

if TYPE_CHECKING:

    from F_NovoQuarto import F_NovoQuarto

#------------------------- Form ----------------------------------------------------------------------------------------------------------------------------------------------------------------------/

class Form():

    def InicializarComponentes(self: "F_NovoQuarto", master):
        
        # Janela

        self.F_NovoQuarto = tk.Toplevel(master)

        # Frames

        self.frm_Conteudo = tk.Frame(self.F_NovoQuarto)
        self.frm_NomeQuarto = tk.Frame(self.frm_Conteudo)
        self.frm_StatusQuarto = tk.Frame(self.frm_Conteudo)
        self.frm_TipoQuarto = tk.Frame(self.frm_Conteudo)
        self.frm_CapQuarto = tk.Frame(self.frm_Conteudo)

        # Labels

        self.lb_NomeQuarto = tk.Label(self.frm_NomeQuarto)
        self.lb_StatusQuarto = tk.Label(self.frm_StatusQuarto)
        self.lb_TipoQuarto = tk.Label(self.frm_TipoQuarto)
        self.lb_CapQuarto = tk.Label(self.frm_CapQuarto)

        # Entrys

        self.ent_NomeQuarto = tk.Entry(self.frm_NomeQuarto)
        self.ent_NomeQuarto_text = "Ex: Quarto102"
        self.nud_CapQuarto = NumericUpDown(self.frm_CapQuarto)

        # ComboBoxs

        self.cbb_StatusQuarto = ComboBox(self.frm_StatusQuarto)
        self.cbb_TipoQuarto = ComboBox(self.frm_TipoQuarto)

        # Buttons

        self.btn_Confirmar = tk.Button(self.frm_Conteudo)

    #------------------------- Componentes Janela ---------------------------------/
        
        #
        # frm_Conteudo
        #   

        self.frm_Conteudo.pack(fill="both", expand=True)
        Style.frame.Bord(self.frm_Conteudo)


        #
        # Componentes Multiplos Frames
        #

        list_Frames = [
            
            self.frm_NomeQuarto,
            self.frm_StatusQuarto,
            self.frm_TipoQuarto,
            self.frm_CapQuarto
            
        ]

        for frm in list_Frames:

            frm.config(height=80)
            frm.pack(side="top", fill="x")
            frm.pack_propagate(False)
            Style.frame.Bord(frm)

        #
        # Compoenetes Multiplos Labels
        #

        list_Labels = [
            
            ("Quarto", self.lb_NomeQuarto), 
            ("Status", self.lb_StatusQuarto), 
            ("Tipo", self.lb_TipoQuarto), 
            ("Capacidade", self.lb_CapQuarto) 

        ]
        
        for txt, lb in list_Labels:

            lb.config(text=txt)
            lb.pack(anchor="w", pady=(10, 1), padx=(4, 0))
            Style.label.Hide(lb)

        #
        # Componentes Multiplos
        #

        list_Comps = [
            
            (self.ent_NomeQuarto_text, self.ent_NomeQuarto),
            ("", self.nud_CapQuarto),
            ("", self.cbb_StatusQuarto),
            ("", self.cbb_TipoQuarto)
        ]

        for txt, comp in list_Comps:

            if isinstance(comp, tk.Entry):

                comp.insert(0, txt)
                Style.entry.Bord(comp)

            if isinstance(comp, ComboBox):

                comp.ent_Box.config(state="readonly")

            if isinstance(comp, NumericUpDown):

                comp.SetValueMin(1)
                Style.numericUpDown.Flat(comp)

            comp.pack(anchor="w", padx=(4, 0))

        #
        # btn_Confirmar
        #

        btn = self.btn_Confirmar

        btn.config(text="Confirmar")
        btn.config(command=lambda: self.Click_btn_Confirmar())
        btn.pack(side="bottom", fill="both", expand=True)
        Style.button.Hide(btn)

        #
        # F_NovoQuarto
        #

        altura = 400
        lagura = 400
        x = (self.F_NovoQuarto.winfo_screenwidth() - lagura)//2
        y = (self.F_NovoQuarto.winfo_screenheight() - altura)//2
        
        self.F_NovoQuarto.title("Novo Quarto")
        self.F_NovoQuarto.geometry(f"{lagura}x{altura}+{x}+{y}")
        self.F_NovoQuarto.resizable(False,False)
        self.F_NovoQuarto.transient(master)
        self.F_NovoQuarto.grab_set()

    #--------------------------------------------------------\

#-------------------------------------------------------------------------------------\
