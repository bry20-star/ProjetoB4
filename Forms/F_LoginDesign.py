
# importações 

import tkinter as tk
from typing import TYPE_CHECKING
from Styles.Style import Style
from Styles.Tema import Config

if TYPE_CHECKING:

    from F_Login import F_Login

#--------------------------------- Form ---------------------------------------------------------------------------------------------------------------------------------------------------/

class Form():

    def InicializarComponentes(self: "F_Login"):

        # janela

        self.F_Login = tk.Tk()

        # frame

        self.frm_Conteudo = tk.Frame(self.F_Login)
        self.frm_BarraSuperior = tk.Frame(self.frm_Conteudo)
        self.frm_Conta = tk.Frame(self.frm_Conteudo)
        self.frm_ContaSenha = tk.Frame(self.frm_Conteudo)

        # label

        self.lb_BarraSuperior = tk.Label(self.frm_BarraSuperior)
        self.lb_Conta = tk.Label(self.frm_Conta)
        self.lb_ContaSenha = tk.Label(self.frm_ContaSenha)

        # entry

        self.ent_Conta = tk.Entry(self.frm_Conta)
        self.ent_ContaSenha = tk.Entry(self.frm_ContaSenha)

        # button

        self.btn_Login = tk.Button(self.frm_Conteudo)
        self.btn_MostraSenha = tk.Button(self.frm_ContaSenha)

    #---------------- Compoenentes Janela -------------------------------------------------/

        #
        # frm_Conteudo
        #

        self.frm_Conteudo.pack(fill="both", expand=True)
        Style.frame.Bord(self.frm_Conteudo)

        #
        # frm_BarraSuperior
        #

        self.frm_BarraSuperior.pack(fill="x", side="top")
        self.frm_BarraSuperior.config(height=50)
        Style.frame.Bord(self.frm_BarraSuperior)

        #
        # frm_Conta
        #

        self.frm_Conta.pack(fill="x", side="top")
        self.frm_Conta.config(height=90)
        self.frm_Conta.pack_propagate(False)
        Style.frame.Bord(self.frm_Conta)

        #
        # frm_ContaSenha
        #

        self.frm_ContaSenha.pack(fill="x", side="top" )
        self.frm_ContaSenha.config(height=90)
        self.frm_ContaSenha.pack_propagate(False)
        Style.frame.Bord(self.frm_ContaSenha)

        #
        # lb_BarraSuperior
        #

        self.lb_BarraSuperior.config(text="Bem-Vindo!", font=Config.tema.fonteTitulo)
        self.lb_BarraSuperior.pack(side="left", expand=True)
        Style.label.Hide(self.lb_BarraSuperior)
       

        #
        # lb_Conta
        #

        self.lb_Conta.config(text="Conta", font=Config.tema.fonte)
        self.lb_Conta.pack(anchor="w", padx=2, pady=10)
        Style.label.Hide(self.lb_Conta)

        #
        # lb_ContaSenha
        #

        self.lb_ContaSenha.config(text="Senha", font=Config.tema.fonte)
        self.lb_ContaSenha.pack(anchor="w", padx=2, pady=10)
        Style.label.Hide(self.lb_ContaSenha)

        #
        # ent_Conta
        #

        self.ent_Conta.pack(anchor="w", padx=2)
        self.ent_Conta.insert(0,"bry")
        self.ent_Conta.config(width=30)
        Style.entry.Bord(self.ent_Conta)

        #
        # ent_ContaSenha
        #

        self.ent_ContaSenha.pack(side="left", padx=2, pady=(0,20))
        self.ent_ContaSenha.insert(0,"123")
        self.ent_ContaSenha.config(show="*")
        Style.entry.Bord(self.ent_ContaSenha)

        #
        # btn_Login
        #

        self.btn_Login.config(text="Logar")
        self.btn_Login.pack(side="bottom", fill="x", expand=True)
        self.btn_Login.config(command= lambda: self.Click_btn_Login())
        Style.button.Hide(self.btn_Login) 

        #
        # btn_MostraSenha
        #

        self.btn_MostraSenha.config(text="x_x")
        self.btn_MostraSenha.pack(side="left", padx=5, pady=(0,25))
        self.btn_MostraSenha.config(command= lambda: self.Click_btn_MostraSenha())
        Style.button.Hide(self.btn_MostraSenha) 

        #
        # F_Login
        #

        altura = 300
        lagura = 400
        x = (self.F_Login.winfo_screenwidth() - lagura)//2
        y = (self.F_Login.winfo_screenheight() - altura)//2
        self.F_Login.title("Login")
        self.F_Login.geometry(f"{lagura}x{altura}+{x}+{y}")
        self.F_Login.resizable(False,False)

    #-----------------------------------------------------------------------------------------------------------------\

#----------------------------------------------------------------------------------------------------------------------------------------------\