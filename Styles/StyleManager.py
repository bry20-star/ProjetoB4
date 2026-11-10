
# importações

from Styles.Tema import Config

#-------------- StyleManager ------------------------------------------------------/

class StyleManager():

    __componentes = []

    @classmethod
    def Registra(cls, comp, met):

        for item in cls.__componentes:

            if item["comp"] == comp: return

        cls.__componentes.append({"comp": comp, "metodo": met})
        
        comp.bind("<Destroy>", lambda event, c=comp: cls.Remove(c))

    @classmethod
    def Remove(cls, comp):

        cls.__componentes = [   
            
            item for item in cls.__componentes 
            if item["comp"] != comp
        ]

    @classmethod
    def AtualizarTema(cls, tema):
       
        Config.SetTema(tema) 

        cls.__componentes = [c for c in cls.__componentes if c["comp"].winfo_exists()]

        for item in cls.__componentes:

            c = item["comp"]
            m = item["metodo"]
            
            m(c)

#-----------------------------------------------------------------\

