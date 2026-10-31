from Banco.Banco import Banco
from Form.F_PrincipalDesign import Form
import tkinter as tk
from tkinter import messagebox

class F_principal(Form):

    def __init__(self):

        self.InicializarComponentes()

        self.CarregarItem_flt_Hospede(Banco.DQL("SELECT * FROM tb_Hospedes"))

    def FormAbrir_Click(self, f):

        f(self.fp)

    def SelectCell(self):
        
       return  

    def MostraFrame_Click(self,frame):

        for i in [self.frm_Home,self.frm_Hospedes,self.frm_Funcionarios, self.frm_Relatorio, self.frm_Config]:

            i.pack_forget()
        
        frame.pack(fill="both", expand=True)

    def btn_ExcluirHospede_Click(self):

        if not self.flt_Hospede.linhaAtual: 
            
            messagebox.showerror("Error","Nenhum item selecionador")
            return

        if (not messagebox.askyesno("Excluir?" ,"Deseja Excluir Hóspede?")): return

        Banco.DeleteDado(int(self.flt_Hospede.linhaAtual.list_cells[0].cget("text")), "tb_Hospedes","n_IdHospede")

        self.flt_Hospede.RemoveItem(self.flt_Hospede.linhaAtual)

    def btn_BuscarHospede_Click(self):

        if self.ent_BuscarHospede.get() == "" or self.ent_BuscarHospede.get() == "Buscar:" : 

            for item in list(self.flt_Hospede.listLinhas):

                item.pack_forget()

            for item in list(self.flt_Hospede.listLinhas):

                item.pack(fill="x", expand=True)
            
            return

        for item in list(self.flt_Hospede.listLinhas):

            item.pack(fill="x", expand=True)

            if not self.ent_BuscarHospede.get() in item.list_cells[1].cget("text"):

                item.pack_forget()