# --- importações
from typing import TYPE_CHECKING
import tkinter as tk
from tkinter import messagebox
from Form.F_EditarHospedeDesign import Form
from Banco.Banco import Banco
from Styles.Style import Style
from Models.Class import Tabelas as tb

if TYPE_CHECKING:

    from Form.F_Principal import F_principal


class F_EditarHospede(Form):

	def __init__(self, master, fp: "F_principal"):

		self.InicializarComponentes(master)

		self.linhaAtual = fp.flt_Hospede.linhaAtual
		self.fp = fp
		self.ent_IdHospede.delete(0, tk.END)
		self.ent_IdHospede.insert(0, self.linhaAtual.list_cells[0].cget("text"))
		self.ent_IdHospede.config(state="readonly")

		self.ent_NameHospede.delete(0, tk.END)
		self.ent_NameHospede.insert(0, self.linhaAtual.list_cells[1].cget("text"))
		Style.EntryBord(self.ent_NameHospede)

		self.cbb_TipoCobranca.AddItem({"Anual":"A", "Mensal":"M", "Diaria":"D"})
		self.cbb_TipoCobranca.itemAtual = self.cbb_TipoCobranca.GetItem(self.linhaAtual.list_cells[2].cget("text"))
		self.cbb_TipoCobranca.ent_Box.delete(0, tk.END)
		self.cbb_TipoCobranca.ent_Box.insert(0, self.linhaAtual.list_cells[2].cget("text"))
		self.cbb_TipoCobranca.ent_Box.config(state="readonly")

		self.ent_IdQuarto.delete(0, tk.END)
		self.ent_IdQuarto.insert(0, self.linhaAtual.list_cells[3].cget("text"))
		Style.EntryBord(self.ent_IdQuarto)

		self.F_EditarHosp.wait_window()

	def Click_btn_Confirmar(self):

		if not self.ent_NameHospede.get().strip(): 
			
			messagebox.showerror("Error",f"Campo {self.lb_NameHospede.cget('text')} não pode estar vazio")
			self.ent_NameHospede.focus_set()
			return

		if not self.ent_NameHospede.get().replace(" ", "").isalpha(): 
			
			messagebox.showerror("Error", f"Campo {self.lb_NameHospede.cget('text')} não pode ter números ou caracters especiais")
			self.ent_NameHospede.focus_set()
			return

		if len(self.ent_NameHospede.get().strip()) > 200:

			messagebox.showerror("Error", f"Nome muito grande")
			self.ent_NameHospede.focus_set()
			return

		for item in self.fp.flt_Hospede.listLinhas:

			if self.ent_NameHospede.get().title() == item.list_cells[1].cget("text") and int(self.ent_IdHospede.get()) != int(item.list_cells[0].cget("text")):
	
				messagebox.showerror("Error", f"Hóspede já registrado com esse nome")
				self.ent_NameHospede.focus_set()
				return

		if not self.ent_IdQuarto.get().strip(): 
			
			messagebox.showerror("Error", f"Campo {self.lb_IdQuarto.cget('text')} não pode estar vazio")
			self.ent_IdQuarto.focus_set()
			return

		if not self.ent_IdQuarto.get().isdigit(): 
			
			messagebox.showerror("Error", f"Campo {self.lb_IdQuarto.cget('text')} não ter letras ou caracteres especiais")
			self.ent_IdQuarto.focus_set()
			return

		Banco.SetDado(

			dadoId=int(self.ent_IdHospede.get()),
			tabela=tb.Hospede.tabela,
			idKey=tb.Hospede.n_Id,
			dados={

				tb.Hospede.t_Nome : self.ent_NameHospede.get().title(),
				tb.Hospede.t_TipoCobranca : self.cbb_TipoCobranca.itemAtual.value.title(),
				tb.Hospede.n_IdQuarto : int(self.ent_IdQuarto.get())
			}
		)

		self.linhaAtual.list_cells[1].config(text=self.ent_NameHospede.get().title())
		self.linhaAtual.list_cells[2].config(text=self.cbb_TipoCobranca.itemAtual.viewValue.title())
		self.linhaAtual.list_cells[3].config(text=self.ent_IdQuarto.get().title())
		
		self.F_EditarHosp.destroy()