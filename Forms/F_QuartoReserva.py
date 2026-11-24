
# importações

from typing import List
from typing import TYPE_CHECKING    
from Forms.F_QuartoReservaDesign import Form
from Banco.Banco import Banco
from Modelos.Tabelas import Tabelas as tb
from tkinter import messagebox
from datetime import datetime
from datetime import date
import tkinter as tk
from CustomComps.CustomComps import CustomComps as cc
from Styles.Style import Style

if TYPE_CHECKING:
    
    from Forms.F_Principal import F_principal

class F_QuartoReserva(Form):

    def __init__(self, master, fp: "F_principal"):
       
        self.InicializarComponentes(master)
        
        self.fp = fp
        self.list_Hops: List[cc.ComboBox] = []

        # Imcorporando comboBox
        
        dados = Banco.DQL(f""" 
        
            SELECT *

            FROM 

                {tb.Quarto.tabela}
        
        """)

        for dado in dados:

            self.cbb_NomeQuarto.AddItem({ dado[tb.Quarto.t_Nome] : dado[tb.Quarto.n_Id] })

        # comboBox Status

        self.cbb_Status.ent_Box.config(state="readonly")

        for item in tb.Reservas.status:

            self.cbb_Status.AddItem({ item["view"] : item["value"]})

        dados = Banco.DQL(f"""
        
            SELECT * 

            FROM

                { tb.Hospede.tabela }
        """)

        for dado in dados:

           self.cbb_HospResponsavel.AddItem({ dado[ tb.Hospede.t_Nome ] : dado[ tb.Hospede.n_Id ] })
           self.cbb_Hosp.AddItem({ dado[ tb.Hospede.t_Nome ] : dado[ tb.Hospede.n_Id ] })
        

        self.list_Hops.append(self.cbb_HospResponsavel)
        self.list_Hops.append(self.cbb_Hosp)

        self.btn_Confirmar.config(command= lambda:  self.Click_btn_Confirmar())
        self.btn_AddHosp.config(command= lambda: self.Click_btn_AddHosp())

        self.F_Reserva.wait_window()

    #------------------------------ metodos ------------------------------------------------------------------------------------------------/

    def Click_btn_AddHosp(self):

        quarto = Banco.GetDado(
                
                tabela= tb.Quarto.tabela,
                idKey= tb.Quarto.n_Id,
                dadoÌd= self.cbb_NomeQuarto.itemAtual.value

        )

        self.btn_AddHosp.forget()

        frm = tk.Frame(self.frm_Hosps)
        frm.pack(anchor="w", padx=5, pady=(0, 5))
        Style.Frame.Base(frm)

        cbb = cc.ComboBox(frm)
        cbb.pack(side="left")

        # imcorporando ccb

        dados = Banco.DQL(f"""
        
            SELECT *
                    
            FROM 
                
                { tb.Hospede.tabela }

        """)

        for dado in dados:

            cbb.AddItem({ dado[ tb.Hospede.t_Nome ] : dado[ tb.Hospede.n_Id ] })

        self.list_Hops.append(cbb)

        if quarto[0][tb.Quarto.n_Cap] <= len(self.list_Hops): return

        frm_button = tk.Frame(frm, width=30)
        frm_button.pack(side="right", fill="y", padx=(10, 0))
        frm_button.pack_propagate(False)
        Style.Frame.Base(frm_button)
        
        self.btn_AddHosp = tk.Button(
            
            frm_button,
            text="Add",
            command= lambda: self.Click_btn_AddHosp()
        )

        self.btn_AddHosp.pack(fill="both", expand=True)
        Style.Button.Flat(self.btn_AddHosp)

        self.altura += 25

        x = (self.F_Reserva.winfo_screenwidth() - self.lagura)//2
        y = (self.F_Reserva.winfo_screenheight() - self.altura)//2

        self.F_Reserva.geometry(f"{self.lagura}x{self.altura}+{x}+{y}")

    def Click_btn_Confirmar(self):

        # Verificações de campos 

        # Nome Quarto 

        cbb = self.cbb_NomeQuarto 

        if not cbb.ent_Box.get().strip():

            messagebox.showerror("Error", f"Campo { self.lb_NomeQuarto.cget('text')} não pode está vazio")
            if cbb.winfo_exists(): cbb.ent_Box.focus_set()
            return
        
        achou = False

        for item in cbb.list_Items:

            if cbb.ent_Box.get().replace(" ","").lower() == item.viewValue.replace(" ", "").lower(): achou = True

        if not achou:

            messagebox.showerror("Error", "Quarto não encontrado")
            if cbb.winfo_exists(): cbb.ent_Box.focus_set()
            return

        # datas 

        tbm = self.tbm_Data

        datas = tbm.get().split(" até ")

        try:

            datetime.strptime(datas[0], "%d/%m/%Y")

        except:

            messagebox.showerror("Error", "Data de entrada não existe")
            if tbm.winfo_exists(): tbm.focus_set()
            return

        try:

            datetime.strptime(datas[1], "%d/%m/%Y")

        except:

            messagebox.showerror("Error", "Data de saida não existe")
            if tbm.winfo_exists(): tbm.focus_set()
            return

        dataEntrada = datas[0].split("/")
        dataSaida = datas[1].split("/")

        dataEntrada = date(int(dataEntrada[2]), int(dataEntrada[1]), int(dataEntrada[0])) 
        dataSaida = date(int(dataSaida[2]), int(dataSaida[1]), int(dataSaida[0]))

        if dataEntrada > dataSaida:

            messagebox.showerror("Error", "data de entrada não pode ser depois da data de saida")
            if tbm.winfo_exists(): tbm.focus_set()
            return
        
        dados = Banco.DQL(f"""
        
            SELECT *
            
            FROM

                { tb.Reservas.tabela } as 'tbr'

            INNER JOIN

                { tb.Hospede.tabela } as 'tbh' ON tbr.{ tb.Reservas.n_IdHosp } = tbh.{ tb.Hospede.n_Id },
                { tb.Quarto.tabela } as 'tbq' ON tbr.{ tb.Reservas.n_IdQuarto } = tbq.{ tb.Quarto.n_Id }

             WHERE tbr.{tb.Reservas.n_IdQuarto} = {self.cbb_NomeQuarto.itemAtual.value}

        """)

        if dados:
            
            for dado in dados:

                dataEntrada1 = str(dado[tb.Reservas.t_DataEntrda]).split("/")
                dataSaida1 = str(dado[tb.Reservas.t_DataSaida]).split("/")

                dataEntrada1 = date(int(dataEntrada1[2]), int(dataEntrada1[1]), int(dataEntrada1[0])) 
                dataSaida1= date(int(dataSaida1[2]), int(dataSaida1[1]), int(dataSaida1[0]))

                if dataEntrada < dataSaida1 and dataSaida > dataEntrada1:

                    messagebox.showerror("Error", f"Quarto já reservado pra essas data: entra {dataEntrada1} saida {dataSaida1}")
                    if tbm.winfo_exists(): tbm.focus_set()
                    return

            if len(self.list_Hops) > dados[0][ tb.Quarto.n_Cap]:

                messagebox.showerror("Error", f"Hóspedes alem da capacidade do quarto")
                if self.cbb_Hosp.winfo_exists(): self.cbb_Hosp.focus_set()
                return

        for hosp in self.list_Hops:

            dado = Banco.GetDado(
                
                tabela= tb.Hospede.tabela,
                idKey= tb.Hospede.n_Id,
                dadoÌd= hosp.itemAtual.value
            )

            if dado[0][tb.Hospede.n_IdReserva]:

                messagebox.showerror("Error", f"Hóspde: {hosp.itemAtual.viewValue} já está em uma reserva")
                return

            for hosp2 in self.list_Hops:

                if hosp.itemAtual.value == hosp2.itemAtual.value and hosp != hosp2:

                    messagebox.showerror("Error", f"não pode té hóspedes iguais")
                    return

        # hospede

        cbb = self.cbb_HospResponsavel

        if not cbb.ent_Box.get().strip():

            messagebox.showerror("Error", f"Campo { self.lb_HospResponsavel.cget('text')} não pode está vazio")
            if cbb.winfo_exists(): cbb.ent_Box.focus_set()
            return
        
        achou = False

        for item in cbb.list_Items:

            if cbb.ent_Box.get().replace(" ", "").lower() == item.viewValue.replace(" ", "").lower(): achou = True

        if not achou:

            messagebox.showerror("Error", "Hóspede não encontrado")
            if cbb.winfo_exists(): cbb.ent_Box.focus_set()
            return

        for item in self.fp.flt_Reserva.listLinhas:

            if cbb.itemAtual.value == item.dados[ tb.Reservas.n_IdHosp ] and self.cbb_NomeQuarto.itemAtual.value == item.dados[ tb.Reservas.n_IdQuarto ]:

                messagebox.showerror("Error", "Hóspede já possuir reserva nesse quarto")
                if cbb.winfo_exists(): cbb.ent_Box.focus_set()
                return

        # adicionando dados 

        reservaId = Banco.AddDado(
        
            tabela=tb.Reservas.tabela,
            
            dados = {
                
                tb.Reservas.n_IdHosp: self.cbb_HospResponsavel.itemAtual.value,
                tb.Reservas.n_IdQuarto: self.cbb_NomeQuarto.itemAtual.value,
                tb.Reservas.t_Status: self.cbb_Status.itemAtual.value,
                tb.Reservas.t_DataEntrda: datas[0],
                tb.Reservas.t_DataSaida: datas[1],
                tb.Reservas.n_QtdeHosp: len(self.list_Hops)

            }

        )

        for hosp in self.list_Hops:

            Banco.SetDado(
            
                tabela= tb.Hospede.tabela,
                idKey= tb.Hospede.n_Id,
                dadoId= hosp.itemAtual.value,
                
                dados={
                    
                    tb.Hospede.n_IdReserva: reservaId

                }

            )

        self.fp.flt_Reserva.AddItem(
            
            str(reservaId), 
            self.cbb_NomeQuarto.itemAtual.viewValue,
            datas[0],
            datas[1],
            self.cbb_HospResponsavel.itemAtual.viewValue
        )

        self.F_Reserva.destroy()

    #-------------------------------------------------------------------------------------------\







