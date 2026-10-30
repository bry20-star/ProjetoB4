# arquivo de desiner

import tkinter as tk
from typing import TYPE_CHECKING
from Componentes.ComponentesPersonalizados import FrameList
from Form.F_NovoHospede import F_NovoHospede
from Styles.Style import Style
from Styles.Style import TemaConfig

if TYPE_CHECKING:

    from F_Principal import F_principal

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
        self.frm_Hospedes = tk.Frame(self.frm_Conteudo)
        self.frm_HospedesTitulo = tk.Frame(self.frm_Hospedes)
        self.lb_HospedesTitulo = tk.Label(self.frm_HospedesTitulo)
        self.btn_NovoHospede = tk.Button(self.frm_HospedesTitulo)
        self.frm_BuscarHospede = tk.Frame(self.frm_Hospedes)
        self.lb_BuscarHospede = tk.Label(self.frm_BuscarHospede)
        self.ent_BuscarHospede = tk.Entry(self.frm_BuscarHospede)
        self.btn_BuscarHospede = tk.Button(self.frm_BuscarHospede)
        self.frm_HospedesBotoes = tk.Frame(self.frm_Hospedes)
        self.btn_EditarHospede = tk.Button(self.frm_HospedesBotoes)
        self.btn_ExcluirHospede = tk.Button(self.frm_HospedesBotoes)
        self.btn_AbrirHospede = tk.Button(self.frm_HospedesBotoes)
        self.frm_Funcionarios = tk.Frame(self.frm_Conteudo)
        self.frm_Relatorio = tk.Frame(self.frm_Conteudo)
        self.frm_Config = tk.Frame(self.frm_Conteudo)
        self.lb_Menu = tk.Label(self.frm_BarraLateral)
        self.lb_HomeTitulo = tk.Label(self.frm_Home)
        self.lb_BSTitulo = tk.Label(self.frm_BarraSuperio)
        self.flt_Hospede = FrameList(self.frm_Hospedes)
     
        #
        # Componentes Multiplos - FrameConteudos
        #

        self.frameConteudos = [self.frm_Conteudo, self.frm_Home, self.frm_Hospedes, self.frm_Funcionarios, self.frm_Relatorio, self.frm_Config]
        
        for frm in self.frameConteudos:

            Style.Frame(frm)
            frm.pack_propagate(False)
            frm.forget()

        self.frm_Home.pack(fill="both", expand=True)

        #
        # frm_HospedesTitulo
        #

        self.frm_HospedesTitulo.config(height=80)
        self.frm_HospedesTitulo.pack_propagate(False)
        self.frm_HospedesTitulo.pack(side="top", fill="x")
        Style.FrameBord(self.frm_HospedesTitulo)

        #
        # frm_HospedesPesquisa
        #

        self.frm_BuscarHospede.config(height=60)
        self.frm_BuscarHospede.pack_propagate(False)
        self.frm_BuscarHospede.pack(side="top", fill="x")
        Style.FrameBord(self.frm_BuscarHospede)

        #
        # frm_HospedesBotoes
        #

        self.frm_HospedesBotoes.config(height=60)
        self.frm_HospedesBotoes.pack_propagate(False)
        self.frm_HospedesBotoes.pack(side="bottom", fill="x")
        Style.FrameBord(self.frm_HospedesBotoes)

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

        self.lb_BSTitulo.config(text="Accommodation Hotel", font=TemaConfig.tema.fonteTitulo)
        self.lb_BSTitulo.pack(side="left", padx=10)
        Style.LabeHide(self.lb_BSTitulo)

        #
        # lb_HospedesTitulo
        #

        self.lb_HospedesTitulo.config(text="Hóspedes", font=TemaConfig.tema.fonte)
        self.lb_HospedesTitulo.pack(side="left", padx=10)
        Style.LabeHide(self.lb_HospedesTitulo)

        #
        # lb_HospedesPesquisa
        #

        self.lb_BuscarHospede.config(text="Pesquisa", font=TemaConfig.tema.fonte)
        self.lb_BuscarHospede.pack(side="left", padx=10)
        Style.LabeHide(self.lb_BuscarHospede)

        # 
        # ent_BuscarHospede
        #

        self.ent_BuscarHospede.pack(side="left", padx=10)
        Style.EntryBord(self.ent_BuscarHospede)

        #
        # btn_NovoHospede
        #

        self.btn_NovoHospede.config(text="Novo Hóspede")
        self.btn_NovoHospede.config(command=lambda: self.FormAbrir_Click(F_NovoHospede))
        self.btn_NovoHospede.pack(side="right", padx=10) 
        Style.ButtonHide(self.btn_NovoHospede)

        #
        # btn_BuscarHospede
        #

        self.btn_BuscarHospede.config(text="Buscar")
        self.btn_BuscarHospede.pack(side="left", padx=10)
        Style.ButtonHide(self.btn_BuscarHospede)

        #
        # btn_EditarHospede
        #

        self.btn_EditarHospede.config(text="Editar")
        self.btn_EditarHospede.pack(side="left", padx=10)
        Style.ButtonHide(self.btn_EditarHospede)

        #
        # btn_ExcluirHospede
        #

        self.btn_ExcluirHospede.config(text="Excluir")
        self.btn_ExcluirHospede.pack(side="left", padx=10)
        Style.ButtonHide(self.btn_ExcluirHospede)

        #
        # btn_AbrirHospede
        #
        
        self.btn_AbrirHospede.config(text="Abrir")
        self.btn_AbrirHospede.pack(side="left", padx=10)
        Style.ButtonHide(self.btn_AbrirHospede)

        #
        # componentes multiplos - buttonsMenu
        #

        self.ButtonsMenu = [
            
            ("Home", self.frm_Home),
            ("Hóspedes", self.frm_Hospedes),
            ("Funcionários", self.frm_Funcionarios),
            ("Relatório", self.frm_Relatorio),
            ("Configurações", self.frm_Config),
        ]

        for texto, frm in self.ButtonsMenu:

            btn = tk.Button(self.frm_BarraLateral, text=texto, command=lambda f=frm: self.MostraFrame_Click(f))
            Style.ButtonFlat(btn)
            btn.pack(fill="x", padx=10, pady=4, ipady=8)
        
        self.flt_Hospede.config(bg=TemaConfig.tema.segundario)
        self.flt_Hospede.config(width=600)
        self.flt_Hospede.pack(fill="both", expand=True)
        self.flt_Hospede.OnSelectItem = self.SelectCell
        Style.FrameListZebrado(self.flt_Hospede)

        self.flt_Hospede.AddColuna("ID","Nome","Forma de Pagamento","ID Quarto")
        
        for i in range(0,50):

            self.flt_Hospede.AddItem(f"{i}","bryan","Mensal: R$67,00","02")

        #
        # F_principal
        #

        self.fp.title("Accommodation Hotel")
        self.fp.geometry("800x600")
        self.fp.state("zoomed")
        self.fp.mainloop()
