
#------------ Tema ---------------------------------------------------------------------------------------------------/

class Tema:

    #----------- Dark ---------------------------------------------------------/

    class Dark:

        # cores
        primario = "#202123"
        segundario = "#2D2F33"
        texto = "#FFFFFF"
        hover = "#4C5057"
        destaque = "#0E639C"
        botao = "#3A3D42"

        click = "#1F4E79"     
        borda = "#3E4147"       

        fonte = ("Segoe UI",11)
        fonteTitulo = ("Segoe UI", 22, "bold")

    #------------------------------------------------------\

    #------------ White --------------------------------------------------/

    class White:

        primario = "#F7F7F8"    
        segundario = "#FFFFFF"    
        texto = "#202123"        
        hover = "#D8DBDF"        
        destaque = "#0E639C"     
        botao = "#E4E6E9"       

        click = "#D2E5F5"     
        borda = "#E2E4E7"       

        fonte = ("Segoe UI",11)
        fonteTitulo = ("Segoe UI", 22, "bold")

    #------------------------------------------------------\

#---------------------------------------------------------------------\

#--------------- Config ----------------------------------------------------------------/

class Config():
 
    tema = Tema.Dark

    #--------- SetTema ----------------------------------/

    @staticmethod
    def SetTema(tema):

        if tema == "dark":

            Config.tema = Tema.Dark
        
        elif tema == "white": 

            Config.tema = Tema.White

    #---------------------------------------\

#------------------------------------------------------------------------\