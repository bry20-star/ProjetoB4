
# importações 

from typing import List
import tkinter as tk
from Styles.Tema import Config

#----------------------------------------------- CustomComboBox --------------------------------------------------------------/

class CustomComboBox(tk.Frame):

    def __init__(self, master): 

        super().__init__(master)
        
        # Combo Box

        self.winfo_toplevel().bind("<Button-1>", self.__Click_Janela, add="+")
        self.winfo_toplevel().bind("<FocusOut>", self.__FocusOut_Janela, add="+")
        self.winfo_toplevel().bind("<Configure>", self.__Configure_Janela, add="+")

        self.tema = Config.tema
        self.list_Items: List[CustomComboBoxItem] = []
        self.item_bg = Config.tema.primario
        self.item_height = 20
        self.frm_btn_bg = Config.tema.borda
        self.frm_Items_high = 1
        self.btn_Seta_bg = Config.tema.primario
        self.ent_Box_bg = Config.tema.primario
        self.frm_Items_bg = Config.tema.primario
        self.listItemsAberta = False
        self.itemAtual: CustomComboBoxItem = None
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

    def _SelectItem(self, item: "CustomComboBoxItem", event):

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

            cbb = CustomComboBoxItem(self.frm_Items, self, value, key)
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

#------------------------------------------ CustomComboBoxItem --------------------------------------------------------------------------/

class CustomComboBoxItem(tk.Frame):

    def __init__(self, master, cbb: CustomComboBox, value, viewValue):

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