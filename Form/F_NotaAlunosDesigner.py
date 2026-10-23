# arquivo de desiner

import tkinter as tk
from Componentes.ComponentesPersonalizados import FrameInferior, FrameList, FrameSuperio
from Form.F_NovaTurma import F_NovaTurma
from Styles.Style import Style
from Styles.Tema import Tema

class Form():

    # metodo que criar e configura os componentes
    def InicializarComponentes(self):
        
        self.F_principal = tk.Tk()
        self.pw_Panel = tk.PanedWindow(self.F_principal)
        self.frm_BarraLateral = tk.Frame(self.pw_Panel)
        self.frm_BarraSuperio = FrameSuperio(self.F_principal)
        self.frm_Botoes = tk.Frame(self.frm_BarraLateral)
        self.frm_Conteudo = tk.Frame(self.pw_Panel)
        self.frm_Home = tk.Frame(self.frm_Conteudo)
        self.frm_Turmas = tk.Frame(self.frm_Conteudo)
        self.frm_TurmasTitulo = FrameSuperio(self.frm_Turmas)
        self.lb_TurmasTitulo = tk.Label(self.frm_TurmasTitulo)
        self.btn_NovaTurma = tk.Button(self.frm_TurmasTitulo)
        self.frm_TurmasPesquisa = FrameSuperio(self.frm_Turmas)
        self.lb_TurmaPesquisa = tk.Label(self.frm_TurmasPesquisa)
        self.ent_BuscarTurma = tk.Entry(self.frm_TurmasPesquisa)
        self.btn_BuscarTurma = tk.Button(self.frm_TurmasPesquisa)
        self.frm_TurmasBotoes = FrameInferior(self.frm_Turmas)
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

            frm.config(bg=Tema.primario)
            frm.pack_propagate(False)
            frm.forget()

        self.frm_Home.pack(fill="both", expand=True)
        #
        # frm_TurmasTitulo
        #
        self.frm_TurmasTitulo.config(height=80)
        Style.DarkFrame(self.frm_TurmasTitulo)
        #
        # frm_TurmasPesquisa
        #
        self.frm_TurmasPesquisa.config(height=60)
        Style.DarkFrame(self.frm_TurmasPesquisa)
        #
        # frm_TurmasBotoes
        #
        self.frm_TurmasBotoes.config(height=60)
        Style.DarkFrame(self.frm_TurmasBotoes)
        #
        # frm_barraLateral
        #
        self.frm_BarraLateral.config(width=200)
        Style.DarkFrame(self.frm_BarraLateral)
        self.frm_BarraLateral.pack(side="left", fill="y")
        self.frm_BarraLateral.pack_propagate(False)
        #
        # frm_barraSuperio
        #
        self.frm_BarraSuperio.config(height=60)
        Style.DarkFrame(self.frm_BarraSuperio)
        #
        # pw_Panel
        #
        self.pw_Panel.pack(fill="both", expand=True)
        self.pw_Panel.config(orient="horizontal")
        self.pw_Panel.config(showhandle=True, sashrelief="flat", sashpad=-3)
        self.pw_Panel.config(bg=Tema.primario)
        self.pw_Panel.add(self.frm_BarraLateral)
        self.pw_Panel.add(self.frm_Conteudo)
        #
        # lb_Menu
        #
        self.lb_Menu.config(bg=Tema.segundario, fg=Tema.texto)
        self.lb_Menu.config(text="Menu", font=("arial", 15, "bold"))
        self.lb_Menu.pack(fill="x", padx=(1,1), pady=(1,10))
        #
        # lb_HomeTitulo
        #
        self.lb_HomeTitulo.config(bg=Tema.primario, fg=Tema.texto)
        self.lb_HomeTitulo.config(text="Home", font=Tema.fonteTitulo)  
        self.lb_HomeTitulo.pack(anchor="nw", pady=20, padx= 20)
        #
        # lb_BSTitulo
        #
        self.lb_BSTitulo.config(bg=Tema.segundario, fg=Tema.texto)
        self.lb_BSTitulo.config(text="Sistema de Notas", font=Tema.fonteTitulo)
        self.lb_BSTitulo.pack(side="left", padx=10)
        #
        # lb_TurmasTitulo
        #
        self.lb_TurmasTitulo.config(bg=self.frm_TurmasTitulo["bg"], fg=Tema.texto)
        self.lb_TurmasTitulo.config(text="Turmas", font=Tema.fonte)
        self.lb_TurmasTitulo.pack(side="left", padx=10)
        #
        # lb_TurmasPesqiusa
        #
        self.lb_TurmaPesquisa.config(bg=self.frm_TurmasPesquisa["bg"], fg=Tema.texto)
        self.lb_TurmaPesquisa.config(text="Pesquisa", font=Tema.fonte)
        self.lb_TurmaPesquisa.pack(side="left", padx=10)
        # 
        # ent_BuscarTurma
        #
        Style.DarkBoxEntry(self.ent_BuscarTurma)
        self.ent_BuscarTurma.pack(side="left", padx=10)
        #
        # btn_NovaTurma
        #
        self.btn_NovaTurma.config(Style.MenuTButton, bg=self.frm_TurmasTitulo["bg"])
        self.btn_NovaTurma.config(text="Nova Turma")
        self.btn_NovaTurma.config(command=lambda: self.FormAbrir_Click(F_NovaTurma))
        self.btn_NovaTurma.pack(side="right", padx=10)
        #
        # btn_BuscarTurma
        #
        self.btn_BuscarTurma.config(Style.MenuTButton, bg=self.frm_TurmasPesquisa["bg"])
        self.btn_BuscarTurma.config(text="Buscar")
        self.btn_BuscarTurma.pack(side="left", padx=10)
        #
        # btn_EditarTurma
        #
        self.btn_EditarTurma.config(Style.MenuTButton, bg=self.frm_TurmasBotoes["bg"])
        self.btn_EditarTurma.config(text="Editar")
        self.btn_EditarTurma.pack(side="left", padx=10)
        #
        # btn_ExcluirTurma
        #
        self.btn_ExcluirTurma.config(Style.MenuTButton, bg=self.frm_TurmasBotoes["bg"])
        self.btn_ExcluirTurma.config(text="Excluir")
        self.btn_ExcluirTurma.pack(side="left", padx=10)
        #
        # btn_AbrirTurma
        #
        self.btn_AbrirTurma.config(Style.MenuTButton, bg=self.frm_TurmasBotoes["bg"])
        self.btn_AbrirTurma.config(text="Abrir")
        self.btn_AbrirTurma.pack(side="left", padx=10)
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
            Style.DarkButton(btn)
            btn.pack(fill="x", padx=10, pady=4, ipady=8)
        
        self.ListView.config(bg=Tema.segundario)
        self.ListView.config(width=600)
        self.ListView.pack(fill="both", expand=True)
        self.ListView.AddColuna("ID","Nome","Nota","ID Turma")
        self.ListView.AddItem("01","bryan","10","02")
        #
        # F_principal
        #
        self.F_principal.title("Menu Principal")
        self.F_principal.geometry("800x600")
        self.F_principal.state("zoomed")
        self.F_principal.mainloop()
