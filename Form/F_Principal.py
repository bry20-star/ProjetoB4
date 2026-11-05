# importações 
from Banco.Banco import Banco
from Form.F_PrincipalDesign import Form
from Form.F_EditarHospede import F_EditarHospede
from Form.F_Login import F_Login
import tkinter as tk
from tkinter import messagebox

class F_principal(Form):

    def __init__(self):

        F_Login()

        self.InicializarComponentes()

        self.flt_Hospede.AddColuna("ID", "Hóspede", "Tipo Cobrança", "ID Quarto")

        self.CarregarItem_flt_Hospede(Banco.DQL(

            """
            SELECT *,

                CASE

                    WHEN t_TipoCobranca = 'A' THEN 'Anual' 
                    WHEN t_TipoCobranca = 'M' THEN 'Mensal' 
                    WHEN t_TipoCobranca = 'D' THEN 'Diaria'
                    
                END 
                    
                FROM tb_Hospedes
                    
            """
            
        ))

        # self.flt_Hospede.SetColuna(colunaId=0, peso=1)
        # self.flt_Hospede.SetColuna(colunaId=1, peso=2)
        # self.flt_Hospede.SetColuna(colunaId=2, peso=1)
        # self.flt_Hospede.SetColuna(colunaId=3, peso=1)

        self.fp.mainloop()

    def FormAbrir_Click(self, f):

        if f == F_EditarHospede:
            
            if not self.flt_Hospede.linhaAtual: 
                
                messagebox.showerror("Error","Nenhum Hóspede selecionador")
                return 

        f(self.fp, self)

    def MostraFrame_Click(self,frame):

        for i in [self.frm_Home,self.frm_Hospedes,self.frm_Funcionarios, self.frm_Relatorio, self.frm_Config]:

            i.pack_forget()
        
        frame.pack(fill="both", expand=True)

    def btn_ExcluirHospede_Click(self):

        if not self.flt_Hospede.linhaAtual: 
            
            messagebox.showerror("Error","Nenhum Hóspede selecionador")
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

            if not self.ent_BuscarHospede.get().lower() in item.list_cells[1].cget("text").lower():

                item.pack_forget()