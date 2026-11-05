# --- importações
import tkinter as tk
from tkinter import messagebox
from Form.F_LoginDesign import Form
from Banco.Banco import Banco
from Styles.Style import Style

class F_Login(Form):

	def __init__(self):

		self.InicializarComponentes()

		self.F_Login.mainloop()