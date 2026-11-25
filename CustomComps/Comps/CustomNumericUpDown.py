
# importações 

import tkinter as tk

#-------------------------------------- CustomNumericUpDown -------------------------------------------------------------------/ 

class CustomNumericUpDown(tk.Frame):

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