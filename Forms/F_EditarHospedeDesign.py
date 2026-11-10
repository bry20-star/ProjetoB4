# arquivo de desiner

import tkinter as tk
from typing import TYPE_CHECKING
from Styles.Style import Style
from Comps.CustomComps import ComboBox

if TYPE_CHECKING:

    from F_EditarHospede import F_EditarHospede

class Form():

    def InicializarComponentes(self: "F_EditarHospede", master):

        # janela

        self.F_EditarHosp = tk.Toplevel()

        # frames

        self.frm_Conteudo = tk.Frame(self.F_EditarHosp)
        self.frm_IdHospede = tk.Frame(self.frm_Conteudo)
        self.frm_NameHospede = tk.Frame(self.frm_Conteudo)
        self.frm_TipoCobranca = tk.Frame(self.frm_Conteudo)
        self.frm_Quarto = tk.Frame(self.frm_Conteudo)

        # labels

        self.lb_IdHospede = tk.Label(self.frm_IdHospede)
        self.lb_NameHospede = tk.Label(self.frm_NameHospede)
        self.lb_TipoCobranca = tk.Label(self.frm_TipoCobranca)
        self.lb_Quarto = tk.Label(self.frm_Quarto)

        # entry

        self.ent_IdHospede = tk.Entry(self.frm_IdHospede)
        self.ent_NameHospede = tk.Entry(self.frm_NameHospede)

        # combobox

        self.cbb_Quarto = ComboBox(self.frm_Quarto)
        self.cbb_TipoCobranca = ComboBox(self.frm_TipoCobranca)

        # button

        self.btn_Confirmar = tk.Button(self.frm_Conteudo)
                
        #
        # frm_Conteudo
        #

        self.frm_Conteudo.pack(fill="both", expand=True)
        Style.frame.Bord(self.frm_Conteudo) 

        #
        # frm_IdHospede
        #

        self.frm_IdHospede.pack(fill="x", side="top")
        self.frm_IdHospede.config(height=80)
        self.frm_IdHospede.pack_propagate(False)
        Style.frame.Bord(self.frm_IdHospede)

        #
        # frm_NameHospede
        #

        self.frm_NameHospede.pack(fill="x", side="top")
        self.frm_NameHospede.config(height=80)
        self.frm_NameHospede.pack_propagate(False)
        Style.frame.Bord(self.frm_NameHospede)

        #
        # frm_TipoCobranca
        #

        self.frm_TipoCobranca.pack(fill="x", side="top")
        self.frm_TipoCobranca.config(height=80)
        self.frm_TipoCobranca.pack_propagate(False)
        Style.frame.Bord(self.frm_TipoCobranca)

        #
        # frm_Quarto
        #

        self.frm_Quarto.pack(fill="x", side="top")
        self.frm_Quarto.config(height=80)
        self.frm_Quarto.pack_propagate(False)
        Style.frame.Bord(self.frm_Quarto)

        #
        # lb_IdHospede
        #

        self.lb_IdHospede.pack(anchor="w")
        self.lb_IdHospede.config(height=2, text="ID do Hóspede")
        Style.label.Hide(self.lb_IdHospede)

        #
        # lb_NameHospede 
        #

        self.lb_NameHospede.pack(anchor="w")
        self.lb_NameHospede.config(height=2, text="Nome do Hóspede")
        Style.label.Hide(self.lb_NameHospede)

        #
        # lb_TipoCobranca
        #

        self.lb_TipoCobranca.pack(anchor="w")
        self.lb_TipoCobranca.config(height=2, text="Tipo de Cobrança")
        Style.label.Hide(self.lb_TipoCobranca)

        #
        # lb_Quarto 
        #

        self.lb_Quarto.pack(anchor="w")
        self.lb_Quarto.config(height=2, text="ID do Quarto")
        Style.label.Hide(self.lb_Quarto)

        #
        # ent_IdHospede
        #

        self.ent_IdHospede.pack(anchor="w")
        Style.entry.Bord(self.ent_IdHospede) 

        #
        # ent_NameHospede
        #

        self.ent_NameHospede.pack(anchor="w")
        self.ent_NameHospede.config(width=40)
        Style.entry.Bord(self.ent_NameHospede)
        
        #
        # cbb_Quarto 
        #

        self.cbb_Quarto.pack(anchor="w")

        #
        # cbb_TipoCobranca
        #
       
        self.cbb_TipoCobranca.pack(anchor="w")

        #
        # btn_Confirmar
        #

        self.btn_Confirmar.pack(side="bottom", expand=True, fill="both")
        self.btn_Confirmar.config(text="Confirmar")
        self.btn_Confirmar.config(command=lambda: self.Click_btn_Confirmar())
        Style.button.Hide(self.btn_Confirmar)

        #
        # F_EditarHosp
        #
       
        altura = 400
        lagura = 400
        x = (self.F_EditarHosp.winfo_screenwidth() - lagura)//2
        y = (self.F_EditarHosp.winfo_screenheight() - altura)//2
        self.F_EditarHosp.title("Editar Hóspede")
        self.F_EditarHosp.geometry(f"{lagura}x{altura}+{x}+{y}")
        self.F_EditarHosp.resizable(False, False)
        self.F_EditarHosp.transient(master)
        self.F_EditarHosp.grab_set()