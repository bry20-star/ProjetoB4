
# importações 

from typing import TYPE_CHECKING
from Banco.Banco import Banco
from Forms.F_NovoQuartoDesign import Form
import tkinter as tk
from tkinter import messagebox
from Modelos.Tabelas import Tabelas as tb

if TYPE_CHECKING:

	from Forms.F_Principal import F_principal

#----------------------- F_NovoQuarto ----------------------------------------------------------------------------------------------------------------------------------------------------/

class F_NovoQuarto(Form):

	def __init__(self, master, fp: "F_principal"):

		self.InicializarComponentes(master)

		self.fp = fp

		# ComboBoxs - imcorporando

		self.cbb_StatusQuarto.AddItem({
		
			tb.Quarto.disponivel["view"] : tb.Quarto.disponivel["value"],
			tb.Quarto.oculpado["view"] : tb.Quarto.oculpado["value"],
			tb.Quarto.bloqueado["view"] : tb.Quarto.bloqueado["value"]

		})

		self.cbb_TipoQuarto.AddItem({
			
			tb.Quarto.standard["view"] : tb.Quarto.standard["value"],	
			tb.Quarto.luxo["view"] : tb.Quarto.luxo["value"],	
			tb.Quarto.suite["view"] : tb.Quarto.suite["value"]	
		})

		self.F_NovoQuarto.wait_window()

	#------------------------ Metodos ----------------------------------------------------------------------------------------------------------/

	def Click_btn_Confirmar(self):

		# campo Nome Quarto

		nud = self.ent_NomeQuarto

		if nud.get() == self.ent_NomeQuarto_text:

			messagebox.showerror("Error","Nome do Quarto não foi definido")
			if nud.winfo_exists(): nud.focus_set()
			return

		if not nud.get().strip():

			messagebox.showerror("Error", f"Campo {self.lb_NomeQuarto.cget('text')} não pode está vazio")
			if nud.winfo_exists(): nud.focus_set()
			return

		for l in nud.get().replace(" ",""):
				
			if l.isdigit(): continue

			if l.isalpha(): continue

			messagebox.showerror("Error", f"O nome do quarto não ter caracteres especiais")
			if nud.winfo_exists(): nud.focus_set()
			return

		if "  " in nud.get():
			   
			messagebox.showerror("Error", "O nome do quarto não ter espaços duplos")
			if nud.winfo_exists(): nud.focus_set()
			return

		for item in self.fp.flt_Quarto.listLinhas:

			if str(item.dados[tb.Quarto.t_Nome]).replace(" ","").lower() == nud.get().replace(" ","").lower():
				
				messagebox.showerror("Error", "Quarto já registrado com esse nome")
				if nud.winfo_exists(): nud.focus_set()
				return

		# Adicionando dados

		quartoId = Banco.AddDado(
			
			tabela=tb.Quarto.tabela,

			dados={
			
				tb.Quarto.t_Nome: self.ent_NomeQuarto.get().strip(),
				tb.Quarto.t_Estado: self.cbb_StatusQuarto.itemAtual.value,
				tb.Quarto.t_Tipo: self.cbb_TipoQuarto.itemAtual.value,
				tb.Quarto.n_Cap: self.nud_CapQuarto._value

			}
		)

		dados = Banco.DQL(f"""
            
            SELECT *,

                CASE 

                    WHEN {tb.Quarto.t_Tipo} = '{tb.Quarto.standard["value"]}' THEN '{tb.Quarto.standard["view"]}'
                    WHEN {tb.Quarto.t_Tipo} = '{tb.Quarto.luxo["value"]}' THEN '{tb.Quarto.luxo["view"]}'
                    WHEN {tb.Quarto.t_Tipo} = '{tb.Quarto.suite["value"]}' THEN '{tb.Quarto.suite["view"]}'

                END as 'tipo',

                CASE 

                    WHEN {tb.Quarto.t_Estado} = '{tb.Quarto.disponivel["value"]}' THEN '{tb.Quarto.disponivel["view"]}'
                    WHEN {tb.Quarto.t_Estado} = '{tb.Quarto.oculpado["value"]}' THEN '{tb.Quarto.oculpado["view"]}'
                    WHEN {tb.Quarto.t_Estado} = '{tb.Quarto.bloqueado["value"]}' THEN '{tb.Quarto.bloqueado["view"]}'

                END as 'estado'

            FROM
                
                {tb.Quarto.tabela}

			WHERE {tb.Quarto.n_Id} = {quartoId}
        
        """)

		self.fp.flt_Quarto.AddItem(
			
				str(quartoId),
				self.ent_NomeQuarto.get().strip()

		).dados = dados[0]

		self.F_NovoQuarto.destroy()

	#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------\

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\

