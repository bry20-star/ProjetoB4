# arquivo logico

from Form.F_NotaAlunosDesigner import Form

class F_principal(Form):

    def __init__(self):

        self.InicializarComponentes()
    
    def FormAbrir_Click(self, f):

        f(self.fp)

    def SelectCell(self):
        
        if not self.ListView.linhaAtual:
            return

        celula = self.ListView.linhaAtual.GetCell(1)
        if celula:
            print(celula.cget("text"))

        #self.ListView.AddItem("asd","ads","ds","as")
        #if self.ListView.linhaAtual: self.ListView.RemoveItem(self.ListView.linhaAtual)

        # 3. Atualiza o Canvas
        self.ListView.canvas.update_idletasks()

    def MostraFrame_Click(self,frame):

        for i in [self.frm_Home,self.frm_Turmas,self.frm_Alunos, self.frm_Relatorio, self.frm_Config]:

            i.pack_forget()
        
        frame.pack(fill="both", expand=True)
