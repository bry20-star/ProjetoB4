from typing import TYPE_CHECKING
from Styles.Tema import Tema
import tkinter as tk

if TYPE_CHECKING:

    from Componentes.ComponentesPersonalizados import FrameList, FrameListItems

class TemaConfig():

    idTema = 0
 
    tema = Tema.Dark

    @staticmethod
    def SetTema(i):

        TemaConfig.idTema = i

        if i== 0:

            TemaConfig.tema = Tema.Dark
        
        elif i == 1: 

            TemaConfig.tema = Tema.White

class Style():

    _componentes = []

    @staticmethod
    def ButtonFlat(comp: tk.Button):

        comp.config(
            
            bg=TemaConfig.tema.botao,
            fg=TemaConfig.tema.texto,
            activebackground=TemaConfig.tema.clicado,
            highlightthickness=0,
            activeforeground=TemaConfig.tema.destaque,
            relief="flat",
            bd=0,
            font=("Segoe UI",12),

        )

        comp.bind("<Enter>", lambda event: comp.config(bg=TemaConfig.tema.hover, highlightthickness=2))
        comp.bind("<FocusIn>", lambda event: comp.config(bg=TemaConfig.tema.hover, highlightthickness=2))
        comp.bind("<Leave>", lambda event: comp.config(bg=TemaConfig.tema.botao, highlightthickness=0))
        comp.bind("<FocusOut>", lambda event: comp.config(bg=TemaConfig.tema.botao, highlightthickness=0))
    
        if any(item["comp"] == comp for item in Style._componentes): return

        Style._componentes.append({"comp": comp, "metodo": Style.ButtonFlat })

    @staticmethod
    def ButtonHide(comp: tk.Button):

        if not comp.master: return
        
        comp.config(
            
            bg=comp.master["bg"],
            fg=TemaConfig.tema.texto,
            activebackground=comp.master["bg"],
            activeforeground=TemaConfig.tema.destaque,
            highlightthickness=0,
            relief="flat",
            padx=0,
            pady=0,
            bd=0,
            font=("Segoe UI",12),

        )

        comp.bind("<Enter>", lambda event: comp.config(bg=comp.master["bg"], fg=TemaConfig.tema.hover, font=("Segoe UI",13)))
        comp.bind("<FocusIn>", lambda event: comp.config(bg=comp.master["bg"], fg=TemaConfig.tema.hover))
        comp.bind("<Leave>", lambda event: comp.config(bg=comp.master["bg"], fg=TemaConfig.tema.texto, font=("Segoe UI",12)))
        comp.bind("<FocusOut>", lambda event: comp.config(bg=comp.master["bg"], fg=TemaConfig.tema.texto))

        if any(item["comp"] == comp for item in Style._componentes): return

        Style._componentes.append({"comp": comp, "metodo": Style.ButtonHide })

    @staticmethod
    def FrameBord(comp: tk.Frame):

        comp.config(
            
            bg=TemaConfig.tema.segundario,
            highlightthickness=1,
            highlightbackground=TemaConfig.tema.primario,
            highlightcolor=TemaConfig.tema.primario
        )
        
        if any(item["comp"] == comp for item in Style._componentes): return

        Style._componentes.append({"comp": comp, "metodo": Style.FrameBord })

    @staticmethod
    def Frame(comp: tk.Frame):

        comp.config(
            
            bg=TemaConfig.tema.segundario,
       
        )
        
        if any(item["comp"] == comp for item in Style._componentes): return

        Style._componentes.append({"comp": comp, "metodo": Style.Frame })
    
    @staticmethod
    def EntryBord(comp: tk.Entry):

        comp.config(
            
            bg=TemaConfig.tema.primario,
            fg=TemaConfig.tema.hover,
            relief="flat",
            highlightthickness=1,
            highlightbackground=TemaConfig.tema.primario,
            highlightcolor=TemaConfig.tema.destaque

        )

        comp.insert(0, "Buscar:")

        comp.bind("<Enter>", lambda event: Style.__EntryEnter("mouse",event))
        comp.bind("<FocusIn>", lambda event: Style.__EntryEnter("tab",event))
        comp.bind("<Leave>", lambda event: Style.__EntryLeave("mouse",event))
        comp.bind("<FocusOut>", lambda event: Style.__EntryLeave("tab",event))

        if any(item["comp"] == comp for item in Style._componentes): return

        Style._componentes.append({"comp": comp, "metodo": Style.EntryBord })

    def __EntryEnter(entrada: str,event):

        comp:tk.Entry = event.widget

        if comp.get() == "Buscar:":

            comp.delete(0,tk.END)

        comp.config(bg=TemaConfig.tema.hover, fg=TemaConfig.tema.texto)

    def __EntryLeave(entrada: str,event):

        comp: tk.Entry = event.widget

        if entrada == "tab":

            comp.delete(0,tk.END)

        if comp.winfo_toplevel().focus_get() == comp: return

        if comp.get() == "":

            comp.insert(0, "Buscar:")

        comp.config(bg=TemaConfig.tema.primario, fg=TemaConfig.tema.hover)

    def LabeHide(lb: tk.Label):

        if not lb.master: return

        lb.config(

            bg=lb.master["bg"], 
            fg=TemaConfig.tema.texto
            
        )
        
        if any(item["comp"] == lb for item in Style._componentes): return

        Style._componentes.append({"comp": lb, "metodo": Style.LabeHide })

    def FrameListZebrado(comp: "FrameList"):

        comp.config(bg=TemaConfig.tema.primario)
        comp.frm_Conteudo.config(bg=TemaConfig.tema.primario)
        comp.frm_Coluna.config(bg=TemaConfig.tema.segundario)

        for colum in comp.listColunas:

            colum.config(

                bg=TemaConfig.tema.primario, 
                fg=TemaConfig.tema.texto,

            )

        for i,item in enumerate(comp.listLinhas):

            cor = TemaConfig.tema.primario if i % 2 else TemaConfig.tema.segundario

            item.config(bg=cor)

            for cell in item.list_cells:

                cell.config(bg=cor, fg=TemaConfig.tema.texto)

        if any(item["comp"] == comp for item in Style._componentes): return

        Style._componentes.append({"comp": comp, "metodo": Style.FrameListZebrado })
        
    @staticmethod
    def AtualizarTema(i):
       
        TemaConfig.SetTema(i)

        Style._componentes = [c for c in Style._componentes if c["comp"].winfo_exists()]

        for item in Style._componentes:

            c = item["comp"]
            m = item["metodo"]
            
            m(c)