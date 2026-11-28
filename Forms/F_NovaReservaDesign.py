
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
        self.frm_ReservaNomeQuarto = tk.Frame(self.frm_Conteudo)
        self.frm_StatusReserva = tk.Frame(self.frm_Conteudo)
        self.frm_DataReserva = tk.Frame(self.frm_Conteudo)
        self.frm_ResposavelReserva = tk.Frame(self.frm_Conteudo)
        self.frm_HospsReserva = tk.Frame(self.frm_Conteudo)
        self.frm_CardHospReserva = tk.Frame(self.frm_HospsReserva)
        self.frm_ReservaButton = tk.Frame(self.frm_CardHospReserva)

        # Label

        self.lb_ReservaNomeQuarto = tk.Label(self.frm_ReservaNomeQuarto)
        self.lb_StatusReserva = tk.Label(self.frm_StatusReserva)
        self.lb_DataReserva = tk.Label(self.frm_DataReserva)
        self.lb_ResponsavelReserva = tk.Label(self.frm_ResposavelReserva)
        self.lb_HospsReserva = tk.Label(self.frm_HospsReserva)

        # Entry

        self.tbm_DataReserva = cc.TextBoxMask(self.frm_DataReserva)
        
        # ComboBox

        self.cbb_ReservaNomeQuarto = cc.ComboBox(self.frm_ReservaNomeQuarto)
        self.cbb_StatusReserva = cc.ComboBox(self.frm_StatusReserva)
        self.cbb_ResponsavelReserva = cc.ComboBox(self.frm_ResposavelReserva)
        self.cbb_HospReserva = cc.ComboBox(self.frm_CardHospReserva)

        # Button

        self.btn_Confirmar = tk.Button(self.frm_Conteudo)
        self.btn_AddHosp = tk.Button(self.frm_ReservaButton)
       
    #------------------------- Componente Janela --------------------------------------------------/
        
        #
        # frm_Conteudo
        #

        self.frm_Conteudo.pack(fill="both", expand= True)
        Style.Frame.Base(self.frm_Conteudo)

        #
        # frm_HospsButton
        #

        self.frm_ReservaButton.config(width=30)
        self.frm_ReservaButton.pack(side="right", fill="y", padx=(10,0))
        self.frm_ReservaButton.pack_propagate(False)
        Style.Frame.Base(self.frm_ReservaButton)

        #
        # Componentes Multiplos - Frames
        #
        
        list_frm = (
            
            self.frm_ReservaNomeQuarto, 
            self.frm_StatusReserva,
            self.frm_DataReserva, 
            self.frm_ResposavelReserva,
            self.frm_HospsReserva
        )

        for frm in list_frm:

            frm.config(height=80)
            if frm != self.frm_HospsReserva:  frm.pack_propagate(False)
            frm.pack(side="top", fill="x")
            Style.Frame.Bord(frm)

        #
        # Componentes Multiplos - Label
        #
        
        list_lb = (
            
            ("Quarto", self.lb_ReservaNomeQuarto),
            ("Data", self.lb_DataReserva),
            ("Status", self.lb_StatusReserva),
            ("Hóspede Responsavel", self.lb_ResponsavelReserva),
            ("Hóspedes", self.lb_HospsReserva)

        )

        for txt, lb in list_lb:

            lb.config(text=txt)
            lb.pack(anchor="w", padx=5, pady=(10, 0))
            Style.Label.Hide(lb)

        #
        # Componentes Multiplos - Entry, Combobox, Button
        #

        list_comps = (
            
            ("", self.cbb_ReservaNomeQuarto), 
            ("", self.cbb_StatusReserva),
            ("", self.tbm_DataReserva),
            ("", self.cbb_ResponsavelReserva),
            ("", self.frm_CardHospReserva),
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

        self.cbb_HospReserva.pack(side="left")

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
    






















