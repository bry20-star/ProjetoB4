from typing import List
import tkinter as tk
from Styles.Style import Style
from Styles.Style import TemaConfig

class FrameList(tk.Frame):

    def __init__(self, master, pdxColuna=2, pdyItems=1):

        super().__init__(master)

        self.winfo_toplevel().bind_all("<Button-1>", self.__ClickExterno)
        self.padxColuna = pdxColuna
        self.padyItems = pdyItems
        self.ItemColor1 = TemaConfig.tema.primario
        self.ItemColor2 = TemaConfig.tema.segundario
        self.linhaAtual: FrameListItem = None
        self.linhaAnterio: FrameListItem = None

        self.listColunas: List[tk.Label] = []
        self.listLinhas: List[FrameListItem] = []

        # frame coluna
        self.frm_Coluna = tk.Frame(self)
        self.frm_Coluna.config(bg=TemaConfig.tema.segundario)
        self.frm_Coluna.pack(side="top", fill="x")

        self.scrollbar = tk.Scrollbar(self, orient="vertical")
        self.scrollbar.config(activebackground=TemaConfig.tema.destaque)
        self.scrollbar.pack(side="right", fill="y")

        # canvas
        self.canvas = tk.Canvas(self, bg=TemaConfig.tema.primario, highlightthickness=0, yscrollcommand= self.scrollbar.set)
        self.canvas.bind("<Configure>", lambda event: self._AtualizarCanvas(event))
        self.canvas.pack(fill="both", expand=True)

        self.scrollbar.config(command=self.canvas.yview)

        # frame conteudo
        self.frm_Conteudo = tk.Frame(self.canvas, bg=self.ItemColor1, height=0)

        self.canvas_window = self.canvas.create_window(0, 0, window=self.frm_Conteudo, anchor="nw")

        self.frm_Conteudo.bind("<Configure>", lambda event: self._AtualizarCanvas(event))

        self.pack_propagate(False)

    #--------------------- metodos pra sobreescrever -----------------

    def OnSelectItem(self):

        pass

    #--------------------

    def __ClickExterno(self, event):

        if isinstance(event.widget, FrameListItem): return
        if isinstance(event.widget, Cells): return
        if isinstance(event.widget, tk.Button): return
        if self.linhaAtual:

            self.linhaAtual.config(bg=self.linhaAtual.cellCor)
            self.linhaAtual = None

    def _AtualizarCanvas(self, event):

        self.canvas.itemconfigure(self.canvas_window, width=self.canvas.winfo_width())

        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def AddColuna(self,*text):

        for i,txt in enumerate(text):

            lb_Coluna = tk.Label(self.frm_Coluna, text=txt, width=20)

            lb_Coluna.config(

                bg=self.ItemColor1, 
                fg=TemaConfig.tema.texto, 
    
            )

            lb_Coluna.grid(row=0, column=i, sticky="nsew", padx=self.padxColuna, pady=self.padyItems)

            self.listColunas.append(lb_Coluna)
            
        for i in range(len(text)):

            self.frm_Coluna.grid_columnconfigure(i, weight=1)

    def AddItem(self,*items):
        
        if (len(items) != len(self.listColunas)): 

            if (len(items) > len(self.listColunas)): raise TypeError("Argumentos não existem")

            if (len(items) < len(self.listColunas)): raise TypeError("Argumentos Faltando")
        
        frm_linha = FrameListItem(self.frm_Conteudo, self, *items)

        self.listLinhas.append(frm_linha)
        
    def _SelectItem(self, event):

        compAtual = event.widget

        self.linhaAnterio = self.linhaAtual

        if self.linhaAnterio:

            self.linhaAnterio.config(bg=self.linhaAnterio.cellCor)

        if isinstance(compAtual, Cells):

            linha = compAtual.master

        else:

            linha = compAtual

        self.linhaAtual = linha

        self.linhaAtual.config(bg=TemaConfig.tema.destaque)

        self.canvas.update_idletasks()

        self.OnSelectItem()

    def RemoveItem(self, item):

        if not item: raise TypeError("item com valor nullo")

        if item in self.listLinhas:

            self.listLinhas.remove(item)

        if item == self.linhaAtual:

            self.linhaAtual = None

        if item == self.linhaAnterio:

            self.linhaAnterio = None

        item.destroy()

    def GetItem(self, idItem):

        if not isinstance(idItem, int): return None

        if idItem >= len(self.listLinhas) or idItem < 0: return None

        return self.listLinhas[idItem]


class FrameListItem(tk.Frame):

    def __init__(self, master, frm_list: FrameList,*items):

        super().__init__(master)

        self.list_cells: list[Cells] = []
        self.frm_list = frm_list
        self.cellCor = frm_list.ItemColor1 if len(frm_list.listLinhas) % 2 else frm_list.ItemColor2
        self.config(bg=self.cellCor)

        self.bind("<Button-1>", lambda event: frm_list._SelectItem(event))
        self.bind("<Configure>", lambda event: frm_list._AtualizarCanvas(event))
        self.bind("<Enter>", lambda event: self.__Enter(event))
        self.bind("<Leave>", lambda event: self.__Leave(event))
        self.pack(side="top", fill="x") 

        if items:

            for i, item in enumerate(items):

                self.AddCell(i, item)

            for i in range(len(items)):

                self.grid_columnconfigure(i, weight=1)
    
    def __Leave(self, event):

        if self["bg"] == TemaConfig.tema.destaque: return

        self.config(bg=self.cellCor)
    
    def __Enter(self, event):

        if self["bg"] == TemaConfig.tema.destaque: return

        self.config(bg=TemaConfig.tema.hover)

    def AddCell(self, i, item):

        cell = Cells(self, self.frm_list, i, item)
        cell.config(bg=self.cellCor)
        self.list_cells.append(cell)

    def GetCell(self, item):

        if isinstance(item, int) or (isinstance(item, str) and item.isdigit()):
        
            itemId = int(item) 
        
            if itemId >= 0 and itemId < len(self.list_cells):

                return self.list_cells[itemId]

            return None 

        else:

            for cell in self.list_cells:
               
                if cell.cget("text") == item:

                    return cell 
                
            return None 
       
class Cells(tk.Label):

    def __init__(self, master, frm_List: FrameList, index, item):
       
        super().__init__(master, text=item, width=20)    

        self.config(fg=TemaConfig.tema.texto)

        self.grid(row=0, column=index, sticky="nsew", pady=frm_List.padyItems)

        self.bind("<Button-1>", lambda event: frm_List._SelectItem(event))
