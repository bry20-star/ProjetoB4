
# Impotarções

from typing import TYPE_CHECKING
from Forms.F_NovoHospedeDesign import Form
from Banco.Banco import Banco
from tkinter import messagebox
from Modelos.Tabelas import Tabelas as tb

if TYPE_CHECKING:

    from Forms.F_Principal import F_principal

class F_NovoHospede(Form):

    def __init__(self, master, fp: "F_principal"):
        
        self.InicializarComponentes(master)

        self.fp = fp

        self.cbb_TipoCobranca.AddItem({
            
            tb.Hospede.anual["view"] : tb.Hospede.anual["value"],
			tb.Hospede.mensal["view"] : tb.Hospede.mensal["value"],
			tb.Hospede.diaria["view"] : tb.Hospede.diaria["value"]
            
        })

        dados = Banco.DQL(f"""
        
            SELECT *
            
            FROM
                
                {tb.Quarto.tabela}
        """)

        for dado in dados:

            self.cbb_Quarto.AddItem({dado[tb.Quarto.t_Nome]:dado[tb.Quarto.n_Id]})

        self.F_Hosp.wait_window()
        

    def Click_btn_Confirmar(self):

        # Campo Nome

        ent = self.ent_NameHospede

        if ent.get() == self.ent_NameHospede_text:

            messagebox.showerror("Error", f"Nome do hospede não foi definido")
            if ent.winfo_exists(): ent.focus_set()
            return

        if not ent.get().strip():

            messagebox.showerror("Error", f"Campo {self.lb_NameHospede.cget('text')} não pode esta vazio")
            if ent.winfo_exists(): ent.focus_set()
            return

        if not ent.get().replace(" ", "").isalpha():

            messagebox.showerror("Error", f"Campo {self.lb_NameHospede.cget('text')} não pode ter números ou caracters especiais")
            if ent.winfo_exists(): ent.focus_set()
            return

        if "  " in ent.get().strip():

            messagebox.showerror("Error", f"Campo {self.lb_NameHospede.cget('text')} não pode espaços duplos")
            if ent.winfo_exists(): ent.focus_set()
            return

        if len(ent.get().strip()) > 200:

            messagebox.showerror("Error", f"Nome muito grande")
            if ent.winfo_exists(): ent.focus_set()
            return

        for item in self.fp.flt_Hospede.listLinhas:

            if  self.ent_NameHospede.get().replace(" ","").lower() == str(item.dados[tb.Hospede.t_Nome]).replace(" ", "").lower():

                messagebox.showerror("Error", "Hóspede já registrado com esse nome")
                if ent.winfo_exists(): ent.focus_set()
                return

        # Campo Quarto

        cbb = self.cbb_Quarto

        if not cbb.ent_Box.get().strip():

            messagebox.showerror("Error Campo vazio", f"Campo {self.lb_Quarto.cget('text')} não pode está vazio")
            if cbb.winfo_exists(): cbb.focus_set()
            return

        achou = False

        for item in cbb.list_Items:

            if cbb.ent_Box.get().strip().lower() == item.viewValue.lower():

                achou = True
                break

        if not achou:

            messagebox.showerror("Quarto não encontrado", "Quarto não existi na lista")
            if cbb.winfo_exists(): cbb.focus_set()
            return

        # Adicionando dados

        hospId = Banco.AddDado(

            tabela=tb.Hospede.tabela, 
            dados={
            
                tb.Hospede.t_Nome : self.ent_NameHospede.get().strip(),
                tb.Hospede.t_TipoCobranca : self.cbb_TipoCobranca.itemAtual.value,
                tb.Hospede.n_IdQuarto : int(self.cbb_Quarto.itemAtual.value)
            }            
        )

        hosp = self.fp.flt_Hospede.AddItem(str(hospId), self.ent_NameHospede.get().strip(), self.cbb_TipoCobranca.itemAtual.viewValue, self.cbb_Quarto.itemAtual.viewValue)
        
        dados = Banco.DQL(f"""

            SELECT *,

                CASE

                    WHEN {tb.Hospede.t_TipoCobranca} = '{ tb.Hospede.anual["value"] }' THEN '{ tb.Hospede.anual["view"] }' 
                    WHEN {tb.Hospede.t_TipoCobranca} = '{ tb.Hospede.mensal["value"] }' THEN '{ tb.Hospede.mensal["view"] }' 
                    WHEN {tb.Hospede.t_TipoCobranca} = '{ tb.Hospede.diaria["value"] }' THEN '{ tb.Hospede.diaria["view"] }'
                    
                END as 'tipo'
                    
                FROM 

                    {tb.Hospede.tabela} as 'tbh'
                    
                INNER JOIN {tb.Quarto.tabela} as 'tbq' ON tbq.{tb.Quarto.n_Id} = tbh.{tb.Hospede.n_IdQuarto}

                WHERE  {tb.Hospede.n_Id} = {hospId}   
                    
        """)

        hosp.dados = dados[0]

        self.F_Hosp.destroy()