# arquivo de desiner

import tkinter as tk
from typing import TYPE_CHECKING
from Componentes.ComponentesPersonalizados import FrameList
from Form.F_NovaTurma import F_NovaTurma
from Styles.Style import Style
from Styles.Style import TemaConfig

if TYPE_CHECKING:

    from F_NotaAlunos import F_principal

class Form():

    # metodo que criar e configura os componentes
    def InicializarComponentes(self: "F_principal"):
        
        self.fp = tk.Tk()
        self.pw_Panel = tk.PanedWindow(self.fp)
        self.frm_BarraLateral = tk.Frame(self.pw_Panel)
        self.frm_BarraSuperio = tk.Frame(self.fp)
        self.frm_Botoes = tk.Frame(self.frm_BarraLateral)
        self.frm_Conteudo = tk.Frame(self.pw_Panel)
        self.frm_Home = tk.Frame(self.frm_Conteudo)
        self.frm_Turmas = tk.Frame(self.frm_Conteudo)
        self.frm_TurmasTitulo = tk.Frame(self.frm_Turmas)
        self.lb_TurmasTitulo = tk.Label(self.frm_TurmasTitulo)
        self.btn_NovaTurma = tk.Button(self.frm_TurmasTitulo)
        self.frm_TurmasPesquisa = tk.Frame(self.frm_Turmas)
        self.lb_TurmaPesquisa = tk.Label(self.frm_TurmasPesquisa)
        self.ent_BuscarTurma = tk.Entry(self.frm_TurmasPesquisa)
        self.btn_BuscarTurma = tk.Button(self.frm_TurmasPesquisa)
        self.frm_TurmasBotoes = tk.Frame(self.frm_Turmas)
        self.btn_EditarTurma = tk.Button(self.frm_TurmasBotoes)
        self.btn_ExcluirTurma = tk.Button(self.frm_TurmasBotoes)
        self.btn_AbrirTurma = tk.Button(self.frm_TurmasBotoes)
        self.frm_Alunos = tk.Frame(self.frm_Conteudo)
        self.frm_Relatorio = tk.Frame(self.frm_Conteudo)
        self.frm_Config = tk.Frame(self.frm_Conteudo)
        self.lb_Menu = tk.Label(self.frm_BarraLateral)
        self.lb_HomeTitulo = tk.Label(self.frm_Home)
        self.lb_BSTitulo = tk.Label(self.frm_BarraSuperio)
        self.ListView = FrameList(self.frm_Turmas)
     
        #
        # Componentes Multiplos - FrameConteudos
        #

        self.frameConteudos = [self.frm_Conteudo, self.frm_Home, self.frm_Turmas, self.frm_Alunos, self.frm_Relatorio, self.frm_Config]
        
        for frm in self.frameConteudos:

            Style.Frame(frm)
            frm.pack_propagate(False)
            frm.forget()

        self.frm_Home.pack(fill="both", expand=True)

        #
        # frm_TurmasTitulo
        #

        self.frm_TurmasTitulo.config(height=80)
        self.frm_TurmasTitulo.pack_propagate(False)
        self.frm_TurmasTitulo.pack(side="top", fill="x")
        Style.FrameBord(self.frm_TurmasTitulo)

        #
        # frm_TurmasPesquisa
        #

        self.frm_TurmasPesquisa.config(height=60)
        self.frm_TurmasPesquisa.pack_propagate(False)
        self.frm_TurmasPesquisa.pack(side="top", fill="x")
        Style.FrameBord(self.frm_TurmasPesquisa)

        #
        # frm_TurmasBotoes
        #

        self.frm_TurmasBotoes.config(height=60)
        self.frm_TurmasBotoes.pack_propagate(False)
        self.frm_TurmasBotoes.pack(side="bottom", fill="x")
        Style.FrameBord(self.frm_TurmasBotoes)

        #
        # frm_barraLateral
        #

        self.frm_BarraLateral.config(width=200)
        self.frm_BarraLateral.pack(side="left", fill="y")
        self.frm_BarraLateral.pack_propagate(False)
        Style.FrameBord(self.frm_BarraLateral)

        #
        # frm_barraSuperio
        #

        self.frm_BarraSuperio.config(height=60)
        self.frm_BarraSuperio.pack_propagate(False)
        self.frm_BarraSuperio.pack(side="top", fill="x")
        Style.FrameBord(self.frm_BarraSuperio)

        #
        # pw_Panel
        #

        self.pw_Panel.config(orient="horizontal")
        self.pw_Panel.config(showhandle=True, sashrelief="flat", sashpad=-2)
        self.pw_Panel.config(bg=TemaConfig.tema.destaque, bd=0)
        self.pw_Panel.pack(fill="both", expand=True)
        self.pw_Panel.add(self.frm_BarraLateral)
        self.pw_Panel.add(self.frm_Conteudo)

        #
        # lb_Menu
        #

        self.lb_Menu.config(text="Menu", font=("arial", 15, "bold"))
        self.lb_Menu.pack(fill="x", padx=(1,1), pady=(1,10))
        Style.LabeHide(self.lb_Menu)

        #
        # lb_HomeTitulo
        #

        self.lb_HomeTitulo.config(text="Home", font=TemaConfig.tema.fonteTitulo)  
        self.lb_HomeTitulo.pack(anchor="nw", pady=20, padx= 20)
        Style.LabeHide(self.lb_HomeTitulo)

        #
        # lb_BSTitulo
        #

        self.lb_BSTitulo.config(text="Sistema de Hotel", font=TemaConfig.tema.fonteTitulo)
        self.lb_BSTitulo.pack(side="left", padx=10)
        Style.LabeHide(self.lb_BSTitulo)

        #
        # lb_TurmasTitulo
        #

        self.lb_TurmasTitulo.config(text="Turmas", font=TemaConfig.tema.fonte)
        self.lb_TurmasTitulo.pack(side="left", padx=10)
        Style.LabeHide(self.lb_TurmasTitulo)

        #
        # lb_TurmasPesqiusa
        #

        self.lb_TurmaPesquisa.config(text="Pesquisa", font=TemaConfig.tema.fonte)
        self.lb_TurmaPesquisa.pack(side="left", padx=10)
        Style.LabeHide(self.lb_TurmaPesquisa)

        # 
        # ent_BuscarTurma
        #

        self.ent_BuscarTurma.pack(side="left", padx=10)
        Style.EntryBord(self.ent_BuscarTurma)

        #
        # btn_NovaTurma
        #

        self.btn_NovaTurma.config(text="Nova Turma")
        self.btn_NovaTurma.config(command=lambda: self.FormAbrir_Click(F_NovaTurma))
        self.btn_NovaTurma.pack(side="right", padx=10) 
        Style.ButtonHide(self.btn_NovaTurma)

        #
        # btn_BuscarTurma
        #

        self.btn_BuscarTurma.config(text="Buscar")
        self.btn_BuscarTurma.pack(side="left", padx=10)
        Style.ButtonHide(self.btn_BuscarTurma)

        #
        # btn_EditarTurma
        #

        self.btn_EditarTurma.config(text="Editar")
        self.btn_EditarTurma.pack(side="left", padx=10)
        Style.ButtonHide(self.btn_EditarTurma)

        #
        # btn_ExcluirTurma
        #

        self.btn_ExcluirTurma.config(text="Excluir")
        self.btn_ExcluirTurma.pack(side="left", padx=10)
        Style.ButtonHide(self.btn_ExcluirTurma)

        #
        # btn_AbrirTurma
        #
        
        self.btn_AbrirTurma.config(text="Abrir")
        self.btn_AbrirTurma.pack(side="left", padx=10)
        Style.ButtonHide(self.btn_AbrirTurma)

        #
        # componentes multiplos - buttonsMenu
        #

        self.ButtonsMenu = [
            
            ("Home", self.frm_Home),
            ("Turmas", self.frm_Turmas),
            ("Alunos", self.frm_Alunos),
            ("Relatorio", self.frm_Relatorio),
            ("Configurações", self.frm_Config),
        ]

        for texto, frm in self.ButtonsMenu:

            btn = tk.Button(self.frm_BarraLateral, text=texto, command=lambda f=frm: self.MostraFrame_Click(f))
            Style.ButtonFlat(btn)
            btn.pack(fill="x", padx=10, pady=4, ipady=8)
        
        self.ListView.config(bg=TemaConfig.tema.segundario)
        self.ListView.config(width=600)
        self.ListView.pack(fill="both", expand=True)
        self.ListView.OnSelectItem = self.SelectCell
        Style.FrameListZebrado(self.ListView)

        self.ListView.AddColuna("ID","Nome","Nota","ID Turma")
        
        for i in range(0,50):

            self.ListView.AddItem(f"{i}","bryan","10","02")

        #
        # F_principal
        #

        self.fp.title("Menu Principal")
        self.fp.geometry("800x600")
        self.fp.state("zoomed")
        self.fp.mainloop()
