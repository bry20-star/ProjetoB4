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
        
        # scrollbar
        self.scrollbar = tk.Scrollbar(self, orient="vertical")
        self.scrollbar.config(activebackground=TemaConfig.tema.destaque)
        self.scrollbar.pack(side="right", fill="y")

        # frame coluna
        self.frm_Coluna = tk.Frame(self)
        self.frm_Coluna.config(bg=TemaConfig.tema.segundario)
        self.frm_Coluna.pack(side="top", fill="x")

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

# ----------------------- ComboBox ---------------------------------------

class ComboBox(tk.Frame):

    def __init__(self, master): 

        super().__init__(master)
        self.tema = TemaConfig.tema
        self.list_Items: List[ComboBoxItem] = []
        self.item_bg = TemaConfig.tema.primario
        self.item_height = 20
        self.frm_btn_bg = TemaConfig.tema.borda
        self.btn_Seta_bg = TemaConfig.tema.primario
        self.ent_Box_bg = TemaConfig.tema.primario
        self.frm_Items_bg = TemaConfig.tema.primario
        self.listItemsAberta = False
        self.itemAtual: ComboBoxItem = None

        self.__Criar_F_ListItems()

        self.ent_Box = tk.Entry(

            self, 
            bg=TemaConfig.tema.primario, 
            fg=TemaConfig.tema.texto, 
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

    # ------------------------- metodos internos -------------------------------------------

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

    def __Criar_F_ListItems(self):

        self.F_ListItems = tk.Toplevel(self.winfo_toplevel()) 
        self.F_ListItems.overrideredirect(True)
        self.F_ListItems.config(bg=self.frm_Items_bg)
        self.F_ListItems.withdraw() 

        self.F_ListItems.bind("<FocusOut>", lambda event: self.__Fechar_F_ListItems(event))

        self.canvas = tk.Canvas(self.F_ListItems, bg=self.frm_Items_bg, highlightthickness=0)

        # self.scrollbar = tk.Scrollbar(self.F_ListItems, orient="vertical")
        # self.scrollbar.pack(side="right", fill="y")

        # self.canvas.config(yscrollcommand=self.scrollbar.set)

        # self.scrollbar.config(command=self.canvas.yview)
        
        self.frm_Items = tk.Frame(self.canvas, bg=self.frm_Items_bg)
        self.frm_Items.bind("<Configure>", lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas_window = self.canvas.create_window((0, 0), window=self.frm_Items, anchor="nw")
        self.canvas.bind("<Configure>", lambda event: self.canvas.itemconfigure(self.canvas_window, width=event.width))


    def __Atualizar_F_ListItems(self):

        if hasattr(self, 'F_ListItems') and self.F_ListItems.winfo_exists():

            self.update_idletasks()
            x = self.winfo_rootx()
            y = self.winfo_rooty() + self.winfo_height()
            largura = self.winfo_width()
            
            num_itens = len(self.list_Items)
            altura_calculada = min(num_itens, 6) * self.item_height
            
            self.F_ListItems.geometry(f"{largura}x{altura_calculada}+{x}+{y}")
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

        if not hasattr(self, 'F_ListItems') or not self.F_ListItems.winfo_exists():

             guardados = [item.lb_Item.cget("text") for item in self.list_Items]
             self.list_Items.clear()
             self.__Criar_F_ListItems()
             self.AddItem(*guardados)

        self.listItemsAberta = True

        self.__Atualizar_F_ListItems()

        # if len(self.list_Items) > 5:

        #     self.scrollbar.pack(side="right", fill="y")

        # else:

        #    # self.scrollbar.pack_forget()
        #    pass

        self.canvas.pack(side="left", fill="both", expand=True)
        self.F_ListItems.deiconify()
        self.F_ListItems.lift()
        self.F_ListItems.focus_set()

    def __SelectItem(self, item: "ComboBoxItem" = None):

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

        if hasattr(self, 'F_ListItems') and self.F_ListItems.winfo_exists():

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

        if itemId < 0 or itemId >= len(self.list_Items):

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
        self.lb_Item.bind("<Button-1>", lambda event, item=self: self.cbb._ComboBox__SelectItem(item))