
# Importações

import tkinter as tk
from Styles.Style import Style
from Styles.Tema import Config

#----------------------------- Form --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------/


class Form:

    def InicializarComponentes(self,master):

        # Janela

        self.F_HospObs = tk.Toplevel()

        # Frame

        self.frm_Conteudo = tk.Frame(self.F_HospObs)
        
        
        # Label

        self.lb_HospObs = tk.Label(self.frm_Conteudo)

        # Entry

        self.txt_HospObs = tk.Text(self.frm_Conteudo)

        # Button

        self.btn_HospObs = tk.Button(self.frm_Conteudo)
        
    #------------------------- Componente Janela --------------------------------------------------/

        #
        # frm_Conteudo
        #

        self.frm_Conteudo.pack(fill="both", expand= True)
        self.frm_Conteudo.pack_propagate(False)
        Style.Frame.Base(self.frm_Conteudo)

        #
        # lb_HospObs
        #

        self.lb_HospObs.config(text="Observações")
        self.lb_HospObs.pack(anchor="w")
        Style.Label.Hide(self.lb_HospObs)

        #
        # txt_HospObs
        #

        self.txt_HospObs.config(width= 200, height=14)
        self.txt_HospObs.pack(anchor="w")
        

        #
        # btn_SalvarObs
        #

        self.btn_HospObs.config(text="Salvar", height=3)
        self.btn_HospObs.pack(side="bottom")
        Style.Button.Hide(self.btn_HospObs)

        #
        # F_HospObs
        #

        self.altura = 300
        self.lagura = 360 
        x = (self.F_HospObs.winfo_screenwidth() - self.lagura)//2
        y = (self.F_HospObs.winfo_screenheight() - self.altura)//2
        self.F_HospObs.title("Observações do Hospede")
        self.F_HospObs.geometry(f"{self.lagura}x{self.altura}+{x}+{y}")
        self.F_HospObs.resizable(False, False)
        self.F_HospObs.transient(master)
        self.F_HospObs.grab_set()

    #---------------------------------------------------------------------------\
    
   
