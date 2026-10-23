# arquivo logico

from Form.F_NotaAlunosDesigner import Form

class F_principal(Form):

    def __init__(self):

        self.InicializarComponentes()
    
    def FormAbrir_Click(self, f):

        f(self.F_principal)

    def MostraFrame_Click(self,frame):

        for i in [self.frm_Home,self.frm_Turmas,self.frm_Alunos, self.frm_Relatorio, self.frm_Config]:

            i.pack_forget()
        
        frame.pack(fill="both", expand=True)
