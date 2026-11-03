# --- importações
from typing import TYPE_CHECKING
import tkinter as tk
from tkinter import messagebox
from Form.F_EditarHospedeDesign import Form
from Banco.Banco import Banco
from Styles.Style import Style

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

		self.ccb_TipoCobranca.AddItem({"Anual":"A", "Mensal":"M", "Diaria":"D"})
		self.ccb_TipoCobranca.itemAtual = self.ccb_TipoCobranca.GetItem(self.linhaAtual.list_cells[2].cget("text"))
		self.ccb_TipoCobranca.ent_Box.delete(0, tk.END)
		self.ccb_TipoCobranca.ent_Box.insert(0, self.linhaAtual.list_cells[2].cget("text"))
		self.ccb_TipoCobranca.ent_Box.config(state="readonly")

		self.ent_IdQuarto.delete(0, tk.END)
		self.ent_IdQuarto.insert(0, self.linhaAtual.list_cells[3].cget("text"))
		Style.EntryBord(self.ent_IdQuarto)

		self.F_EditarHosp.wait_window()

	def Click_btn_Confirmar(self):

		if not self.ent_IdQuarto.get().strip(): 
			
			messagebox.showerror("Error", f"Campo {self.lb_IdQuarto.cget('text')} não pode estar vazio")
			return

		if not self.ent_IdQuarto.get().isdigit(): 
			
			messagebox.showerror("Error", f"Campo {self.lb_IdQuarto.cget('text')} não ter letras")
			return

		if not self.ent_NameHospede.get().strip(): 
			
			messagebox.showerror("Error",f"Campo {self.lb_NameHospede.cget('text')} não pode estar vazio")
			return

		if any(char.isdigit() for char in self.ent_NameHospede.get()): 
			
			messagebox.showerror("Error",f"Campo {self.lb_NameHospede.cget('text')} não pode ter números")
			return
				
		for item in self.fp.flt_Hospede.listLinhas:

			if self.ent_NameHospede.get().title() == item.list_cells[1].cget("text") and int(self.ent_IdHospede.get()) != int(item.list_cells[0].cget("text")):
	
				messagebox.showerror("Error", f"Hóspede com esse nome já existir")
				return

		Banco.SetDado(

			dadoId=int(self.ent_IdHospede.get()),
			tabela="tb_Hospedes",
			idKey="n_IdHospede",
			dados={

				"t_NameHospede": self.ent_NameHospede.get().title(),
				"t_TipoCobranca": self.ccb_TipoCobranca.itemAtual.value.title(),
				"n_IdQuarto": self.ent_IdQuarto.get().title()
			}
		)

		self.linhaAtual.list_cells[1].config(text=self.ent_NameHospede.get().title())
		self.linhaAtual.list_cells[2].config(text=self.ccb_TipoCobranca.itemAtual.viewValue.title())
		self.linhaAtual.list_cells[3].config(text=self.ent_IdQuarto.get().title())
		
		self.F_EditarHosp.destroy()