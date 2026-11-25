# importações 

from typing import List
import tkinter as tk
from Styles.Tema import Config

#-------------------------------- CustomFrameList --------------------------------------------------------------------------------------/

class CustomFrameList(tk.Frame):

    def __init__(self, master, pdxColuna: int = 2, pdyColuna: int = 1, pdyItem: int = 1, pdxItem: int = 0):

        super().__init__(master)

        # Frame List

        self.winfo_toplevel().bind_all("<Button-1>", self.__ClickExterno, add="+")

        self.padxColuna = pdxColuna
        self.padyColuna = pdyColuna
        self.padyItem = pdyItem
        self.padxItem = pdxItem
        self.frm_Coluna_bg = Config.tema.segundario
        self.lb_Coluna_bg = Config.tema.primario
        self.ItemColor1 = Config.tema.primario
        self.ItemColor2 = Config.tema.segundario
        self.linhaAtual: CustomFrameListItem = None
        self.linhaAnterio: CustomFrameListItem = None

        self.listColunas: List[CustomFrameListCollum] = []
        self.listLinhas: List[CustomFrameListItem] = []
        self.listSelectLinhas: List[CustomFrameListItem] = []
        
        self.pack_propagate(False)

        # frame scrollbar

        self.frm_Scrollbar = tk.Frame(self, bg=self.ItemColor1)
        self.frm_Scrollbar.config(width=1)
        self.frm_Scrollbar.pack_propagate(False)
        self.frm_Scrollbar.pack(side="right", fill="y")

        # scrollbar

        self.scrollbar = tk.Scrollbar(self.frm_Scrollbar, orient="vertical")
        self.scrollbar.config(activebackground=Config.tema.destaque)
        self.scrollbar.pack(side="right", fill="y")

        # frame coluna

        self.frm_Coluna = tk.Frame(self)
        self.frm_Coluna.config(bg=Config.tema.segundario)
        self.frm_Coluna.pack(side="top", fill="x")

        # canvas

        self.canvas = tk.Canvas(self, bg=Config.tema.primario, highlightthickness=0, yscrollcommand= self.scrollbar.set)
        self.canvas.bind("<Configure>", lambda event: self._AtualizarCanvas(event))
        self.canvas.bind("<Enter>", lambda event: self.canvas.bind_all("<MouseWheel>", lambda event: self.__MouseWheel_Canvas(event)))
        self.canvas.bind("<Leave>", lambda event: self.canvas.unbind_all("<MouseWheel>"))
        self.canvas.pack(fill="both", expand=True)

        self.scrollbar.config(command=self.canvas.yview)

        # frame conteudo

        self.frm_Conteudo = tk.Frame(self.canvas, bg=self.ItemColor1, height=0)
        self.frm_Conteudo.bind("<Configure>", lambda event: self._AtualizarCanvas(event))

        self.canvas_window = self.canvas.create_window(0, 0, window=self.frm_Conteudo, anchor="nw")

    #--------------------- metodos pra sobreescrever -----------------/

    def OnSelectItem(self, event):

        pass

    #--------------------\

    #-------------------------- Metodos Internos -----------------------------------/

    def __MouseWheel_Canvas(self, event):

        if self.scrollbar.get() == (0.0, 1.0): return

        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def __ClickExterno(self, event):

        if isinstance(event.widget, CustomFrameListItem): return
        if isinstance(event.widget, CustomFrameListItemCell): return
        if isinstance(event.widget, tk.Button): return

        if self.linhaAtual:

            self.linhaAtual.config(bg=self.linhaAtual.cellCor)
            self.linhaAtual = None

    def _AtualizarCanvas(self, event):

        self.canvas.itemconfigure(self.canvas_window, width=self.canvas.winfo_width())

        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        self.__AtualizarVisibilidadeScrollbar()

    def __AtualizarVisibilidadeScrollbar(self):

        if self.canvas.winfo_height() < self.canvas.bbox("all")[3] and self.canvas.winfo_height() > 1:

            if not self.scrollbar.winfo_manager():

                self.scrollbar.pack(side="right", fill="y")
                self.frm_Scrollbar.pack_propagate(True)

        else:

            if self.scrollbar.winfo_manager():

                self.scrollbar.pack_forget()
                self.frm_Scrollbar.pack_propagate(False)
                self.frm_Scrollbar.config(width=1)
        
    def _SelectMultiploItem(self, event):

       compAtual = event.widget

       self.linhaAnterio = self.linhaAtual

       if isinstance(compAtual, CustomFrameListItemCell):

            linha: CustomFrameListItem = compAtual.master

       else:

            linha = compAtual

       self.linhaAtual = linha

       if linha in self.listSelectLinhas:

            self.listSelectLinhas.remove(self.linhaAtual)
            self.linhaAtual.config(bg= self.linhaAtual.cellCor)

       else:

            self.listSelectLinhas.append(self.linhaAtual)
            self.linhaAtual.config(bg=Config.tema.destaque)

       self.OnSelectItem(event)

    def _SelectItem(self, event):

        compAtual = event.widget

        if self.listSelectLinhas != []:

            for linha in self.listSelectLinhas:

                linha.config(bg= linha.cellCor)

            self.listSelectLinhas.clear()

        self.linhaAnterio = self.linhaAtual

        if self.linhaAnterio:

            self.linhaAnterio.config(bg=self.linhaAnterio.cellCor)

        if isinstance(compAtual, CustomFrameListItemCell):

            linha = compAtual.master

        else:

            linha = compAtual

        self.linhaAtual = linha


        if self.listSelectLinhas.__contains__(linha):

            self.listSelectLinhas.remove(self.linhaAtual)
            self.linhaAtual.config(bg= self.linhaAtual.cellCor)

        else:

            self.listSelectLinhas.append(self.linhaAtual)
            self.linhaAtual.config(bg=Config.tema.destaque)

        self.canvas.update_idletasks()

        self.OnSelectItem(event)

    #--------------------------------------------------\

    #-------------------------- metodos externos -------------------------------/

    def AddColuna(self,*text):

        for i, collum in enumerate(text):

            CustomFrameListCollum(self, collum, i)
            
        for i in range(len(text)):

            self.frm_Coluna.grid_columnconfigure(i, weight=self.listColunas[i].peso)

    def SetColuna(self, colunaId, peso):

        self.listColunas[colunaId].peso = peso

        self.frm_Coluna.grid_columnconfigure(index=colunaId, weight=peso)

        for item in self.listLinhas:

            item.grid_columnconfigure(index=colunaId, weight=peso)

    def AddItem(self,*items):

        if (len(items) != len(self.listColunas)): 

            if (len(items) > len(self.listColunas)): raise TypeError("Argumentos não existem")

            if (len(items) < len(self.listColunas)): raise TypeError("Argumentos Faltando")

        frm_linha = CustomFrameListItem(self.frm_Conteudo, self, *items)
        self.listLinhas.append(frm_linha)

        return frm_linha

    def RemoveItem(self, item):

        if not item: raise TypeError("item com valor nullo")

        if item in self.listLinhas:

            self.listLinhas.remove(item)

        if item in self.listSelectLinhas:

            self.listSelectLinhas.remove(item)

        if item == self.linhaAtual:

            self.linhaAtual = None

        if item == self.linhaAnterio:

            self.linhaAnterio = None

        item.destroy()

    def GetItem(self, idItem):

        if not isinstance(idItem, int): raise TypeError("parammetro com typo errador")

        if idItem >= len(self.listLinhas) or idItem < 0: raise TypeError("item não existi na lista")

        return self.listLinhas[idItem]

    #----------------------------------------------------------------------\

#---------------------------------------------------------------------------------------------\

#------------------------------------- FrameListItem -----------------------------------------------/

class CustomFrameListItem(tk.Frame):

    def __init__(self, master, flt: CustomFrameList,*items):

        super().__init__(master)

        self.list_cells: list[CustomFrameListItemCell] = []
        self.frm_list = flt
        self.cellCor = flt.ItemColor1 if len(flt.listLinhas) % 2 else flt.ItemColor2
        self.config(bg=self.cellCor)
        self.dados = None

        self.bind("<Button-1>", lambda event: flt._SelectItem(event))
        self.bind("<Configure>", lambda event: flt._AtualizarCanvas(event))
        self.bind("<Enter>", lambda event: self.__Enter(event))
        self.bind("<Leave>", lambda event: self.__Leave(event))
        self.pack(side="top", fill="x") 

        if items:

            for i, item in enumerate(items):

                self.AddCell(i, item)

            for i in range(len(items)):

                self.grid_columnconfigure(i, weight=flt.listColunas[i].peso)
    
    #--------------------- metodos internos -------------------------------/

    def __Leave(self, event):

        if self["bg"] == Config.tema.destaque: return

        self.config(bg=self.cellCor)
    
    def __Enter(self, event):

        if self["bg"] == Config.tema.destaque: return

        self.config(bg=Config.tema.hover)

    #----------------------------------------------------\

    #------------------------- metodos externos ----------------------------------/

    def AddCell(self, i, item):

        cell = CustomFrameListItemCell(self, self.frm_list, i, item)
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

    #----------------------------------------------------------------\

#----------------------------------------------------------------------------------\

#------------------------------ CustomFrameListCollum --------------------------------------------/

class CustomFrameListCollum(tk.Label):

    def __init__(self, flt: CustomFrameList, txt, i):
        
        super().__init__(flt.frm_Coluna, text=txt, width=20)

        self.peso = 1

        self.config(

            bg=flt.lb_Coluna_bg, 
            fg=Config.tema.texto, 
    
        )

        self.grid(row=0, column=i, sticky="nsew", padx=flt.padxColuna, pady=flt.padyItem)
        flt.listColunas.append(self)

#--------------------------------------------------------------------------\

#------------------------------- CustomFrameListItemCell ------------------------------------------/

class CustomFrameListItemCell(tk.Label):

    def __init__(self, master, frm_List: CustomFrameList, index, item):
       
        super().__init__(master, text=item, width=20)    

        self.config(fg=Config.tema.texto)

        self.grid(row=0, column=index, sticky="nsew", pady=frm_List.padyItem)

        self.bind("<Button-1>", lambda event: frm_List._SelectItem(event))
        self.bind("<Button-3>", lambda event: frm_List._SelectMultiploItem(event))

#-------------------------------------------------------------------------------------\