
# Impotarções

from typing import TYPE_CHECKING
from Form.F_NovoHospedeDesign import Form
from Banco.Banco import Banco
from tkinter import messagebox
from Models.Class import Tabelas as tb

if TYPE_CHECKING:

    from Form.F_Principal import F_principal

class F_NovoHospede(Form):

    def __init__(self, master, fp: "F_principal"):
        
        self.InicializarComponentes(master)

        self.fp = fp

        self.cbb_TipoCobranca.AddItem({"Anual":"A", "Mensal":"M", "Diaria":"D"})

        self.F_Hosp.wait_window()
        

    def Click_btn_Confirmar(self):

        if not self.ent_NameHospede.get().strip():

            messagebox.showerror("Error", f"Campo {self.lb_NameHospede.cget('text')} não pode esta vazio")
            self.ent_NameHospede.focus_set()
            return

        if not self.ent_NameHospede.get().replace(" ", "").isalpha():

            messagebox.showerror("Error", f"Campo {self.lb_NameHospede.cget('text')} não pode ter números ou caracters especiais")
            self.ent_NameHospede.focus_set()
            return

        if len(self.ent_NameHospede.get().strip()) > 200:

            messagebox.showerror("Error", f"Nome muito grande")
            self.ent_NameHospede.focus_set()
            return

        for item in self.fp.flt_Hospede.listLinhas:

            if  self.ent_NameHospede.get().title() == item.list_cells[1].cget("text"):

                messagebox.showerror("Error", "Hóspede já registrado com esse nome")
                self.ent_NameHospede.focus_set()
                return

        if not self.ent_IdQuarto.get().strip():

            messagebox.showerror("Error", f"Campo {self.lb_IdQuarto.cget('text')} não pode esta vazio")
            self.ent_IdQuarto.focus_set()
            return

        if not self.ent_IdQuarto.get().isdigit():

            messagebox.showerror("Error", f"Campo {self.lb_IdQuarto.cget('text')} não pode ter letras ou caracteres especiais")
            self.ent_IdQuarto.focus_set()
            return

        hosp = Banco.AddDado(

            tabela=tb.Hospede.tabela, 
            dados={
            
                tb.Hospede.t_Nome : self.ent_NameHospede.get().title(),
                tb.Hospede.t_TipoCobranca : self.cbb_TipoCobranca.itemAtual.value.title(),
                tb.Hospede.n_IdQuarto : int(self.ent_IdQuarto.get())
            }            
        )

        self.fp.flt_Hospede.AddItem(str(hosp), self.ent_NameHospede.get().title(), self.cbb_TipoCobranca.itemAtual.viewValue.title(), self.ent_IdQuarto.get())

        self.F_Hosp.destroy()