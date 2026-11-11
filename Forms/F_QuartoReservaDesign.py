
#importações

from logging import config
from pydoc import text
import tkinter  as tk
from Styles.Style import Style
from Comps.CustomComps import ComboBox
from Styles.Tema import Config

class Form():

    def InicializarComponentes(self, master):

        # Janela de reserva

        self.F_Reserva = tk.Toplevel(master)

        # Frames

        self.frm_Conteudo = tk.Frame(self.F_Reserva)
        self.frm_NomeQuarto = tk.Frame(self.frm_Conteudo)
        self.frm_Status = tk.Frame(self.frm_Conteudo)
        self.frm_Data = tk.Frame(self.frm_Conteudo)
        self.frm_AddConvidado = tk.Frame(self.frm_Conteudo)

        # Label

        self.lb_NomeQuarto = tk.Label(self.frm_NomeQuarto)
        self.lb_Status = tk.Label(self.frm_Status)
        self.lb_Data = tk.Label(self.frm_Data)
        self.lb_AddConvidado = tk.Label(self.frm_AddConvidado)
        self.lb_DataAte = tk.Label(self.frm_Data)

        # Entry

        self.ent_NomeQuarto = tk.Entry(self.frm_NomeQuarto)
        self.ent_DataEntrada = tk.Entry(self.frm_Data)
        self.ent_DataSaida = tk.Entry(self.frm_Data)
        
        # ComboBox
        self.cbb_Status = ComboBox(self.frm_Status)
        
        # Button
        self.btn_AddConvidado = tk.Button(self.frm_AddConvidado)
        self.btn_Confirmar = tk.Button(self.frm_Conteudo)
       
    #------------------------- Componente Janela --------------------------------------------------/
        
        #
        # frm_Conteudo
        #

        self.frm_Conteudo.pack(fill="both", expand= True)
        Style.frame.Base(self.frm_Conteudo)

        #
        # Componentes Multiplos - Frames
        #
        
        list_frm = (
            
            self.frm_NomeQuarto, 
            self.frm_Status,
            self.frm_Data, 
            self.frm_AddConvidado 
        )

        for frm in list_frm:

            frm.config(height=80)
            frm.pack_propagate(False)
            frm.pack(side="top", fill="x")
            Style.frame.Bord(frm)

        #
        # Componentes Multiplos - Label
        #
        
        list_lb = (
            
            ("Quarto", self.lb_NomeQuarto), 
            ("Status", self.lb_Status),
            ("Data", self.lb_Data), 
            ("Convidado", self.lb_AddConvidado) 

        )

        for txt, lb in list_lb:

            lb.config(text=txt)
            lb.pack(anchor="w", padx=5, pady=(10, 0))
            Style.label.Hide(lb)

            if txt == "Data":

                lb.config(text=txt, font=Config.tema.fonte)
                lb.pack(side="left", padx=10, pady=(0,4))
                Style.label.Hide(lb)




        #
        # Componentes Multiplos - Entry, Combobox, Button
        #

        list_comps = (
            
            ("Ex: Quarto 2", self.ent_NomeQuarto), 
            ("", self.cbb_Status),
            ("Data", self.ent_DataEntrada),
            ("Até", self.lb_DataAte),
            ("Data", self.ent_DataSaida),
            ("Adicionar", self.btn_AddConvidado) 
        )

        for txt, comp in list_comps:

            if isinstance(comp, tk.Entry):
                
                comp.config(text=txt)
                Style.entry.Bord(comp)

            if isinstance (comp, tk.Button):

                comp.config(text=txt)
                Style.button.Hide(comp)


            if isinstance (comp, tk.Label):
                
                comp.config(text=txt, font=Config.tema.fonte)
                Style.label.Hide(comp)


            if txt == "Data" or txt == "Até":
                
                comp.pack(side="left", padx=5)
                continue

            
            comp.pack(anchor="w", padx=5, pady=10)

        self.btn_Confirmar.config(text="Confirmar")
        self.btn_Confirmar.pack(fill="both", expand=True)
        Style.button.Hide(self.btn_Confirmar)

























        #
        # F_Reserva
        #

        altura = 400
        lagura = 400 
        x = (self.F_Reserva.winfo_screenwidth() - lagura)//2
        y = (self.F_Reserva.winfo_screenheight() - altura)//2
        self.F_Reserva.title("Reserva de Quarto")
        self.F_Reserva.geometry(f"{lagura}x{altura}+{x}+{y}")
        self.F_Reserva.resizable(False, False)
        self.F_Reserva.transient(master)
        self.F_Reserva.grab_set()




    #---------------------------------------------------------------------------\
    






















