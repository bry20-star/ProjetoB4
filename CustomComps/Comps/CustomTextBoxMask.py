
# importações

import tkinter as tk

#------------------------- CustomTextBoxMask ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------/

class CustomTextBoxMask(tk.Entry):

    def __init__(self, master, mask="__/__/____"):

        super().__init__(master)

        # variaveis

        self.mask = mask
        self.SoLetras = False
        self.fixos = set(self.mask.replace("_", ""))

        # entry

        ent_verif = self.winfo_toplevel().register(self.__Verif_Entry)
        
        self.config(

            validate="key",
            validatecommand=(ent_verif, "%P", "%d")

        )

        self.insert(0, self.mask)
        self.bind("<KeyRelease>", self.__AplicarMask)
        self.bind("<FocusIn>", self.__posicionar_cursor, add="+")

    #---------------------------------- metodos internos -------------------------------------------------------------------------------------/

    def __Verif_Entry(self, txt, acao):

        if acao == "0" or not txt: return True

        digitados = [c for c in txt if c != "_" and c not in self.fixos]

        total_espacos = self.mask.count("_")

        if len(digitados) > total_espacos: return False


        if not self.SoLetras:

            if not all( c.isdigit() for c in digitados): return False

            # if digitados and not digitados[-1].isdigit(): return False


        else:

            if not all( c.isalpha() for c in digitados): return False
        
        return True

    def __AplicarMask(self, event):

        if event.keysym in ("Left", "Right", "Tab"): return

        atualTxt = self.get()

        digitados = [c for c in atualTxt if c != "_" and c not in self.fixos]
        
        novoTxt = ""
        idDig = 0

        for charMask in self.mask:

            if charMask == "_":

                if idDig < len(digitados):

                    novoTxt += digitados[idDig]
                    idDig += 1

                else:

                    novoTxt += "_"
            else:

                novoTxt += charMask

        if novoTxt != atualTxt:

            self.delete(0, tk.END)
            self.insert(0, novoTxt)
            self.__posicionar_cursor()

    def __posicionar_cursor(self, event=None):

        texto = self.get()

        if "_" in texto:

            pos = texto.index("_")
            self.icursor(pos)

        else:

            self.icursor(tk.END)

    #------------------------------------------------------------------------------------------------------------------\

    #-------------------------- metodos externos -----------------------------------------------------------------------------------------------------/

    def SetMask(self, mask: str):

        self.mask = mask
        self.fixos = set(mask.replace("_",""))
        self.delete(0, tk.END)
        self.insert(0, mask)

    #-----------------------------------------------------------------------------------------------------------------------------\