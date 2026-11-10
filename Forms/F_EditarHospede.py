
# importações

from typing import TYPE_CHECKING
import tkinter as tk
from tkinter import messagebox
from Forms.F_EditarHospedeDesign import Form
from Banco.Banco import Banco
from Styles.Style import Style
from Modelos.Tabelas import Tabelas as tb

if TYPE_CHECKING:

    from Forms.F_Principal import F_principal

#--------------------------------------- F_EditarHospede --------------------------------------------------------------------------------------------------------------------------------------------/

class F_EditarHospede(Form):

	def __init__(self, master, fp: "F_principal"):

		self.InicializarComponentes(master)

		self.linhaAtual = fp.flt_Hospede.linhaAtual
		self.fp = fp

		self.ent_IdHospede.delete(0, tk.END)
		self.ent_IdHospede.insert(0, self.linhaAtual.dados[tb.Hospede.n_Id])
		self.ent_IdHospede.config(state="readonly")

		self.ent_NameHospede.delete(0, tk.END)
		self.ent_NameHospede.insert(0, self.linhaAtual.dados[tb.Hospede.t_Nome])
		Style.entry.Bord(self.ent_NameHospede)

		# combobox - imcorporando

		self.cbb_TipoCobranca.AddItem({
			
			tb.Hospede.anual["view"] : tb.Hospede.anual["value"],
			tb.Hospede.mensal["view"] : tb.Hospede.mensal["value"],
			tb.Hospede.diaria["view"] : tb.Hospede.diaria["value"]
			
		})
		
		self.cbb_TipoCobranca.ent_Box.config(state="readonly")
		self.cbb_TipoCobranca.SetItem(self.linhaAtual.dados["tipo"])

		dados = Banco.DQL(f"""
		
			SELECT *
			
			FROM

				{tb.Quarto.tabela}

		""")

		for dado in dados:

			self.cbb_Quarto.AddItem({dado[tb.Quarto.t_Nome]:dado[tb.Quarto.n_Id]})

		self.cbb_Quarto.SetItem(self.linhaAtual.dados[tb.Quarto.t_Nome])

		self.F_EditarHosp.wait_window()

	#------------------------------------ metodos ------------------------------------------------------------------------------------------------/

	def Click_btn_Confirmar(self):

		# Campo Nome

		ent = self.ent_NameHospede

		if not	ent.get().strip(): 
			
			messagebox.showerror("Error",f"Campo {self.lb_NameHospede.cget('text')} não pode estar vazio")
			if ent.winfo_exists(): ent.focus_set()
			return

		if not ent.get().replace(" ", "").isalpha(): 
			
			messagebox.showerror("Error", f"Campo {self.lb_NameHospede.cget('text')} não pode ter números ou caracters especiais")
			if ent.winfo_exists(): ent.focus_set()
			return

		if "  " in ent.get().strip():

			messagebox.showerror("Error", f"Campo {self.lb_NameHospede.cget('text')} não pode ter espaços duplos")
			if ent.winfo_exists(): ent.focus_set()
			return

		if len(ent.get().strip()) > 200:

			messagebox.showerror("Error", f"Nome muito grande")
			if ent.winfo_exists(): ent.focus_set()
			return

		for item in self.fp.flt_Hospede.listLinhas:

			if ent.get().replace(" ","").lower() == str(item.dados[tb.Hospede.t_Nome]).replace(" ","").lower() and int(self.linhaAtual.dados[tb.Hospede.n_Id]) != int(item.dados[tb.Hospede.n_Id]):
	
				messagebox.showerror("Error", f"Hóspede já registrado com esse nome")
				if ent.winfo_exists(): ent.focus_set()
				return
			
		# Campo Quarto

		cbb = self.cbb_Quarto

		if not cbb.ent_Box.get().strip(): 
			
			messagebox.showerror("Error", f"Campo {self.lb_Quarto.cget('text')} não pode estar vazio")
			if cbb.winfo_exists(): cbb.focus_set()
			return

		achou = False

		for item in	cbb.list_Items:

			if cbb.ent_Box.get().strip().lower() == item.viewValue.lower():
				
				achou = True
				break

		if not achou:

			messagebox.showerror("Quarto não encontrado", "Quarto não existi na lista")
			if cbb.winfo_exists(): cbb.ent_Box.focus_set()
			return

		# Salvando dados

		Banco.SetDado(

			dadoId=int(self.ent_IdHospede.get()),
			tabela=tb.Hospede.tabela,
			idKey=tb.Hospede.n_Id,

			dados={

				tb.Hospede.t_Nome : self.ent_NameHospede.get().strip(),
				tb.Hospede.t_TipoCobranca : self.cbb_TipoCobranca.itemAtual.value,
				tb.Hospede.n_IdQuarto : int(self.cbb_Quarto.itemAtual.value)
			}
		)
		
		self.linhaAtual.list_cells[1].config(text=self.ent_NameHospede.get().strip())
		self.linhaAtual.list_cells[2].config(text=self.cbb_TipoCobranca.itemAtual.viewValue)
		self.linhaAtual.list_cells[3].config(text=self.cbb_Quarto.itemAtual.viewValue)
		
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

				WHERE {tb.Hospede.n_Id} = {self.linhaAtual.dados[tb.Hospede.n_Id]}
                    
        """)

		self.linhaAtual.dados = dados[0]

		self.F_EditarHosp.destroy()

	#-----------------------------------------------------------------------------------------------------------------------------------------------------------\

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------\