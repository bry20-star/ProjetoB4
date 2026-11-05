# arquivo de designer

from logging import config
import tkinter as tk
from typing import TYPE_CHECKING
from Styles.Style import Style
from Styles.Style import TemaConfig
from Componentes.ComponentesPersonalizados import ComboBox


if TYPE_CHECKING:

    from F_Login import F_Login

class Form():

    def InicializarComponentes(self: "F_Login"):

        self.F_Login = tk.Tk()
        self.frm_Conteudo = tk.Frame(self.F_Login)
        self.frm_BarraSuperior = tk.Frame(self.frm_Conteudo)
        self.frm_Conta = tk.Frame(self.frm_Conteudo)
        self.frm_ContaSenha = tk.Frame(self.frm_Conteudo)
        self.lb_BarraSuperior = tk.Label(self.frm_BarraSuperior)
        self.lb_Conta = tk.Label(self.frm_Conta)
        self.lb_ContaSenha = tk.Label(self.frm_ContaSenha)
        self.ent_Conta = tk.Entry(self.frm_Conta)
        self.ent_ContaSenha = tk.Entry(self.frm_ContaSenha)
        self.btn_Login = tk.Button(self.frm_Conteudo)
        self.btn_MostraSenha = tk.Button(self.frm_ContaSenha)
        self.btn_Fechar = tk.Button(self.frm_BarraSuperior)

        #
        # frm_Conteudo
        #

        self.frm_Conteudo.pack(fill="both", expand=True)
        Style.FrameBord(self.frm_Conteudo)

        #
        # frm_BarraSuperior
        #

        self.frm_BarraSuperior.pack(fill="x", side="top")
        self.frm_BarraSuperior.config(height=50)
        Style.FrameBord(self.frm_BarraSuperior)

        #
        # frm_Conta
        #

        self.frm_Conta.pack(fill="x", side="top")
        self.frm_Conta.config(height=90)
        self.frm_Conta.pack_propagate(False)
        Style.FrameBord(self.frm_Conta)

        #
        # frm_ContaSenha
        #

        self.frm_ContaSenha.pack(fill="x", side="top" )
        self.frm_ContaSenha.config(height=90)
        self.frm_ContaSenha.pack_propagate(False)
        Style.FrameBord(self.frm_ContaSenha)

        #
        # lb_BarraSuperior
        #

        self.lb_BarraSuperior.config(text="Bem-Vindo!", font=TemaConfig.tema.fonteTitulo)
        self.lb_BarraSuperior.pack(side="left", expand=True)
        Style.LabeHide(self.lb_BarraSuperior)

        #
        # lb_Conta
        #

        self.lb_Conta.config(text="Conta", font=TemaConfig.tema.fonte)
        self.lb_Conta.pack(anchor="w", padx=2, pady=10)
        Style.LabeHide(self.lb_Conta)

        #
        # lb_ContaSenha
        #

        self.lb_ContaSenha.config(text="Senha", font=TemaConfig.tema.fonte)
        self.lb_ContaSenha.pack(anchor="w", padx=2, pady=10)
        Style.LabeHide(self.lb_ContaSenha)

        #
        # ent_Conta
        #

        self.ent_Conta.pack(anchor="w", padx=2)
        self.ent_Conta.config(width=30)
        Style.EntryBord(self.ent_Conta)

        #
        # ent_ContaSenha
        #

        self.ent_ContaSenha.pack(side="left", padx=2, pady=(0,20))
        self.ent_ContaSenha.config(show="*")
        Style.EntryBord(self.ent_ContaSenha)

        #
        # btn_Login
        #

        self.btn_Login.config(text="Logar")
        self.btn_Login.pack(side="bottom", expand=True)
        Style.ButtonHide(self.btn_Login) 

        #
        # btn_MostraSenha
        #

        self.btn_MostraSenha.config(text="x_x")
        self.btn_MostraSenha.pack(side="left", padx=5, pady=(0,25))
        Style.ButtonHide(self.btn_MostraSenha) 

        #
        # btn_Fechar
        #

        self.btn_Fechar.config(text=" X ", width=5, command=self.F_Login.destroy)
        self.btn_Fechar.pack(side="right", fill="y")
        Style.ButtonHide(self.btn_Fechar)

        #
        # F_Login
        #

        altura = 300
        lagura = 400
        x = (self.F_Login.winfo_screenwidth() - lagura)//2
        y = (self.F_Login.winfo_screenheight() - altura)//2
        self.F_Login.title("Login")
        self.F_Login.overrideredirect(True)
        self.F_Login.geometry(f"{lagura}x{altura}+{x}+{y}")
        self.F_Login.resizable(False,False)
