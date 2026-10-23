import tkinter as tk
from Styles.Tema import Tema
from Styles.Style import Style

class FrameList(tk.Frame):

    def __init__(self, master):

        super().__init__(master)

        self.listColunas = []
        self.listLinhas = []
        
        # frame coluna
        self.frm_Coluna = tk.Frame(self)
        self.frm_Coluna.pack(side="top", fill="x")

        # canvas
        self.canvas = tk.Canvas(self, bg="red", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # frame conteudo
        self.frm_Conteudo = tk.Frame(self.canvas, bg=Tema.primario)

        self.canvas_window = self.canvas.create_window((0, 0), window=self.frm_Conteudo, anchor="nw")

        self.frm_Conteudo.bind("<Configure>", self.AtualizarCanvas)

        self.pack_propagate(False)

    def AtualizarCanvas(self, event):

        self.canvas.itemconfigure(self.canvas_window, width=self.canvas.winfo_width())

    def AddColuna(self,*text):

        for i,txt in enumerate(text):

            lb_Coluna = tk.Label(self.frm_Coluna, text=txt, width=20)
            lb_Coluna.config(bg=Tema.segundario, fg=Tema.texto, highlightthickness=1, highlightbackground=Tema.primario)
            lb_Coluna.grid(row=0, column=i, sticky="nsew")

            self.listColunas.append(lb_Coluna)
            
        for i in range(len(text)):

            self.frm_Coluna.grid_columnconfigure(i, weight=1)

    def AddItem(self,*items):
        
        if (len(items) != len(self.listColunas)): 

            if (len(items) > len(self.listColunas)): raise TypeError("Argumentos não existem")

            if (len(items) < len(self.listColunas)): raise TypeError("Argumentos Faltando")

        frm_Linha = tk.Frame(self.frm_Conteudo)
        frm_Linha.bind("<Button-1>", lambda e:self.Frame_Click(frm_Linha))
        frm_Linha.pack(side="top", fill="x")

        for i,item in enumerate(items): 

            lb_item = tk.Label(frm_Linha, text=item, width=20)
            lb_item.config(bg=Tema.segundario, fg=Tema.texto)
            lb_item.grid(row=0, column=i, sticky="nsew")

        for i in range(len(items)):

            frm_Linha.grid_columnconfigure(i, weight=1)

        self.listLinhas.append(frm_Linha)
        
    def Frame_Click(self, event):

        event.config(highlightbackground=Tema.destaque, bg=Tema.destaque)
        print("clicou")

class FrameListItems(tk.Frame):

    def __init__(self, master):

        super().__init__(master)

# outros componetes

class FrameSuperio(tk.Frame):

    def __init__(self, master, **kw):

        super().__init__(master, **kw)

        self.pack_propagate(False)
        self.pack(side="top", fill="x")
        

class FrameInferior(tk.Frame):

    def __init__(self, master, **kw):

        super().__init__(master, **kw)

        self.pack_propagate(False)
        self.pack(side="bottom", fill="x")

