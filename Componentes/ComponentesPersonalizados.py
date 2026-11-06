# importações 
from string import Template
from turtle import bgcolor
from typing import List
import tkinter as tk
from Styles.Style import Style
from Styles.Style import TemaConfig

class FrameList(tk.Frame):

    def __init__(self, master, pdxColuna: int = 2, pdyColuna: int = 1, pdyItem: int = 1, pdxItem: int = 0):

        super().__init__(master)

        self.winfo_toplevel().bind_all("<Button-1>", self.__ClickExterno)
        self.padxColuna = pdxColuna
        self.padyColuna = pdyColuna
        
        self.padyItem = pdyItem
        self.padxItem = pdxItem
        self.frm_Coluna_bg = TemaConfig.tema.segundario
        self.lb_Coluna_bg = TemaConfig.tema.primario
        self.ItemColor1 = TemaConfig.tema.primario
        self.ItemColor2 = TemaConfig.tema.segundario
        self.linhaAtual: FrameListItem = None
        self.linhaAnterio: FrameListItem = None

        self.listColunas: List[FrameListCollum] = []
        self.listLinhas: List[FrameListItem] = []
        
        self.pack_propagate(False)

        # frame scrollbar
        self.frm_Scrollbar = tk.Frame(self, bg=self.ItemColor1)
        self.frm_Scrollbar.config(width=1)
        self.frm_Scrollbar.pack_propagate(False)
        self.frm_Scrollbar.pack(side="right", fill="y")

        # scrollbar
        self.scrollbar = tk.Scrollbar(self.frm_Scrollbar, orient="vertical")
        self.scrollbar.config(activebackground=TemaConfig.tema.destaque)
        self.scrollbar.pack(side="right", fill="y")

        # frame coluna
        self.frm_Coluna = tk.Frame(self)
        self.frm_Coluna.config(bg=TemaConfig.tema.segundario)
        self.frm_Coluna.pack(side="top", fill="x")

        # canvas
        self.canvas = tk.Canvas(self, bg=TemaConfig.tema.primario, highlightthickness=0, yscrollcommand= self.scrollbar.set)
        self.canvas.bind("<Configure>", lambda event: self._AtualizarCanvas(event))
        self.canvas.bind("<Enter>", lambda event: self.canvas.bind_all("<MouseWheel>", lambda event: self.__MouseWheel_Canvas(event)))
        self.canvas.bind("<Leave>", lambda event: self.canvas.unbind_all("<MouseWheel>"))
        self.canvas.pack(fill="both", expand=True)

        self.scrollbar.config(command=self.canvas.yview)

        # frame conteudo
        self.frm_Conteudo = tk.Frame(self.canvas, bg=self.ItemColor1, height=0)
        self.frm_Conteudo.bind("<Configure>", lambda event: self._AtualizarCanvas(event))

        self.canvas_window = self.canvas.create_window(0, 0, window=self.frm_Conteudo, anchor="nw")

    #--------------------- metodos pra sobreescrever -----------------

    def OnSelectItem(self):

        pass

    #--------------------

    #-------------------------- Metodos Internos -----------------------------------

    def __MouseWheel_Canvas(self, event):

        if self.scrollbar.get() == (0.0, 1.0): return

        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


    def __ClickExterno(self, event):

        if isinstance(event.widget, FrameListItem): return
        if isinstance(event.widget, FrameListItemCell): return
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
        
    def _SelectItem(self, event):

        compAtual = event.widget

        self.linhaAnterio = self.linhaAtual

        if self.linhaAnterio:

            self.linhaAnterio.config(bg=self.linhaAnterio.cellCor)

        if isinstance(compAtual, FrameListItemCell):

            linha = compAtual.master

        else:

            linha = compAtual

        self.linhaAtual = linha

        self.linhaAtual.config(bg=TemaConfig.tema.destaque)

        self.canvas.update_idletasks()

        self.OnSelectItem()

    #--------------------------------------------------

    #-------------------------- metodos externos -------------------------------

    def AddColuna(self,*text):

        for i, collum in enumerate(text):

            FrameListCollum(self, collum, i)
            
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

        frm_linha = FrameListItem(self.frm_Conteudo, self, *items)
        self.listLinhas.append(frm_linha)

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

        if not isinstance(idItem, int): raise TypeError("parammetro com typo errador")

        if idItem >= len(self.listLinhas) or idItem < 0: raise TypeError("item não existi na lista")

        return self.listLinhas[idItem]

    #----------------------------------------------------------------------

class FrameListItem(tk.Frame):

    def __init__(self, master, flt: FrameList,*items):

        super().__init__(master)

        self.list_cells: list[FrameListItemCell] = []
        self.frm_list = flt
        self.cellCor = flt.ItemColor1 if len(flt.listLinhas) % 2 else flt.ItemColor2
        self.config(bg=self.cellCor)

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
    
    #--------------------- metodos internos -------------------------------

    def __Leave(self, event):

        if self["bg"] == TemaConfig.tema.destaque: return

        self.config(bg=self.cellCor)
    
    def __Enter(self, event):

        if self["bg"] == TemaConfig.tema.destaque: return

        self.config(bg=TemaConfig.tema.hover)

    #--------------------------------

    #------------------------- metodos externos ----------------------------------

    def AddCell(self, i, item):

        cell = FrameListItemCell(self, self.frm_list, i, item)
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

    #----------------------------------------------------------------

class FrameListCollum(tk.Label):

    def __init__(self, flt: FrameList, txt, i):
        
        super().__init__(flt.frm_Coluna, text=txt, width=20)

        self.peso = 1

        self.config(

            bg=flt.lb_Coluna_bg, 
            fg=TemaConfig.tema.texto, 
    
        )

        self.grid(row=0, column=i, sticky="nsew", padx=flt.padxColuna, pady=flt.padyItem)
        flt.listColunas.append(self)

class FrameListItemCell(tk.Label):

    def __init__(self, master, frm_List: FrameList, index, item):
       
        super().__init__(master, text=item, width=20)    

        self.config(fg=TemaConfig.tema.texto)

        self.grid(row=0, column=index, sticky="nsew", pady=frm_List.padyItem)

        self.bind("<Button-1>", lambda event: frm_List._SelectItem(event))

# ----------------------- ComboBox ---------------------------------------

class ComboBox(tk.Frame):

    def __init__(self, master): 

        super().__init__(master)
        self.winfo_toplevel().bind("<FocusOut>", self.__FocusOut_Janela)
        self.winfo_toplevel().bind("<Configure>", self.__Configure_Janela)
        self.tema = TemaConfig.tema
        self.list_Items: List[ComboBoxItem] = []
        self.item_bg = TemaConfig.tema.primario
        self.item_height = 20
        self.frm_btn_bg = TemaConfig.tema.borda
        self.frm_Items_high = 1
        self.btn_Seta_bg = TemaConfig.tema.primario
        self.ent_Box_bg = TemaConfig.tema.primario
        self.frm_Items_bg = TemaConfig.tema.primario
        self.listItemsAberta = False
        self.itemAtual: ComboBoxItem = None
       
        self.ent_Box = tk.Entry(

            self,
            bg=TemaConfig.tema.primario,
            fg=TemaConfig.tema.hover,
            relief="flat",
            highlightthickness=1,
            highlightbackground=TemaConfig.tema.primario,
            highlightcolor=TemaConfig.tema.destaque,
            readonlybackground=TemaConfig.tema.primario

        )

        self.ent_Box.bind("<Enter>", lambda event: self.__Enter_ent_Box(event))
        self.ent_Box.bind("<FocusIn>", lambda event: self.__Enter_ent_Box(event))
        self.ent_Box.bind("<Leave>", lambda event: self.__Leave_ent_Box(event))
        self.ent_Box.bind("<FocusOut>", lambda event: self.__Leave_ent_Box(event))
        self.ent_Box.pack(side="left", fill="x", expand=True, padx=0, pady=0)

        self.frm_Separador = tk.Frame(

            self,
            bg=TemaConfig.tema.destaque,
            width=2

        )

        self.frm_Separador.pack(side="left", fill="y", expand=True)

        self.frm_btn = tk.Frame(self, bg=self.frm_btn_bg, width=20)
        self.frm_btn.pack_propagate(False)
        self.frm_btn.pack(side="right", fill="both", expand=True)

        self.btn_Seta = tk.Button(

            self.frm_btn, 
            text=" < ", 
            bg=self.btn_Seta_bg, 
            fg=TemaConfig.tema.texto,
            relief="flat",
            bd=0,
            width=1,
            activebackground=TemaConfig.tema.hover,
            activeforeground=TemaConfig.tema.destaque,
            command=self.__Alterna_F_ListItems,

        )

        self.btn_Seta.pack(fill="both", expand=True, padx=2, pady=2)

        self.btn_Seta.bind("<Enter>", lambda event: self.__Enter_btn_Seta(event))
        self.btn_Seta.bind("<FocusIn>", lambda event: self.__Enter_btn_Seta(event))
        self.btn_Seta.bind("<Leave>", lambda event: self.__Leave_btn_Seta(event))
        self.btn_Seta.bind("<FocusOut>", lambda event: self.__Leave_btn_Seta(event))

        # F_ListItems
        self.F_ListItems = tk.Toplevel(self.winfo_toplevel()) 
        self.F_ListItems.overrideredirect(True)
        self.F_ListItems.config(bg=self.frm_Items_bg)
        self.F_ListItems.withdraw() 

        # Canvas
        self.canvas = tk.Canvas(self.F_ListItems, bg=self.item_bg, highlightthickness=0)

        # frm_Scrollbar
        self.frm_Scrollbar = tk.Frame(self.F_ListItems, width=1, bg=self.frm_Items_bg)
        self.frm_Scrollbar.pack(side="right", fill="y")

        # scrollbar
        self.scrollbar = tk.Scrollbar(self.frm_Scrollbar, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")
        self.scrollbar.config(command=self.canvas.yview)

        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

        
        self.frm_Items = tk.Frame(self.canvas, bg=self.frm_Items_bg, highlightthickness=self.frm_Items_high, highlightbackground=TemaConfig.tema.destaque)
        self.frm_Items.bind("<Configure>", lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas_window = self.canvas.create_window((0, 0), window=self.frm_Items, anchor="nw")
        self.canvas.bind("<Configure>", lambda event: self.canvas.itemconfigure(self.canvas_window, width=event.width))

    # ------------------------- metodos internos -------------------------------------------
    
    def __Configure_Janela(self, event):

        if not self.listItemsAberta: return

        self.__Atualizar_F_ListItems()

    def __FocusOut_Janela(self, event):

        if self.listItemsAberta:

            self.__Fechar_F_ListItems()

    def __Enter_btn_Seta(self, event):

        self.btn_Seta.config(bg=TemaConfig.tema.hover)

    def __Leave_btn_Seta(self, event):

        if self.btn_Seta.winfo_toplevel().focus_get() == self.btn_Seta: return  
        
        self.btn_Seta.config(bg=self.btn_Seta_bg)

    def __Enter_ent_Box(self, event):

        self.ent_Box.config(bg=TemaConfig.tema.hover, fg=TemaConfig.tema.texto)

    def __Leave_ent_Box(self, event):

        if self.focus_get() == self.ent_Box: return

        self.ent_Box.config(bg=self.ent_Box_bg, fg=TemaConfig.tema.hover)

    def __Atualizar_F_ListItems(self):

        if self.F_ListItems.winfo_exists():

            self.update_idletasks()
            x = self.winfo_rootx()
            y = self.winfo_rooty() + self.winfo_height()
            largura = self.winfo_width()

            if ((num := len(self.list_Items)) <=4):

                altura = num * self.item_height + (self.frm_Items_high * 2)

            else:

                altura = 4 * self.item_height + (self.frm_Items_high * 2)
            
            self.F_ListItems.geometry(f"{largura}x{altura}+{x}+{y}")
            self.canvas.itemconfigure(self.canvas_window, width=largura)

    def __Alterna_F_ListItems(self):

        if self.listItemsAberta:

            self.__Fechar_F_ListItems()

        else:

            self.__Abrir_F_ListItems()

    def __Abrir_F_ListItems(self):

        if not self.list_Items: return

        self.frm_btn.config(bg=TemaConfig.tema.destaque)
        self.btn_Seta.config(text=" > ")
        
        self.listItemsAberta = True

        self.__Atualizar_F_ListItems()

        if len(self.list_Items) > 4:

            self.scrollbar.pack(side="right", fill="y")
            self.frm_Scrollbar.pack_propagate(True)

        else:

            self.scrollbar.pack_forget()
            self.frm_Scrollbar.pack_propagate(False)
            self.frm_Scrollbar.config(width=1)
           
        self.canvas.pack(side="left", fill="both", expand=True)
        self.F_ListItems.deiconify()
        self.F_ListItems.lift()
        # self.F_ListItems.focus_set()

    def _SelectItem(self, item: "ComboBoxItem", event):

        if self.itemAtual != item:

            self.itemAtual = item

        ent_mode = self.ent_Box.cget("state") 

        self.ent_Box.config(state="normal")
        self.ent_Box.delete(0, tk.END)
        self.ent_Box.insert(0, item.viewValue)
        self.ent_Box.config(state=ent_mode)

        self.__Fechar_F_ListItems()

        self.OnSelectItem()

    def __Fechar_F_ListItems(self, event=None):

        self.frm_btn.config(bg=self.frm_btn_bg)
        self.btn_Seta.config(text=" < ")

        if self.F_ListItems.winfo_exists():

            self.F_ListItems.withdraw()

        self.listItemsAberta = False

    # --------------------------------------------------------------------------------------

    # ---------------------- metodos Externos -----------------------------------------------

    def AddItem(self, items: dict):

        mode = self.ent_Box.cget("state") 
        self.ent_Box.config(state="normal")

        for key, value in items.items():

            cbb = ComboBoxItem(self.frm_Items, self, value, key)
            self.list_Items.append(cbb)
            
        if self.list_Items and not self.ent_Box.get():

            self.ent_Box.insert(0, self.list_Items[0].viewValue)
            
        if not self.itemAtual:

            self.itemAtual = self.list_Items[0]

        self.ent_Box.config(state=mode)

        self.__Atualizar_F_ListItems()

    def RemoveItem(self, itemId: int):

        if itemId < 0 or itemId >= len(self.list_Items): raise TypeError("indice não existi")

        self.list_Items.remove(itemId)

    def GetItem(self, item: str):

        items = [i for i in self.list_Items if i.viewValue == item]

        return items[0]

    # -----------------------------------------------------------------------------

    def OnSelectItem(self):

        pass

class ComboBoxItem(tk.Frame):

    def __init__(self, master, cbb: ComboBox, value, viewValue):

        super().__init__(master)

        self.cbb = cbb
        self.config(height=cbb.item_height)
        self.pack_propagate(False)
        self.pack(side="top", fill="x")
        self.value: str = value
        self.viewValue: str = viewValue

        self.lb_Item = tk.Label(

            self,
            bg=self.cbb.item_bg,
            text=viewValue,
            anchor="w",
            fg=TemaConfig.tema.texto,
            padx=10

        )

        self.lb_Item.pack(fill="both", expand=True)
        
        self.lb_Item.bind("<Enter>", lambda event, lb=self.lb_Item: lb.config(bg=TemaConfig.tema.hover))
        self.lb_Item.bind("<Leave>", lambda event, lb=self.lb_Item: lb.config(bg=self.cbb.item_bg))
        self.lb_Item.bind("<Button-1>", lambda event, item=self: self.cbb._SelectItem(item,event))