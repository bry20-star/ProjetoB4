
#importações

import tkinter  as tk
from Styles.Style import Style
from CustomComps.CustomComps import CustomComps as cc

class Form():

    def InicializarComponentes(self, master):

        # Janela de reserva

        self.F_Reserva = tk.Toplevel(master)

        # Frames

        self.frm_Conteudo = tk.Frame(self.F_Reserva)
        self.frm_NomeQuarto = tk.Frame(self.frm_Conteudo)
        self.frm_Status = tk.Frame(self.frm_Conteudo)
        self.frm_Data = tk.Frame(self.frm_Conteudo)
        self.frm_HospResponsavel = tk.Frame(self.frm_Conteudo)
        self.frm_Hosps = tk.Frame(self.frm_Conteudo)
        self.frm_CardHosp = tk.Frame(self.frm_Hosps)
        self.frm_HospsButton = tk.Frame(self.frm_CardHosp)

        # Label

        self.lb_NomeQuarto = tk.Label(self.frm_NomeQuarto)
        self.lb_Status = tk.Label(self.frm_Status)
        self.lb_Data = tk.Label(self.frm_Data)
        self.lb_HospResponsavel = tk.Label(self.frm_HospResponsavel)
        self.lb_Hosps = tk.Label(self.frm_Hosps)

        # Entry

        self.tbm_Data = cc.TextBoxMask(self.frm_Data)
        
        # ComboBox

        self.cbb_NomeQuarto = cc.ComboBox(self.frm_NomeQuarto)
        self.cbb_Status = cc.ComboBox(self.frm_Status)
        self.cbb_HospResponsavel = cc.ComboBox(self.frm_HospResponsavel)
        self.cbb_Hosp = cc.ComboBox(self.frm_CardHosp)

        # Button

        self.btn_Confirmar = tk.Button(self.frm_Conteudo)
        self.btn_AddHosp = tk.Button(self.frm_HospsButton)
       
    #------------------------- Componente Janela --------------------------------------------------/
        
        #
        # frm_Conteudo
        #

        self.frm_Conteudo.pack(fill="both", expand= True)
        Style.Frame.Base(self.frm_Conteudo)

        #
        # frm_HospsButton
        #

        self.frm_HospsButton.config(width=30)
        self.frm_HospsButton.pack(side="right", fill="y", padx=(10,0))
        self.frm_HospsButton.pack_propagate(False)
        Style.Frame.Base(self.frm_HospsButton)

        #
        # Componentes Multiplos - Frames
        #
        
        list_frm = (
            
            self.frm_NomeQuarto, 
            self.frm_Status,
            self.frm_Data, 
            self.frm_HospResponsavel,
            self.frm_Hosps
        )

        for frm in list_frm:

            frm.config(height=80)
            if frm != self.frm_Hosps:  frm.pack_propagate(False)
            frm.pack(side="top", fill="x")
            Style.Frame.Bord(frm)

        #
        # Componentes Multiplos - Label
        #
        
        list_lb = (
            
            ("Quarto", self.lb_NomeQuarto),
            ("Data", self.lb_Data),
            ("Status", self.lb_Status),
            ("Hóspede Responsavel", self.lb_HospResponsavel),
            ("Hóspedes", self.lb_Hosps)

        )

        for txt, lb in list_lb:

            lb.config(text=txt)
            lb.pack(anchor="w", padx=5, pady=(10, 0))
            Style.Label.Hide(lb)

        #
        # Componentes Multiplos - Entry, Combobox, Button
        #

        list_comps = (
            
            ("", self.cbb_NomeQuarto), 
            ("", self.cbb_Status),
            ("", self.tbm_Data),
            ("", self.cbb_HospResponsavel),
            ("", self.frm_CardHosp),
        )

        for txt, comp in list_comps:

            if isinstance(comp, tk.Entry):
                
                comp.delete(0,tk.END)
                comp.insert(0, txt)
                Style.Entry.Bord(comp)

            if isinstance (comp, tk.Button):

                comp.config(text=txt)
                Style.Button.Hide(comp)
            
            if isinstance(comp, cc.TextBoxMask):

                comp.SetMask("__/__/____ até __/__/____")
                comp.config(width=30)

            if isinstance(comp, tk.Frame):

                Style.Frame.Base(comp)

            comp.pack(anchor="w", padx=5, pady=(0, 5))

        self.btn_Confirmar.config(text="Confirmar")
        self.btn_Confirmar.pack(fill="both", expand=True)
        Style.Button.Hide(self.btn_Confirmar)
        
        #
        # cbb_Hosp
        #

        self.cbb_Hosp.pack(side="left")

        #
        # btn_AddHosp
        #

        self.btn_AddHosp.config(text="Add")
        self.btn_AddHosp.pack(fill="both", expand=True)
        Style.Button.Flat(self.btn_AddHosp)

        #
        # F_Reserva
        #

        self.altura = 500
        self.lagura = 400 
        x = (self.F_Reserva.winfo_screenwidth() - self.lagura)//2
        y = (self.F_Reserva.winfo_screenheight() - self.altura)//2
        self.F_Reserva.title("Reserva Quarto")
        self.F_Reserva.geometry(f"{self.lagura}x{self.altura}+{x}+{y}")
        self.F_Reserva.resizable(False, False)
        self.F_Reserva.transient(master)
        self.F_Reserva.grab_set()

    #---------------------------------------------------------------------------\
    






















