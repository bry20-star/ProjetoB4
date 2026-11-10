
# importações 

from typing import List
import tkinter as tk
from Styles.Tema import Config

#-------------------------------- FrameList --------------------------------------------------------------------------------------/

class FrameList(tk.Frame):

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

        self.linhaAtual.config(bg=Config.tema.destaque)

        self.canvas.update_idletasks()

        self.OnSelectItem(event)

    #--------------------------------------------------\

    #-------------------------- metodos externos -------------------------------/

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

        return frm_linha

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

    #----------------------------------------------------------------------\

#---------------------------------------------------------------------------------------------\

#------------------------------------- FrameListItem -----------------------------------------------/

class FrameListItem(tk.Frame):

    def __init__(self, master, flt: FrameList,*items):

        super().__init__(master)

        self.list_cells: list[FrameListItemCell] = []
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

    #----------------------------------------------------------------\

#----------------------------------------------------------------------------------\

#------------------------------ FrameListCollum --------------------------------------------/

class FrameListCollum(tk.Label):

    def __init__(self, flt: FrameList, txt, i):
        
        super().__init__(flt.frm_Coluna, text=txt, width=20)

        self.peso = 1

        self.config(

            bg=flt.lb_Coluna_bg, 
            fg=Config.tema.texto, 
    
        )

        self.grid(row=0, column=i, sticky="nsew", padx=flt.padxColuna, pady=flt.padyItem)
        flt.listColunas.append(self)

#--------------------------------------------------------------------------\

#------------------------------- FrameListItemCell ------------------------------------------/

class FrameListItemCell(tk.Label):

    def __init__(self, master, frm_List: FrameList, index, item):
       
        super().__init__(master, text=item, width=20)    

        self.config(fg=Config.tema.texto)

        self.grid(row=0, column=index, sticky="nsew", pady=frm_List.padyItem)

        self.bind("<Button-1>", lambda event: frm_List._SelectItem(event))

#-------------------------------------------------------------------------------------\

#----------------------------------------------- ComboBox --------------------------------------------------------------/

class ComboBox(tk.Frame):

    def __init__(self, master): 

        super().__init__(master)
        
        # Combo Box

        self.winfo_toplevel().bind("<Button-1>", self.__Click_Janela, add="+")
        self.winfo_toplevel().bind("<FocusOut>", self.__FocusOut_Janela, add="+")
        self.winfo_toplevel().bind("<Configure>", self.__Configure_Janela, add="+")

        self.tema = Config.tema
        self.list_Items: List[ComboBoxItem] = []
        self.item_bg = Config.tema.primario
        self.item_height = 20
        self.frm_btn_bg = Config.tema.borda
        self.frm_Items_high = 1
        self.btn_Seta_bg = Config.tema.primario
        self.ent_Box_bg = Config.tema.primario
        self.frm_Items_bg = Config.tema.primario
        self.listItemsAberta = False
        self.itemAtual: ComboBoxItem = None
        self.buscar = ""
       
        self.ent_Box = tk.Entry(

            self,
            bg=Config.tema.primario,
            fg=Config.tema.hover,
            relief="flat",
            highlightthickness=1,
            highlightbackground=Config.tema.primario,
            highlightcolor=Config.tema.destaque,
            readonlybackground=Config.tema.primario

        )

        self.ent_Box.bind("<Enter>", lambda event: self.__Enter_ent_Box(event))
        self.ent_Box.bind("<FocusIn>", lambda event: self.__Enter_ent_Box(event))
        self.ent_Box.bind("<Leave>", lambda event: self.__Leave_ent_Box("mouse",event))
        self.ent_Box.bind("<FocusOut>", lambda event: self.__Leave_ent_Box("tab", event))
        self.ent_Box.bind("<KeyRelease>", lambda event: self.__KeyRelease_ent_Box(event))
        self.ent_Box.pack(side="left", fill="x", expand=True, padx=0, pady=0)
        
        self.frm_Separador = tk.Frame(

            self,
            bg=Config.tema.destaque,
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
            fg=Config.tema.texto,
            relief="flat",
            bd=0,
            width=1,
            activebackground=Config.tema.hover,
            activeforeground=Config.tema.destaque,
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
        self.canvas.bind("<Enter>", lambda event: self.canvas.bind_all("<MouseWheel>", lambda event: self.__MouseWheel_Canvas(event)))
        self.canvas.bind("<Leave>", lambda event: self.canvas.unbind_all("<MouseWheel>"))

        # frame items

        self.frm_Items = tk.Frame(self.canvas, bg=self.frm_Items_bg, highlightthickness=self.frm_Items_high, highlightbackground=Config.tema.destaque)
        self.frm_Items.bind("<Configure>", lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas_window = self.canvas.create_window((0, 0), window=self.frm_Items, anchor="nw")
        self.canvas.bind("<Configure>", lambda event: self.canvas.itemconfigure(self.canvas_window, width=event.width))

    #------------------------- metodos internos -------------------------------------------/
    
    def __KeyRelease_ent_Box(self, event):

        if self.ent_Box.cget("state") == "readonly": return

        self.buscar = self.ent_Box.get().replace(" ", "").lower()

        if not self.listItemsAberta:

            self.__Abrir_F_ListItems()
        
        for item in self.list_Items:

            item.pack_forget()

        if not self.ent_Box.get():

            for item in self.list_Items:

                item.pack(side="top", fill="x", expand=True)
                
            self.__Fechar_F_ListItems()

        for item in self.list_Items:

            item.pack(side="top", fill="x", expand=True)

            if not self.buscar in item.viewValue.replace(" ","").lower():

                item.pack_forget()

    def __Click_Janela(self, event):

        if not self.listItemsAberta: return

        self.__Fechar_F_ListItems()

    def __MouseWheel_Canvas(self, event):

        self.canvas.yview_scroll(int(-1 * (event.delta / 120)) * 4, "units")

    def __Configure_Janela(self, event):

        if not self.listItemsAberta: return

        self.__Atualizar_F_ListItems()
        pass

    def __FocusOut_Janela(self, event):

        if self.listItemsAberta:

            self.__Fechar_F_ListItems()

    def __Enter_btn_Seta(self, event):

        self.btn_Seta.config(bg=Config.tema.hover)

    def __Leave_btn_Seta(self, event):

        if self.btn_Seta.winfo_toplevel().focus_get() == self.btn_Seta: return  
        
        self.btn_Seta.config(bg=self.btn_Seta_bg)

    def __Enter_ent_Box(self, event):

        self.ent_Box.config(bg=Config.tema.hover, fg=Config.tema.texto)

    def __Leave_ent_Box(self, entrada:str , event):

        if self.focus_get() == self.ent_Box: return

        self.ent_Box.config(bg=self.ent_Box_bg, fg=Config.tema.hover)

        if self.ent_Box.cget("state") != "normal" or not self.buscar: return

        if entrada == "mouse": return

        for item in self.list_Items:

            if self.buscar in item.viewValue.replace(" ", "").lower():

                self.ent_Box.delete(0, tk.END)
                self.ent_Box.insert(0, item.viewValue)
                self.itemAtual = item
                break
       
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

        self.frm_btn.config(bg=Config.tema.destaque)
        self.btn_Seta.config(text=" > ")
        
        self.listItemsAberta = True

        self.__Atualizar_F_ListItems()
           
        self.canvas.pack(side="left", fill="both", expand=True)
        self.F_ListItems.deiconify()
        self.F_ListItems.lift()

    def _SelectItem(self, item: "ComboBoxItem", event):

        if self.itemAtual != item:

            self.itemAtual = item

        ent_mode = self.ent_Box.cget("state") 

        self.ent_Box.config(state="normal")
        self.ent_Box.delete(0, tk.END)
        self.ent_Box.insert(0, item.viewValue)
        self.ent_Box.config(state=ent_mode)

        self.__Fechar_F_ListItems()

        self.OnSelectItem(event)

    def __Fechar_F_ListItems(self, event=None):

        self.frm_btn.config(bg=self.frm_btn_bg)
        self.btn_Seta.config(text=" < ")

        if self.F_ListItems.winfo_exists():

            self.F_ListItems.withdraw()

        self.listItemsAberta = False

    # --------------------------------------------------------------------------------------\

    #----------------------- metodos Externos ---------------------------------------------------------------/

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

    def SetItem(self, value: str):

        items = [i for i in self.list_Items if i.viewValue == value]

        if not items[0]: return

        modo = self.ent_Box.cget("state")
        self.ent_Box.config(state="normal")

        self.itemAtual = items[0]
        self.ent_Box.delete(0, tk.END)
        self.ent_Box.insert(0, value)

        self.ent_Box.config(state=modo)

    # -----------------------------------------------------------------------------\

    #----------------- Metodso pra sobre escrever ---------------------------/

    def OnSelectItem(self, event):

        pass

    #------------------------------------\

#-------------------------------------------------------------------------------------------------\

#------------------------------------------ ComboxItem --------------------------------------------------------------------------/

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
            fg=Config.tema.texto,
            padx=10

        )

        self.lb_Item.pack(fill="both", expand=True)
        
        self.lb_Item.bind("<Enter>", lambda event, lb=self.lb_Item: lb.config(bg=Config.tema.hover))
        self.lb_Item.bind("<Leave>", lambda event, lb=self.lb_Item: lb.config(bg=self.cbb.item_bg))
        self.lb_Item.bind("<Button-1>", lambda event, item=self: self.cbb._SelectItem(item,event))

#-------------------------------------------------------------------------------------------------------\

#------------------------- TextBoxMask ----------------------------------------------------------------------------------/

class TextBoxMask(tk.Entry):

    def __init__(self):

        super().__init__(self)

#---------------------------------------------------------------------------------------------\

#-------------------------------------- NumericUpDown -------------------------------------------------------------------/ 

class NumericUpDown(tk.Frame):

    def __init__(self, master):
            
        super().__init__(master)

        # NumericUpDown

        self._valueMin = 0
        self._valueMax = 100
        self.valueUp = 1
        self.valueDown = 1
        self._value = self._valueMin
        self.press_btn = None

        # entry box
        
        ent_verif = self.winfo_toplevel().register(self.__Verif_ent_box)

        self.ent_box = tk.Entry(
            
            self,
            validate="key",
            validatecommand= (ent_verif, "%P")
            
        )

        self.ent_box.insert(0, self._valueMin)

        self.ent_box.pack(side="left")

        # Frame Buttons
            
        self.frm_botoes = tk.Frame(self, width=20)
        self.frm_botoes.pack(side="right", fill="y")
        self.frm_botoes.pack_propagate(False)

        # Frame Up

        self.frm_Up = tk.Frame(self.frm_botoes)
        self.frm_Up.pack(side="top", fill="both", expand=True)
        self.frm_Up.pack_propagate(False)

        # Frame Down

        frm = self.frm_Down = tk.Frame(self.frm_botoes)
        frm.pack(side="bottom", fill="both", expand=True)
        frm.pack_propagate(False)
        
        # Button Up

        self.btn_Up = tk.Button(
        
            self.frm_Up,
            text="+"
           
        )

        self.btn_Up.bind("<ButtonPress-1>", self.__press_btn_Up)
        self.btn_Up.bind("<ButtonRelease-1>", self.__Release_btn_Up)

        self.btn_Up.pack(fill="both", expand=True)
       
        # Button Down

        self.btn_Down = tk.Button(
            
            self.frm_Down, 
            text="-"
            
        )

        self.btn_Down.bind("<ButtonPress-1>", self.__Press_btn_Down)
        self.btn_Down.bind("<ButtonRelease-1>", self.__Release_btn_Down)

        self.btn_Down.pack(fill="both", expand=True)
        
    #----------------------- Metodos internos ------------------------------------------------/

    def __Verif_ent_box(self, text):
        
        if not text: return True

        if text == "-" and self._valueMin < 0: return True

        try:

            value = int(text)
            self._value = value
            return value >= self._valueMin and value <= self._valueMax

        except ValueError:

            return False
            
    def __Click_btn_Up(self):

        ent = self.ent_box

        if not ent.get(): return

        if int(ent.get()) + self.valueUp > self._valueMax: return

        value = int(ent.get())
        
        ent.delete(0, tk.END)
        ent.insert(0, value + self.valueUp)

        self._value = value + self.valueUp

    def __press_btn_Up(self, event=None):

        self.__Click_btn_Up()

        self.press_btn = self.after(150, self.__press_btn_Up)

    def __Release_btn_Up(self, event=None):

        if self.press_btn:

            self.after_cancel(self.press_btn)
            self.press_btn = None

    def __Click_btn_Down(self):

        ent = self.ent_box

        if not ent.get(): return

        if int(ent.get()) - self.valueDown < self._valueMin: return

        value = int(ent.get())

        ent.delete(0, tk.END)
        ent.insert(0, value - self.valueDown)

        self._value = value - self.valueDown

    def __Press_btn_Down(self, event=None):

        self.__Click_btn_Down()

        self.press_btn = self.after(150, self.__Press_btn_Down)

    def __Release_btn_Down(self, event=None):

        if self.press_btn:

            self.after_cancel(self.press_btn)
            self.press_btn = None

    #----------------------------------------------------------------------------\

    #-------------------- metodos externos ---------------------------------------------------------/

    def SetValueMin(self, value):

        if value > self._valueMax: raise TypeError("Valor minimo não pode ser maior que o maximo")

        self._valueMin = value
        self._value = value
        self.ent_box.delete(0, tk.END)
        self.ent_box.insert(0, value)

    def SetValueMax(self, value):

        if value < self._valueMin: raise TypeError("Valor Máximo não pode ser menor que o valor minimo")

        self._valueMax = value

    def SetValue(self, value):

        if value > self._valueMax or value < self._valueMin: raise TypeError("Valor não pode ser maior o valor maximo ou menor que o valor minimo") 

        self._value = value
        self.ent_box.delete(0, tk.END)
        self.ent_box.insert(0, value)

    #-----------------------------------------------------------------------------------------\

#----------------------------------------------------------------------------------------------------------------\