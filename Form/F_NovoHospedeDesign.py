import tkinter as tk
from Styles.Style import TemaConfig
from Styles.Style import Style
from Componentes.ComponentesPersonalizados import ComboBox 

class Form:

    def InicializarComponentes(self,master):

        self.F_Hosp = tk.Toplevel()

        self.frm_Conteudo = tk.Frame(self.F_Hosp)
        self.frm_NameHospede = tk.Frame(self.frm_Conteudo)
        self.frm_TipoCobranca = tk.Frame(self.frm_Conteudo)
        self.frm_IdQuarto = tk.Frame(self.frm_Conteudo)
        self.lb_NameHospede = tk.Label(self.frm_NameHospede)
        self.lb_TipoCobranca = tk.Label(self.frm_TipoCobranca)
        self.lb_IdQuarto = tk.Label(self.frm_IdQuarto)
        self.ent_NameHospede = tk.Entry(self.frm_NameHospede)
        self.ent_IdQuarto = tk.Entry(self.frm_IdQuarto)
        self.cbb_TipoCobranca = ComboBox(self.frm_TipoCobranca)
        self.btn_Confirmar = tk.Button(self.frm_Conteudo)
                
        #
        # frm_Conteudo
        #

        self.frm_Conteudo.pack(fill="both", expand=True)
        Style.FrameBord(self.frm_Conteudo) 

        #
        # frm_NameHospede
        #

        self.frm_NameHospede.pack(fill="x", side="top")
        self.frm_NameHospede.config(height=90)
        self.frm_NameHospede.pack_propagate(False)
        Style.FrameBord(self.frm_NameHospede)

        #
        # frm_TipoCobranca
        #

        self.frm_TipoCobranca.pack(fill="x", side="top")
        self.frm_TipoCobranca.config(height=90)
        self.frm_TipoCobranca.pack_propagate(False)
        Style.FrameBord(self.frm_TipoCobranca)

        #
        # frm_IdQuarto
        #

        self.frm_IdQuarto.pack(fill="x", side="top")
        self.frm_IdQuarto.config(height=90)
        self.frm_IdQuarto.pack_propagate(False)
        Style.FrameBord(self.frm_IdQuarto)

        #
        # lb_NameHospede 
        #

        self.lb_NameHospede.pack(anchor="w")
        self.lb_NameHospede.config(height=2, text="Nome do Hóspede")
        Style.LabeHide(self.lb_NameHospede)

        #
        # lb_TipoCobranca
        #

        self.lb_TipoCobranca.pack(anchor="w")
        self.lb_TipoCobranca.config(height=2, text="Tipo de Cobrança")
        Style.LabeHide(self.lb_TipoCobranca)

        #
        # lb_IdQuarto 
        #

        self.lb_IdQuarto.pack(anchor="w")
        self.lb_IdQuarto.config(height=2, text="ID do Quarto")
        Style.LabeHide(self.lb_IdQuarto)

        #
        # ent_NameHospede
        #

        self.ent_NameHospede.pack(anchor="w")
        self.ent_NameHospede.config(width=40)
        Style.EntryBord(self.ent_NameHospede)
        
        #
        # ent_IdQuarto 
        #

        self.ent_IdQuarto.pack(anchor="w")
        Style.EntryBord(self.ent_IdQuarto) 

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
        Style.ButtonHide(self.btn_Confirmar)

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
