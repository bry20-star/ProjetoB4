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
    def ButtonFlat(button: tk.Button):

        button.config(
            
            bg=TemaConfig.tema.botao,
            fg=TemaConfig.tema.texto,
            activebackground=TemaConfig.tema.hover,
            activeforeground=TemaConfig.tema.destaque,
            relief="flat",
            bd=0,
            font=("Segoe UI",12),

        )
    
        if any(item["comp"] == button for item in Style._componentes): return

        Style._componentes.append({"comp": button, "metodo": Style.ButtonFlat })
    
    @staticmethod
    def ButtonHide(button: tk.Button):

        if not button.master: return
        
        button.config(
            
            bg= button.master["bg"],
            fg=TemaConfig.tema.texto,
            activebackground=TemaConfig.tema.hover,
            activeforeground=TemaConfig.tema.destaque,
            relief="flat",
            bd=0,
            font=("Segoe UI",12),

        )

        if any(item["comp"] == button for item in Style._componentes): return

        Style._componentes.append({"comp": button, "metodo": Style.ButtonHide })

    @staticmethod
    def FrameBord(frame: tk.Frame):

        frame.config(
            
            bg=TemaConfig.tema.segundario,
            highlightthickness=1,
            highlightbackground=TemaConfig.tema.primario,
            highlightcolor=TemaConfig.tema.destaque
        )
        
        if any(item["comp"] == frame for item in Style._componentes): return

        Style._componentes.append({"comp": frame, "metodo": Style.FrameBord })

    @staticmethod
    def Frame(comp: tk.Frame):

        comp.config(
            
            bg=TemaConfig.tema.segundario,
       
        )
        
        if any(item["comp"] == comp for item in Style._componentes): return

        Style._componentes.append({"comp": comp, "metodo": Style.Frame })
    
    @staticmethod
    def EntryBord(ent: tk.Entry):

        ent.config(
            
            bg=TemaConfig.tema.segundario,
            fg=TemaConfig.tema.texto,
            relief="flat",
            highlightthickness=1,
            highlightbackground=TemaConfig.tema.primario,
            highlightcolor=TemaConfig.tema.destaque

        )

        if any(item["comp"] == ent for item in Style._componentes): return

        Style._componentes.append({"comp": ent, "metodo": Style.EntryBord })

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