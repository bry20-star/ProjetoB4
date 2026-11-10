
# --- importações

import tkinter as tk
from tkinter import messagebox
from Forms.F_LoginDesign import Form
from Banco.Banco import Banco
from Modelos.Tabelas import Tabelas as tb
from Styles.Style import Style

#------------------------------------------------------- F_Login ---------------------------------------------------------------------------------------------------------------------------------------------------------/

class F_Login(Form):

	def __init__(self):

		self.InicializarComponentes()

		self.mostraSenha = False

		self.F_Login.mainloop()

	def Click_btn_MostraSenha(self):

		if not self.mostraSenha:

			self.btn_MostraSenha.config(text="๏_๏")
			self.ent_ContaSenha.config(show="")
			self.mostraSenha = True

		else:

			self.btn_MostraSenha.config(text="x_x")
			self.ent_ContaSenha.config(show="*")
			self.mostraSenha = False

	def Click_btn_Login(self):

		if not self.ent_Conta.get().strip():

			messagebox.showerror("Error", f"Campo {self.lb_Conta.cget('text')} não pode está vazio")
			self.ent_Conta.focus_set()
			return
		
		if " " in self.ent_Conta.get().strip():

			messagebox.showerror("Error", f"Campo {self.lb_Conta.cget('text')} não pode ter espaços")
			self.ent_Conta.focus_set()
			return

		if not self.ent_Conta.get().strip().isalpha():

			messagebox.showerror("Error",f"Campo {self.lb_Conta.cget('text')} não pode ter números, caracteres especiais ou espaços")
			self.ent_Conta.focus_set()
			return

		if not self.ent_ContaSenha.get().strip():

			messagebox.showerror("Error", f"Campo {self.lb_ContaSenha.cget('text')} não pode está vazio")
			self.ent_ContaSenha.focus_set()
			return

		if " " in self.ent_ContaSenha.get().strip():

			messagebox.showerror("Error", f"Campo {self.lb_ContaSenha.cget('text')} não pode ter espaços")
			self.ent_ContaSenha.focus_set()
			return

		if not self.ent_ContaSenha.get().strip().isdigit():

			messagebox.showerror("Error", f"Campo {self.lb_ContaSenha.cget('text')} não pode ter letras, caracteres especiais ou espaços")
			self.ent_ContaSenha.focus_set()
			return

		user = Banco.DQL(f"""
		
			SELECT *

				FROM {tb.Usuario.tabela}

				WHERE {tb.Usuario.t_Conta} == '{self.ent_Conta.get().strip()}' AND

				{tb.Usuario.t_Senha} == '{self.ent_ContaSenha.get().strip()}'
		
		""")

		if not user:
			
			messagebox.showerror("Error", "Conta não encontrada")
			self.ent_Conta.focus_set()
			return

		self.F_Login.destroy()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------\