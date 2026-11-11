
# importações

from Styles.Tema import Config
from Comps.CustomComps import FrameList
from Styles.StyleManager import StyleManager as sm

#----------------------- FrameListStyle -------------------------------------------------------------------------------------------------/

class FrameListStyle():
    
    tema = Config.tema

    #-------------- Zebrado -------------------------------------------------------------------------------------/

    @staticmethod
    def Zebrado(flt: FrameList):

        FrameList.tema = Config.tema
        tema = Config.tema

        sm.Registra(comp=flt, met=FrameListStyle.Zebrado)

        flt.config(bg=tema.primario)
        flt.frm_Conteudo.config(bg=tema.primario)
        flt.frm_Coluna.config(bg=tema.segundario)

        for colum in flt.listColunas:

            colum.config(

                bg=tema.primario, 
                fg=tema.texto,

            )

        for i,item in enumerate(flt.listLinhas):

            cor = tema.primario if i % 2 else tema.segundario

            item.config(bg=cor)
            
            item.bind("<Enter>", lambda event: item)

            for cell in item.list_cells:

                cell.config(bg=cor, fg=tema.texto)

    def __Enter_Item(self, event):

        if self["bg"] == self.tema.destaque: return



    #--------------------------------------------------------------------------------\

#-----------------------------------------------------------------------------------------------------------------------------\