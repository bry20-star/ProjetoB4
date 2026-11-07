# arquivo de desiner

# Importações 
import tkinter as tk
from typing import TYPE_CHECKING
from Componentes.ComponentesPersonalizados import FrameList, ComboBox
from Form.F_NovoHospede import F_NovoHospede
from Form.F_EditarHospede import F_EditarHospede
from Styles.Style import Style
from Styles.Style import TemaConfig
from Models.Class import Tabelas as tb

if TYPE_CHECKING:

    from F_Principal import F_principal

class Form():

    def InicializarComponentes(self: "F_principal"):
        
        self.fp = tk.Tk()
        self.pw_Panel = tk.PanedWindow(self.fp)
        self.frm_BarraLateral = tk.Frame(self.pw_Panel)
        self.frm_BarraSuperio = tk.Frame(self.fp)
        self.frm_Botoes = tk.Frame(self.frm_BarraLateral)
        self.frm_Conteudo = tk.Frame(self.pw_Panel)
        self.lb_BSTitulo = tk.Label(self.frm_BarraSuperio)
        self.lb_Menu = tk.Label(self.frm_BarraLateral)

        # frm_Home
      
        self.frm_Home = tk.Frame(self.frm_Conteudo)
        self.lb_HomeTitulo = tk.Label(self.frm_Home)

        #frm_Hospedes

        self.frm_Hospedes = tk.Frame(self.frm_Conteudo)
        self.frm_HospedesTitulo = tk.Frame(self.frm_Hospedes)
        self.frm_BuscarHospede = tk.Frame(self.frm_Hospedes)
        self.frm_HospedesBotoes = tk.Frame(self.frm_Hospedes)
        self.lb_HospedesTitulo = tk.Label(self.frm_HospedesTitulo)
        self.lb_BuscarHospede = tk.Label(self.frm_BuscarHospede)
        self.btn_BuscarHospede = tk.Button(self.frm_BuscarHospede)
        self.btn_EditarHospede = tk.Button(self.frm_HospedesBotoes)
        self.btn_ExcluirHospede = tk.Button(self.frm_HospedesBotoes)
        self.btn_AbrirHospede = tk.Button(self.frm_HospedesBotoes)
        self.btn_NovoHospede = tk.Button(self.frm_HospedesTitulo)
        self.ent_BuscarHospede = tk.Entry(self.frm_BuscarHospede)
        self.flt_Hospede = FrameList(self.frm_Hospedes)

        #frm_Quarto

        self.frm_Quarto = tk.Frame(self.frm_Conteudo)
        self.frm_QuartoLateral = tk.Frame(self.frm_Quarto)
        self.frm_QuartoBotoes = tk.Frame(self.frm_Quarto)
        self.frm_QuartoBusca = tk.Frame(self.frm_QuartoLateral)
        self.frm_QuartoId = tk.Frame(self.frm_QuartoLateral)
        self.frm_QuartoNome = tk.Frame(self.frm_QuartoLateral)
        self.frm_QuartoOcupacao = tk.Frame(self.frm_QuartoLateral)
        self.frm_QuartoTipo = tk.Frame(self.frm_QuartoLateral)
        self.frm_QuartoCap = tk.Frame(self.frm_QuartoLateral)
        self.lb_QuartoBusca = tk.Label(self.frm_QuartoBusca)
        self.lb_QuartoId = tk.Label(self.frm_QuartoId)
        self.lb_QuartoNome = tk.Label(self.frm_QuartoNome)
        self.lb_QuartoOcupacao = tk.Label(self.frm_QuartoOcupacao)
        self.lb_QuartoTipo = tk.Label(self.frm_QuartoTipo)
        self.lb_QuartoCap = tk.Label(self.frm_QuartoCap)
        self.btn_QuartoSalvar = tk.Button(self.frm_QuartoBotoes)
        self.btn_QuartoExcluir = tk.Button(self.frm_QuartoBotoes)
        self.ent_QuartoBusca = tk.Entry(self.frm_QuartoBusca)
        self.ent_QuartoId = tk.Entry(self.frm_QuartoId)
        self.ent_QuartoNome = tk.Entry(self.frm_QuartoNome)
        self.ent_QuartoCap = tk.Entry(self.frm_QuartoCap) 
        self.cbb_QuartoOcupacao = ComboBox(self.frm_QuartoOcupacao)
        self.cbb_QuartoTipo = ComboBox(self.frm_QuartoTipo)
        

        self.flt_Quarto = FrameList(self.frm_Quarto)

        #frm_Funcionarios

        self.frm_Funcionarios = tk.Frame(self.frm_Conteudo)

        #frm_Relatorio

        self.frm_Relatorio = tk.Frame(self.frm_Conteudo)

        #frm_Config

        self.frm_Config = tk.Frame(self.frm_Conteudo)
        
        #
        # Componentes Multiplos - FrameConteudos
        #

        self.frameConteudos = [self.frm_Conteudo, self.frm_Home, self.frm_Hospedes, self.frm_Quarto, self.frm_Funcionarios, self.frm_Relatorio, self.frm_Config]
        
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
        # frm_QuartoLateral
        #

        self.frm_QuartoLateral.config(width=400)
        self.frm_QuartoLateral.pack(side="right", fill="y")
        self.frm_QuartoLateral.pack_propagate(False)
        Style.FrameBord(self.frm_QuartoLateral)

        #
        # frm_QuartoBotoes
        #

        self.frm_QuartoBotoes.config(height=60)
        self.frm_QuartoBotoes.pack(side="bottom", fill="x")
        self.frm_QuartoBotoes.pack_propagate(False)
        Style.FrameBord(self.frm_QuartoBotoes)

        #
        # frm_QuartoBusca
        #

        self.frm_QuartoBusca.config(height=60)
        self.frm_QuartoBusca.pack(side="top", fill="x", pady=(0, 20))
        self.frm_QuartoBusca.pack_propagate(False)
        Style.FrameBord(self.frm_QuartoBusca)

        #
        # frm_QuartoId
        #

        self.frm_QuartoId.config(height=80)
        self.frm_QuartoId.pack(side="top", fill="x", expand=True)
        self.frm_QuartoId.pack_propagate(False)
        Style.FrameBord(self.frm_QuartoId)

        
        #
        # frm_QuartoNome
        #

        self.frm_QuartoNome.config(height=80)
        self.frm_QuartoNome.pack(side="top", fill="x", expand=True)
        self.frm_QuartoNome.pack_propagate(False)
        Style.FrameBord(self.frm_QuartoNome)

        #
        # frm_QuartoOcupacao
        #

        self.frm_QuartoOcupacao.config(height=80)
        self.frm_QuartoOcupacao.pack(side="top", fill="x", expand=True)
        self.frm_QuartoOcupacao.pack_propagate(False)
        Style.FrameBord(self.frm_QuartoOcupacao)

        #
        # frm_QuartoTipo
        #

        self.frm_QuartoTipo.config(height=80)
        self.frm_QuartoTipo.pack(side="top", fill="x", expand=True)
        self.frm_QuartoTipo.pack_propagate(False)
        Style.FrameBord(self.frm_QuartoTipo)

        #
        # frm_QuartoCap
        #

        self.frm_QuartoCap.config(height=80)
        self.frm_QuartoCap.pack(side="top", fill="x", expand=True, pady=(0, 60))
        self.frm_QuartoCap.pack_propagate(False)
        Style.FrameBord(self.frm_QuartoCap)

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
        # lb_QuartoBusca
        #

        self.lb_QuartoBusca.config(text="Pesquisa", font=TemaConfig.tema.fonte)
        self.lb_QuartoBusca.pack(side="left", padx=10)
        Style.LabeHide(self.lb_QuartoBusca)

        #
        # lb_QuartoId
        #

        self.lb_QuartoId.config(text="Quarto ID")
        self.lb_QuartoId.pack(anchor="w", padx=10, pady=(15, 0))
        Style.LabeHide(self.lb_QuartoId)

        #
        # lb_QuartoNome
        #

        self.lb_QuartoNome.config(text="Quarto")
        self.lb_QuartoNome.pack(anchor="w", padx=10, pady=(15, 0))
        Style.LabeHide(self.lb_QuartoNome)

        #
        # lb_QuartoOcupacao
        #

        self.lb_QuartoOcupacao.config(text="Ocupação")
        self.lb_QuartoOcupacao.pack(anchor="w", padx=10, pady=(15, 0))
        Style.LabeHide(self.lb_QuartoOcupacao)

        #
        # lb_QuartoTipo
        #

        self.lb_QuartoTipo.config(text="Tipo")
        self.lb_QuartoTipo.pack(anchor="w", padx=10, pady=(15, 0))
        Style.LabeHide(self.lb_QuartoTipo)

        #
        # lb_QuartoCap
        #

        self.lb_QuartoCap.config(text="Capacidade")
        self.lb_QuartoCap.pack(anchor="w", padx=10, pady=(15, 0))
        Style.LabeHide(self.lb_QuartoCap)

        # 
        # ent_BuscarHospede
        #

        self.ent_BuscarHospede.pack(side="left", padx=10)
        self.ent_BuscarHospede.insert(0, "Buscar:")
        Style.EntryBord(self.ent_BuscarHospede)

        #
        # ent_QuartoBusca
        #

        self.ent_QuartoBusca.pack(side="left", padx=10)
        self.ent_QuartoBusca.insert(0, "Buscar:")
        self.ent_QuartoBusca.config(width=25)
        Style.EntryBord(self.ent_QuartoBusca)

        #
        # ent_QuartoId 
        #

        self.ent_QuartoId.pack(side="left", padx=10)
        self.ent_QuartoId.insert(0, "ID:")
        self.ent_QuartoId.config(width=25)
        Style.EntryBord(self.ent_QuartoId)

        #
        # ent_QuartoNome  
        #

        self.ent_QuartoNome.pack(side="left", padx=10)
        self.ent_QuartoNome.insert(0, "Nome:")
        self.ent_QuartoNome.config(width=25)
        Style.EntryBord(self.ent_QuartoNome)

        #
        # ent_QuartoCap 
        #

        self.ent_QuartoCap.pack(side="left", padx=10)
        self.ent_QuartoCap.insert(0, "Capacidade:")
        self.ent_QuartoCap.config(width=25)
        Style.EntryBord(self.ent_QuartoCap)
        
        #
        # cbb_QuartoOcupacao
        #

        self.cbb_QuartoOcupacao.pack(side="left", padx=10)
        self.cbb_QuartoOcupacao.AddItem({"Tipo 1": "Tipo 2"})
        
        #
        # cbb_QuartoTipo
        #
       
        self.cbb_QuartoTipo.pack(side="left", padx=10)
        self.cbb_QuartoTipo.AddItem({"Tipo 1": "Tipo 2"})

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
        self.btn_BuscarHospede.config(command=lambda: self.btn_BuscarHospede_Click())
        Style.ButtonHide(self.btn_BuscarHospede)

        #
        # btn_EditarHospede
        #

        self.btn_EditarHospede.config(text="Editar")
        self.btn_EditarHospede.pack(side="left", padx=10)
        self.btn_EditarHospede.config(command=lambda: self.FormAbrir_Click(F_EditarHospede))
        Style.ButtonHide(self.btn_EditarHospede)

        #
        # btn_ExcluirHospede
        #

        self.btn_ExcluirHospede.config(text="Excluir")
        self.btn_ExcluirHospede.pack(side="left", padx=10)
        self.btn_ExcluirHospede.config(command=lambda: self.btn_ExcluirHospede_Click())
        Style.ButtonHide(self.btn_ExcluirHospede)

        #
        # btn_AbrirHospede
        #
        
        self.btn_AbrirHospede.config(text="Abrir")
        self.btn_AbrirHospede.pack(side="left", padx=10)
        Style.ButtonHide(self.btn_AbrirHospede)

        #
        # btn_QuartoSalvar
        #

        self.btn_QuartoSalvar.config(text="Salvar")
        self.btn_QuartoSalvar.pack(side="left", padx=10)
        Style.ButtonHide(self.btn_QuartoSalvar)


        #
        # btn_QuartoExcluir
        #

        self.btn_QuartoExcluir.config(text="Excluir")
        self.btn_QuartoExcluir.pack(side="left", padx=10)
        Style.ButtonHide(self.btn_QuartoExcluir)

        #
        # componentes multiplos - buttonsMenu
        #

        self.ButtonsMenu = [
            
            ("Home", self.frm_Home),
            ("Hóspedes", self.frm_Hospedes),
            ("Quartos", self.frm_Quarto),
            ("Funcionários", self.frm_Funcionarios),
            ("Relatório", self.frm_Relatorio),
            ("Configurações", self.frm_Config),
        ]

        for texto, frm in self.ButtonsMenu:

            btn = tk.Button(self.frm_BarraLateral, text=texto, command=lambda f=frm: self.MostraFrame_Click(f))
            Style.ButtonFlat(btn)
            btn.pack(fill="x", padx=10, pady=4, ipady=8)

        #
        # flt_Hospede 
        #
        
        self.flt_Hospede.config(bg=TemaConfig.tema.segundario)
        self.flt_Hospede.config(width=600)
        self.flt_Hospede.pack(fill="both", expand=True)
        Style.FrameListZebrado(self.flt_Hospede)

        #
        # flt_Quarto
        #

        self.flt_Quarto.config(bg=TemaConfig.tema.segundario)
        self.flt_Quarto.config(width=600)
        self.flt_Quarto.pack(fill="both", expand=True)
        Style.FrameListZebrado(self.flt_Quarto)

    def CarregarItem_flt_Hospede(self, listItem):

        for item in listItem:

            self.flt_Hospede.AddItem(item[tb.Hospede.n_Id], item[tb.Hospede.t_Nome ], item["Tipo"], item[ tb.Hospede.n_IdQuarto ])

        Style.FrameListZebrado(self.flt_Hospede)

        #
        # F_principal
        #

        self.fp.title("Accommodation Hotel")
        self.fp.geometry("800x600")
        self.fp.state("zoomed")
