
# importações 

from Banco.Banco import Banco
from Forms.F_PrincipalDesign import Form
from Forms.F_EditarHospede import F_EditarHospede
from Forms.F_Login import F_Login
import tkinter as tk
from tkinter import messagebox
from Modelos.Tabelas import Tabelas as tb

#------------------------------------------------------- F_principal -----------------------------------------------------------------------/

class F_principal(Form):

    def __init__(self):

        F_Login()

        self.InicializarComponentes()

        self.itemAtualQuarto = None

        # Frame Hospedes

        self.flt_Hospede.AddColuna("ID", "Hóspede", "Tipo Cobrança", "Quarto")

        dados = Banco.DQL(f"""

            SELECT *,

                CASE

                    WHEN {tb.Hospede.t_TipoCobranca} = '{ tb.Hospede.anual["value"] }' THEN '{ tb.Hospede.anual["view"] }' 
                    WHEN {tb.Hospede.t_TipoCobranca} = '{ tb.Hospede.mensal["value"] }' THEN '{ tb.Hospede.mensal["view"] }' 
                    WHEN {tb.Hospede.t_TipoCobranca} = '{ tb.Hospede.diaria["value"] }' THEN '{ tb.Hospede.diaria["view"] }'
                    
                END as 'tipo'
                    
                FROM 

                    {tb.Hospede.tabela} as 'tbh'
                    
                INNER JOIN {tb.Quarto.tabela} as 'tbq' ON tbq.{tb.Quarto.n_Id} = tbh.{tb.Hospede.n_IdQuarto}
                    
        """)

        for i, dado in  enumerate(dados):

            self.flt_Hospede.AddItem(dado[tb.Hospede.n_Id], dado[tb.Hospede.t_Nome], dado["Tipo"], dado[tb.Quarto.t_Nome])
            self.flt_Hospede.listLinhas[i].dados = dado

        self.flt_Hospede.SetColuna(colunaId=0, peso=1)
        self.flt_Hospede.SetColuna(colunaId=1, peso=3)
        self.flt_Hospede.SetColuna(colunaId=2, peso=1)
        self.flt_Hospede.SetColuna(colunaId=3, peso=1)

        # Frame Quartos

        self.flt_Quarto.AddColuna("ID","Quarto")

        dados = Banco.DQL(f"""
            
            SELECT *,

                CASE 

                    WHEN {tb.Quarto.t_Tipo} = '{tb.Quarto.standard["value"]}' THEN '{tb.Quarto.standard["view"]}'
                    WHEN {tb.Quarto.t_Tipo} = '{tb.Quarto.luxo["value"]}' THEN '{tb.Quarto.luxo["view"]}'
                    WHEN {tb.Quarto.t_Tipo} = '{tb.Quarto.suite["value"]}' THEN '{tb.Quarto.suite["view"]}'

                END as 'tipo',

                CASE 

                    WHEN {tb.Quarto.t_Estado} = '{tb.Quarto.disponivel["value"]}' THEN '{tb.Quarto.disponivel["view"]}'
                    WHEN {tb.Quarto.t_Estado} = '{tb.Quarto.oculpado["value"]}' THEN '{tb.Quarto.oculpado["view"]}'
                    WHEN {tb.Quarto.t_Estado} = '{tb.Quarto.bloqueado["value"]}' THEN '{tb.Quarto.bloqueado["view"]}'

                END as 'estado'

            FROM
                
                {tb.Quarto.tabela}
        
        """)

        for i, dado in enumerate(dados):

            self.flt_Quarto.AddItem(dado[tb.Quarto.n_Id], dado[tb.Quarto.t_Nome])
            self.flt_Quarto.listLinhas[i].dados = dado


        self.flt_Quarto.SetColuna(colunaId=0, peso=1)
        self.flt_Quarto.SetColuna(colunaId=1, peso=3)

        # combobox - imcorporando 

        self.cbb_QuartoEstado.AddItem({
        
            tb.Quarto.disponivel["view"] : tb.Quarto.disponivel["value"], 
            tb.Quarto.oculpado["view"] : tb.Quarto.oculpado["value"], 
            tb.Quarto.bloqueado["view"] : tb.Quarto.bloqueado["value"]
            
        })

        self.cbb_QuartoTipo.AddItem({
        
            tb.Quarto.standard["view"] : tb.Quarto.standard["value"], 
            tb.Quarto.luxo["view"] : tb.Quarto.luxo["value"], 
            tb.Quarto.suite["view"] : tb.Quarto.suite["value"]
            
        })

        self.fp.mainloop()

    #------------------ Janela ------------------------------------------------------------------/

    def FormAbrir_Click(self, f):

        if f == F_EditarHospede:
            
            if not self.flt_Hospede.linhaAtual: 
                
                messagebox.showerror("Error","Nenhum Hóspede selecionador")
                return 

        f(self.fp, self)

    def MostraFrame_Click(self, frame, txt):

        for i in self.frameConteudos:

            i.pack_forget()
        
        frame.pack(fill="both", expand=True)
        self.lb_FrameTitulo.config(text=" - " + txt)

    #------------------------------------------------------------------------------------------------------------------------------------------\

    #--------- Frame Hospede ---------------------------------------------------------------------------------------------------------------------------/

    def btn_ExcluirHospede_Click(self):

        if not self.flt_Hospede.linhaAtual: 
            
            messagebox.showerror("Error","Nenhum Hóspede selecionador")
            return

        if (not messagebox.askyesno("Excluir?" ,"Deseja Excluir Hóspede?")): return

        Banco.DeleteDado(int(self.flt_Hospede.linhaAtual.list_cells[0].cget("text")), tb.Hospede.tabela, tb.Hospede.n_Id )

        self.flt_Hospede.RemoveItem(self.flt_Hospede.linhaAtual)
        
    def btn_BuscarHospede_Click(self):

        if self.ent_BuscarHospede.get() == "" or self.ent_BuscarHospede.get() == "Buscar:" : 

            for item in self.flt_Hospede.listLinhas:

                item.pack_forget()

            for item in self.flt_Hospede.listLinhas:

                item.pack(fill="x", expand=True)
            
            return

        for item in self.flt_Hospede.listLinhas:

            item.pack(fill="x", expand=True)

            if not self.ent_BuscarHospede.get().lower() in str(item.dados[tb.Hospede.t_Nome]).lower():

                item.pack_forget()

    #----------------------------------------------------------------------------------------------------------\

    #-------- Frame Quartos ----------------------------------------------------------------------------------------------/

    def SelectItem_Quarto(self, event):

        if not self.flt_Quarto.linhaAtual: return

        item = self.flt_Quarto.linhaAtual
        self.itemAtualQuarto = item

        self.ent_QuartoId.config(state="normal")
        self.ent_QuartoId.delete(0, tk.END)
        self.ent_QuartoId.insert(0, item.list_cells[0].cget("text"))
        self.ent_QuartoId.config(state="readonly")
        self.ent_QuartoNome.delete(0, tk.END)
        self.ent_QuartoNome.insert(0, self.flt_Quarto.linhaAtual.list_cells[1].cget("text"))

        self.cbb_QuartoEstado.SetItem(item.dados["estado"])
        self.cbb_QuartoTipo.SetItem(item.dados["tipo"])

        self.nud_QuartoCap.SetValue(item.dados[tb.Quarto.n_Cap])

    def KeyRelease_ent_QuartoBusca(self, event):

        if not self.ent_QuartoBusca.get(): 

            for item in self.flt_Quarto.listLinhas:

                item.pack(fill="x", expand=True)

        buscar = self.ent_QuartoBusca.get().replace(" ","").lower()

        for item in self.flt_Quarto.listLinhas:

            item.pack_forget()

        for item in self.flt_Quarto.listLinhas:

            item.pack(fill="x", expand=True)

            if not buscar in str(item.dados[tb.Quarto.t_Nome]).replace(" ","").lower():

                item.pack_forget()

    def Click_btn_QuartoExcluir(self):

        item = self.flt_Quarto.linhaAtual

        if not item:

            messagebox.showerror("Error", "Nenhum Quarto selecionador")
            return

        for hosp in self.flt_Hospede.listLinhas:

            if hosp.dados[tb.Quarto.n_Id] == item.dados[tb.Quarto.n_Id]:
                
                messagebox.showerror(f"não foi possivel excluir o quarto", f"Existem hóspedes hospedados nesse quarto")
                return

        if not messagebox.askyesno("Excluir Quarto", "Deseja excluir esse quarto?"): return

        Banco.DeleteDado(
        
            tabela=tb.Quarto.tabela,
            idKey=tb.Quarto.n_Id,
            dadoId=item.dados[tb.Quarto.n_Id]
        )

        self.flt_Quarto.RemoveItem(

            item=item
        )

        self.itemAtualQuarto = None

        self.ent_QuartoId.config(state="normal")
        self.ent_QuartoId.delete(0,tk.END)
        self.ent_QuartoId.insert(0, "Ex: 10")
        self.ent_QuartoId.config(state="readonly")
        self.ent_QuartoNome.delete(0, tk.END)
        self.ent_QuartoNome.insert(0, "Ex: Quarto01")

        self.nud_QuartoCap.SetValue(self.nud_QuartoCap._valueMin)

    def Click_btn_QuartoSalvar(self):

        if not self.itemAtualQuarto:

            messagebox.showerror("Error", "Nenhum Quarto Selecionador")
            return

        # campo nome quarto

        ent = self.ent_QuartoNome

        if not ent.get().strip():

            messagebox.showerror("Error", f"Campo {self.lb_QuartoNome.cget('text')} não pode esta vazio")
            ent.focus_set()
            return

        if "  " in ent.get().strip():

            messagebox.showerror("Error", f"Campo {self.lb_QuartoNome.cget('text')} não pode ter espaços duplos")
            ent.focus_set()
            return
        
        for l in ent.get().replace(" ",""):

            if l.isdigit(): continue

            if l.isalpha(): continue

            messagebox.showerror("Error", f"Campo {self.lb_QuartoNome.cget('text')} não pode ter caracteres especiais")
            ent.focus_set()
            return

        for item in self.flt_Quarto.listLinhas:

            if str(item.dados[tb.Quarto.t_Nome]).replace(" ", "").lower() == ent.get().replace(" ", "").lower() and item.dados[tb.Quarto.n_Id] != int(self.ent_QuartoId.get()):

                messagebox.showerror("Error", "Quarto já registrado com esse nome")
                ent.focus_set()
                return

        # salvando dados

        Banco.SetDado(
            
            tabela=tb.Quarto.tabela,
            dadoId= self.itemAtualQuarto.dados[tb.Quarto.n_Id],
            idKey=tb.Quarto.n_Id,

            dados={
                
                tb.Quarto.t_Nome:  self.ent_QuartoNome.get().strip(),
                tb.Quarto.t_Estado: self.cbb_QuartoEstado.itemAtual.value,
                tb.Quarto.t_Tipo: self.cbb_QuartoTipo.itemAtual.value,
                tb.Quarto.n_Cap: self.nud_QuartoCap._value
            }

        )

        self.itemAtualQuarto.list_cells[1].config(text=self.ent_QuartoNome.get().strip())

        dados = Banco.DQL(f"""
            
            SELECT *,

                CASE 

                    WHEN {tb.Quarto.t_Tipo} = '{tb.Quarto.standard["value"]}' THEN '{tb.Quarto.standard["view"]}'
                    WHEN {tb.Quarto.t_Tipo} = '{tb.Quarto.luxo["value"]}' THEN '{tb.Quarto.luxo["view"]}'
                    WHEN {tb.Quarto.t_Tipo} = '{tb.Quarto.suite["value"]}' THEN '{tb.Quarto.suite["view"]}'

                END as 'tipo',

                CASE 

                    WHEN {tb.Quarto.t_Estado} = '{tb.Quarto.disponivel["value"]}' THEN '{tb.Quarto.disponivel["view"]}'
                    WHEN {tb.Quarto.t_Estado} = '{tb.Quarto.oculpado["value"]}' THEN '{tb.Quarto.oculpado["view"]}'
                    WHEN {tb.Quarto.t_Estado} = '{tb.Quarto.bloqueado["value"]}' THEN '{tb.Quarto.bloqueado["view"]}'

                END as 'estado'

            FROM
                
                {tb.Quarto.tabela}
        
                WHERE {tb.Quarto.n_Id} = {self.itemAtualQuarto.dados[tb.Quarto.n_Id]}
                
        """)

        self.itemAtualQuarto.dados = dados[0]

        for item in self.flt_Hospede.listLinhas:
           
            if item.dados[tb.Hospede.n_IdQuarto] == int(self.ent_QuartoId.get()):

                item.list_cells[3].config(text=self.ent_QuartoNome.get().strip())

        messagebox.showinfo("Salvar", "Quarto salvor com sucesso")

    #----------------------------------------------------------------------------------------\

#-----------------------------------------------------------------------------------------------------------\