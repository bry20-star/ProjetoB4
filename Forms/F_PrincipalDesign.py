
# Importações 

import tkinter as tk
from typing import TYPE_CHECKING
from Comps.CustomComps import FrameList, ComboBox, NumericUpDown
from Forms.F_NovoHospede import F_NovoHospede
from Forms.F_EditarHospede import F_EditarHospede
from Forms.F_NovoQuarto import F_NovoQuarto
from Forms.F_QuartoReserva import F_QuartoReserva
from Styles.Style import Style
from Styles.Tema import Config

if TYPE_CHECKING:

    from F_Principal import F_principal

#--------------------------------- Form -----------------------------------------------------------------------------------/

class Form():

    def InicializarComponentes(self: "F_principal"):
        
        # janela

        self.fp = tk.Tk()

        self.pw_Panel = tk.PanedWindow(self.fp)

        self.frm_BarraLateral = tk.Frame(self.pw_Panel)
        self.frm_BarraSuperio = tk.Frame(self.fp)
        self.frm_Botoes = tk.Frame(self.frm_BarraLateral)
        self.frm_Conteudo = tk.Frame(self.pw_Panel)

        self.lb_BSTitulo = tk.Label(self.frm_BarraSuperio)
        self.lb_FrameTitulo = tk.Label(self.frm_BarraSuperio)
        self.lb_Menu = tk.Label(self.frm_BarraLateral)

        # frm_Home
      
        self.frm_Home = tk.Frame(self.frm_Conteudo)
        self.lb_HomeTitulo = tk.Label(self.frm_Home)

        # frm_Hospedes

        self.frm_Hospedes = tk.Frame(self.frm_Conteudo)
        self.frm_BuscarHospede = tk.Frame(self.frm_Hospedes)
        self.frm_HospedesBotoes = tk.Frame(self.frm_Hospedes)

        self.lb_BuscarHospede = tk.Label(self.frm_BuscarHospede)

        self.btn_BuscarHospede = tk.Button(self.frm_BuscarHospede)
        self.btn_EditarHospede = tk.Button(self.frm_HospedesBotoes)
        self.btn_ExcluirHospede = tk.Button(self.frm_HospedesBotoes)
        self.btn_AbrirHospede = tk.Button(self.frm_HospedesBotoes)
        self.btn_NovoHospede = tk.Button(self.frm_BuscarHospede)

        self.ent_BuscarHospede = tk.Entry(self.frm_BuscarHospede)

        self.flt_Hospede = FrameList(self.frm_Hospedes)

        # frm_Quarto

        self.frm_Quarto = tk.Frame(self.frm_Conteudo)
        self.frm_QuartoLateral = tk.Frame(self.frm_Quarto)
        self.frm_QuartoBotoes = tk.Frame(self.frm_Quarto)
        self.frm_QuartoBusca = tk.Frame(self.frm_QuartoLateral)
        self.frm_QuartoId = tk.Frame(self.frm_QuartoLateral)
        self.frm_QuartoNome = tk.Frame(self.frm_QuartoLateral)
        self.frm_QuartoEstado = tk.Frame(self.frm_QuartoLateral)
        self.frm_QuartoTipo = tk.Frame(self.frm_QuartoLateral)
        self.frm_QuartoCap = tk.Frame(self.frm_QuartoLateral)

        self.lb_QuartoBusca = tk.Label(self.frm_QuartoBusca)
        self.lb_QuartoId = tk.Label(self.frm_QuartoId)
        self.lb_QuartoNome = tk.Label(self.frm_QuartoNome)
        self.lb_QuartoEstado = tk.Label(self.frm_QuartoEstado)
        self.lb_QuartoTipo = tk.Label(self.frm_QuartoTipo)
        self.lb_QuartoCap = tk.Label(self.frm_QuartoCap)

        self.btn_QuartoSalvar = tk.Button(self.frm_QuartoBotoes)
        self.btn_QuartoExcluir = tk.Button(self.frm_QuartoBotoes)
        self.btn_QuartoNovo = tk.Button(self.frm_QuartoBotoes)
        self.btn_QuartoReserva = tk.Button(self.frm_QuartoBotoes)

        self.ent_QuartoBusca = tk.Entry(self.frm_QuartoBusca)
        self.ent_QuartoId = tk.Entry(self.frm_QuartoId)
        self.ent_QuartoNome = tk.Entry(self.frm_QuartoNome)
        self.nud_QuartoCap = NumericUpDown(self.frm_QuartoCap)
        
        self.cbb_QuartoEstado = ComboBox(self.frm_QuartoEstado)
        self.cbb_QuartoTipo = ComboBox(self.frm_QuartoTipo)

        self.flt_Quarto = FrameList(self.frm_Quarto)

        # frm_Funcionarios

        self.frm_Funcionarios = tk.Frame(self.frm_Conteudo)

        # frm_Relatorio

        self.frm_Relatorio = tk.Frame(self.frm_Conteudo)

        # frm_Config

        self.frm_Config = tk.Frame(self.frm_Conteudo)
        
    #-------------------- Componentes Janela --------------------------------------------------------------------------------------------------------------------------------/

        #
        # Componentes Multiplos - FrameConteudos
        #

        self.frameConteudos = [self.frm_Conteudo, self.frm_Home, self.frm_Hospedes, self.frm_Quarto, self.frm_Funcionarios, self.frm_Relatorio, self.frm_Config]
        
        for frm in self.frameConteudos:

            Style.frame.Base(frm)
            frm.pack_propagate(False)
            frm.forget()
            
        self.frm_Home.pack(fill="both", expand=True)

        #
        # frm_barraLateral
        #

        self.frm_BarraLateral.config(width=200)
        self.frm_BarraLateral.pack(side="left", fill="y")
        self.frm_BarraLateral.pack_propagate(False)
        Style.frame.Bord(self.frm_BarraLateral)

        #
        # frm_barraSuperio
        #

        self.frm_BarraSuperio.config(height=60)
        self.frm_BarraSuperio.pack_propagate(False)
        self.frm_BarraSuperio.pack(side="top", fill="x")
        Style.frame.Bord(self.frm_BarraSuperio)


        #
        # pw_Panel
        #

        self.pw_Panel.config(orient="horizontal")
        self.pw_Panel.config(showhandle=True, sashrelief="flat", sashpad=-2)
        self.pw_Panel.config(bg=Config.tema.destaque, bd=0)
        self.pw_Panel.pack(fill="both", expand=True)
        self.pw_Panel.add(self.frm_BarraLateral)
        self.pw_Panel.add(self.frm_Conteudo)

        #
        # lb_Menu
        #

        self.lb_Menu.config(text="Menu", font=("arial", 15, "bold"))
        self.lb_Menu.pack(fill="x", padx=(1,1), pady=(1,10))
        Style.label.Hide(self.lb_Menu)

        #
        # lb_HomeTitulo
        #

        self.lb_HomeTitulo.config(text="Home", font=Config.tema.fonteTitulo)  
        self.lb_HomeTitulo.pack(anchor="nw", pady=20, padx= 20)
        Style.label.Hide(self.lb_HomeTitulo)

        #
        # lb_BSTitulo
        #

        self.lb_BSTitulo.config(text="Accommodation Hotel", font=Config.tema.fonteTitulo)
        self.lb_BSTitulo.pack(side="left", padx=(10, 0))
        Style.label.Hide(self.lb_BSTitulo)

        #
        # lb_FrameTitulo
        #
        
        self.lb_FrameTitulo.config(text="", font=Config.tema.fonteTitulo)
        self.lb_FrameTitulo.pack(side="left")
        Style.label.Hide(self.lb_FrameTitulo)

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

            btn = tk.Button(self.frm_BarraLateral, text=texto, command=lambda f=frm, t=texto: self.MostraFrame_Click(f, t))
            Style.button.Flat(btn)
            btn.pack(fill="x", padx=10, pady=4, ipady=8)

        #
        # F_principal
        #

        self.fp.title("Accommodation Hotel")
        self.fp.geometry("800x600")
        self.fp.state("zoomed")

    #--------------------------------------------------------------------------------------------------------------------------------\

    #---------------------------------- Componentes Home -------------------------------------------------------------------------------------------------/

    #---------------------------------------------------------------------------------------------------------------------------------------\

    #--------------------------------------------- Componentes Hospedes --------------------------------------------------------------------------------/

        #
        # frm_HospedesPesquisa
        #

        self.frm_BuscarHospede.config(height=60)
        self.frm_BuscarHospede.pack_propagate(False)
        self.frm_BuscarHospede.pack(side="top", fill="x")
        Style.frame.Bord(self.frm_BuscarHospede)

        #
        # frm_HospedesBotoes
        #

        self.frm_HospedesBotoes.config(height=60)
        self.frm_HospedesBotoes.pack_propagate(False)
        self.frm_HospedesBotoes.pack(side="bottom", fill="x")
        Style.frame.Bord(self.frm_HospedesBotoes)

        #
        # lb_HospedesPesquisa
        #

        self.lb_BuscarHospede.config(text="Pesquisa", font=Config.tema.fonte)
        self.lb_BuscarHospede.pack(side="left", padx=10)
        Style.label.Hide(self.lb_BuscarHospede)

        # 
        # ent_BuscarHospede
        #

        self.ent_BuscarHospede.pack(side="left", padx=10)
        self.ent_BuscarHospede.insert(0, "Buscar:")
        Style.entry.Bord(self.ent_BuscarHospede)

        #
        # btn_NovoHospede
        #

        self.btn_NovoHospede.config(text="Novo Hóspede")
        self.btn_NovoHospede.config(command=lambda: self.FormAbrir_Click(F_NovoHospede))
        self.btn_NovoHospede.pack(side="right", padx=10) 
        Style.button.Hide(self.btn_NovoHospede)

        #
        # btn_BuscarHospede
        #

        self.btn_BuscarHospede.config(text="Buscar")
        self.btn_BuscarHospede.pack(side="left", padx=10)
        self.btn_BuscarHospede.config(command=lambda: self.btn_BuscarHospede_Click())
        Style.button.Hide(self.btn_BuscarHospede)

        #
        # btn_EditarHospede
        #

        self.btn_EditarHospede.config(text="Editar")
        self.btn_EditarHospede.pack(side="left", padx=10)
        self.btn_EditarHospede.config(command=lambda: self.FormAbrir_Click(F_EditarHospede))
        Style.button.Hide(self.btn_EditarHospede)

        #
        # btn_ExcluirHospede
        #

        self.btn_ExcluirHospede.config(text="Excluir")
        self.btn_ExcluirHospede.pack(side="left", padx=10)
        self.btn_ExcluirHospede.config(command=lambda: self.btn_ExcluirHospede_Click())
        Style.button.Hide(self.btn_ExcluirHospede)

        #
        # btn_AbrirHospede
        #
        
        self.btn_AbrirHospede.config(text="Abrir")
        self.btn_AbrirHospede.pack(side="left", padx=10)
        Style.button.Hide(self.btn_AbrirHospede)

        #
        # flt_Hospede
        #

        self.flt_Hospede.config(bg=Config.tema.segundario)
        self.flt_Hospede.config(width=600)
        self.flt_Hospede.pack(fill="both", expand=True)
        Style.frameList.Zebrado(self.flt_Hospede)

    #-----------------------------------------------------------------------------------------------------------------------\

    #-------------------- Componentes Quartos ----------------------------------------------------------------------------------------------------------/

        #
        # frm_QuartoBotoes
        #

        self.frm_QuartoBotoes.config(height=60)
        self.frm_QuartoBotoes.pack(side="bottom", fill="x")
        self.frm_QuartoBotoes.pack_propagate(False)
        Style.frame.Bord(self.frm_QuartoBotoes)

        #
        # frm_QuartoLateral
        #

        self.frm_QuartoLateral.config(width=400)
        self.frm_QuartoLateral.pack(side="right", fill="y")
        self.frm_QuartoLateral.pack_propagate(False)
        Style.frame.Bord(self.frm_QuartoLateral)

        #
        # frm_QuartoBusca
        #

        self.frm_QuartoBusca.config(height=60)
        self.frm_QuartoBusca.pack(side="top", fill="x", pady=(0, 20))
        self.frm_QuartoBusca.pack_propagate(False)
        Style.frame.Bord(self.frm_QuartoBusca)

        #
        # frm_QuartoId
        #

        self.frm_QuartoId.config(height=80)
        self.frm_QuartoId.pack(side="top", fill="x", expand=True)
        self.frm_QuartoId.pack_propagate(False)
        Style.frame.Bord(self.frm_QuartoId)

        #
        # frm_QuartoNome
        #

        self.frm_QuartoNome.config(height=80)
        self.frm_QuartoNome.pack(side="top", fill="x", expand=True)
        self.frm_QuartoNome.pack_propagate(False)
        Style.frame.Bord(self.frm_QuartoNome)

        #
        # frm_QuartoEstado
        #

        self.frm_QuartoEstado.config(height=80)
        self.frm_QuartoEstado.pack(side="top", fill="x", expand=True)
        self.frm_QuartoEstado.pack_propagate(False)
        Style.frame.Bord(self.frm_QuartoEstado)

        #
        # frm_QuartoTipo
        #

        self.frm_QuartoTipo.config(height=80)
        self.frm_QuartoTipo.pack(side="top", fill="x", expand=True)
        self.frm_QuartoTipo.pack_propagate(False)
        Style.frame.Bord(self.frm_QuartoTipo)

        #
        # frm_QuartoCap
        #

        self.frm_QuartoCap.config(height=80)
        self.frm_QuartoCap.pack(side="top", fill="x", expand=True, pady=(0, 20))
        self.frm_QuartoCap.pack_propagate(False)
        Style.frame.Bord(self.frm_QuartoCap)

        #
        # lb_QuartoBusca
        #

        self.lb_QuartoBusca.config(text="Pesquisa", font=Config.tema.fonte)
        self.lb_QuartoBusca.pack(side="left", padx=10)
        Style.label.Hide(self.lb_QuartoBusca)

        #
        # lb_QuartoId
        #

        self.lb_QuartoId.config(text="ID do quarto")
        self.lb_QuartoId.pack(anchor="w", padx=10, pady=(15, 0))
        Style.label.Hide(self.lb_QuartoId)

        #
        # lb_QuartoNome
        #

        self.lb_QuartoNome.config(text="Quarto")
        self.lb_QuartoNome.pack(anchor="w", padx=10, pady=(15, 0))
        Style.label.Hide(self.lb_QuartoNome)

        #
        # lb_QuartoOcupacao
        #

        self.lb_QuartoEstado.config(text="Estado")
        self.lb_QuartoEstado.pack(anchor="w", padx=10, pady=(15, 0))
        Style.label.Hide(self.lb_QuartoEstado)

        #
        # lb_QuartoTipo
        #

        self.lb_QuartoTipo.config(text="Tipo de quarto")
        self.lb_QuartoTipo.pack(anchor="w", padx=10, pady=(15, 0))
        Style.label.Hide(self.lb_QuartoTipo)

        #
        # lb_QuartoCap
        #

        self.lb_QuartoCap.config(text="Capacidade")
        self.lb_QuartoCap.pack(anchor="w", padx=10, pady=(15, 0))
        Style.label.Hide(self.lb_QuartoCap)

        #
        # ent_QuartoBusca
        #

        self.ent_QuartoBusca.pack(side="left", padx=10)
        self.ent_QuartoBusca.bind("<KeyRelease>", lambda event: self.KeyRelease_ent_QuartoBusca(event))
        self.ent_QuartoBusca.config(width=25)
        self.ent_QuartoBusca_text = "Buscar:"
        self.ent_QuartoBusca.insert(0, self.ent_QuartoBusca_text)
        Style.entry.Bord(self.ent_QuartoBusca)

        #
        # ent_QuartoId 
        #

        self.ent_QuartoId.pack(side="left", padx=10)
        self.ent_QuartoId.insert(0, "Ex: 10")
        self.ent_QuartoId.config(width=25, state="readonly")
        Style.entry.Bord(self.ent_QuartoId)

        #
        # ent_QuartoNome  
        #

        self.ent_QuartoNome.pack(side="left", padx=10)
        self.ent_QuartoNome.insert(0, "Ex: Quarto01")
        self.ent_QuartoNome.config(width=25)
        Style.entry.Bord(self.ent_QuartoNome)

        #
        # nud_QuartoCap 
        #

        self.nud_QuartoCap.pack(side="left", padx=10)
        self.nud_QuartoCap.SetValueMin(1)
        self.nud_QuartoCap.config(width=25)
        Style.numericUpDown.Flat(self.nud_QuartoCap)

        #
        # cbb_QuartoEstado
        #

        self.cbb_QuartoEstado.pack(side="left", padx=10)
        self.cbb_QuartoEstado.ent_Box.config(state="readonly")

        #
        # cbb_QuartoTipo
        #
       
        self.cbb_QuartoTipo.pack(side="left", padx=10)
        self.cbb_QuartoTipo.ent_Box.config(state="readonly")

        #
        # btn_QuartoSalvar
        #

        self.btn_QuartoSalvar.config(text="Salvar")
        self.btn_QuartoSalvar.pack(side="left", padx=10)
        self.btn_QuartoSalvar.config(command=self.Click_btn_QuartoSalvar)
        Style.button.Hide(self.btn_QuartoSalvar)

        #
        # btn_QuartoExcluir
        #

        self.btn_QuartoExcluir.config(text="Excluir")
        self.btn_QuartoExcluir.pack(side="left", padx=10)
        self.btn_QuartoExcluir.config(command=self.Click_btn_QuartoExcluir)
        Style.button.Hide(self.btn_QuartoExcluir)

        #
        # btn_QuartoNovo
        #

        self.btn_QuartoNovo.config(text="Novo")
        self.btn_QuartoNovo.pack(side="left", padx=10)
        self.btn_QuartoNovo.config(command= lambda: self.FormAbrir_Click(F_NovoQuarto))
        Style.button.Hide(self.btn_QuartoNovo)

        #
        # btn_QuartoReserva
        #

        self.btn_QuartoReserva.config(text="Reserva")
        self.btn_QuartoReserva.pack(side="left", padx=10)
        self.btn_QuartoReserva.config(command= lambda: self.FormAbrir_Click(F_QuartoReserva))
        Style.button.Hide(self.btn_QuartoReserva)

        #
        # flt_Quarto
        #

        self.flt_Quarto.config(bg=Config.tema.segundario)
        self.flt_Quarto.config(width=600)
        self.flt_Quarto.pack(fill="both", expand=True)
        self.flt_Quarto.OnSelectItem = self.SelectItem_Quarto
        Style.frameList.Zebrado(self.flt_Quarto)

    #------------------------------------------------------------------------------------------------\

    #--------------------- Componentes Funcionarios --------------------------------------------------------------------------/

    #-------------------------------------------------------------------------------------------------\

    #----------------------- Componentes Relatorio ---------------------------------------------------------------------/

    #-----------------------------------------------------------------------------------------\

    #-------------------- Componentes Config -----------------------------------------------------------------------/

    #---------------------------------------------------------------------------------------\

#---------------------------------------------------------------------------------------------------------------------------------------------------------\