
# importações

import tkinter as tk
from Styles.Style import Style
from Comps.CustomComps import ComboBox 

#----------------------------- Form --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------/

class Form:

    def InicializarComponentes(self,master):

        # Janela

        self.F_Hosp = tk.Toplevel()

        self.frm_Conteudo = tk.Frame(self.F_Hosp)
        self.frm_NameHospede = tk.Frame(self.frm_Conteudo)
        self.frm_TipoCobranca = tk.Frame(self.frm_Conteudo)
        self.frm_Quarto = tk.Frame(self.frm_Conteudo)

        self.lb_NameHospede = tk.Label(self.frm_NameHospede)
        self.lb_TipoCobranca = tk.Label(self.frm_TipoCobranca)
        self.lb_Quarto = tk.Label(self.frm_Quarto)

        self.ent_NameHospede = tk.Entry(self.frm_NameHospede)

        self.cbb_Quarto = ComboBox(self.frm_Quarto)
        self.cbb_TipoCobranca = ComboBox(self.frm_TipoCobranca)

        self.btn_Confirmar = tk.Button(self.frm_Conteudo)
                
    #----------------------- Componentes Janela --------------------------------------/

        #
        # frm_Conteudo
        #

        self.frm_Conteudo.pack(fill="both", expand=True)
        Style.frame.Bord(self.frm_Conteudo) 

        #
        # frm_NameHospede
        #

        self.frm_NameHospede.pack(fill="x", side="top")
        self.frm_NameHospede.config(height=90)
        self.frm_NameHospede.pack_propagate(False)
        Style.frame.Bord(self.frm_NameHospede)

        #
        # frm_TipoCobranca
        #

        self.frm_TipoCobranca.pack(fill="x", side="top")
        self.frm_TipoCobranca.config(height=90)
        self.frm_TipoCobranca.pack_propagate(False)
        Style.frame.Bord(self.frm_TipoCobranca)

        #
        # frm_IdQuarto
        #

        self.frm_Quarto.pack(fill="x", side="top")
        self.frm_Quarto.config(height=90)
        self.frm_Quarto.pack_propagate(False)
        Style.frame.Bord(self.frm_Quarto)

        #
        # lb_NameHospede 
        #

        self.lb_NameHospede.pack(anchor="w")
        self.lb_NameHospede.config(height=2, text="Nome do Hóspede")
        Style.label.Hide(self.lb_NameHospede)

        #
        # lb_TipoCobranca
        #

        self.lb_TipoCobranca.pack(anchor="w")
        self.lb_TipoCobranca.config(height=2, text="Tipo de Cobrança")
        Style.label.Hide(self.lb_TipoCobranca)

        #
        # lb_Quarto 
        #

        self.lb_Quarto.pack(anchor="w")
        self.lb_Quarto.config(height=2, text="Quarto")
        Style.label.Hide(self.lb_Quarto)

        #
        # ent_NameHospede
        #
        self.ent_NameHospede_text = "ex: Hóspede Nome"
        self.ent_NameHospede.insert(0, self.ent_NameHospede_text)
        self.ent_NameHospede.pack(anchor="w")
        self.ent_NameHospede.config(width=40)
        Style.entry.Bord(self.ent_NameHospede)
        
        #
        # cbb_Quarto 
        #

        self.cbb_Quarto.pack(anchor="w")

        #
        # cbb_TipoCobranca
        #
       
        self.cbb_TipoCobranca.pack(anchor="w")
        self.cbb_TipoCobranca.ent_Box.config(state="readonly")

        #
        # btn_Confirmar
        #

        self.btn_Confirmar.pack(side="bottom", expand=True, fill="both")
        self.btn_Confirmar.config(text="Confirmar")
        self.btn_Confirmar.config(command=lambda: self.Click_btn_Confirmar())
        Style.button.Hide(self.btn_Confirmar)

        #
        # F_NovoHospede
        #

        altura = 350
        lagura = 400
        x = (self.F_Hosp.winfo_screenwidth() - lagura)//2
        y = (self.F_Hosp.winfo_screenheight() - altura)//2
        self.F_Hosp.title("Novo Hóspede")
        self.F_Hosp.geometry(f"{lagura}x{altura}+{x}+{y}")
        self.F_Hosp.resizable(False, False)
        self.F_Hosp.transient(master)
        self.F_Hosp.grab_set()

    #-------------------------------------------------------------------------\

#-----------------------------------------------------------------------------------------------------------------------------------------------\