
#------------------ Tabelas --------------------------------------------------------------/

class Tabelas:

    #------------------- Usuario ---------------------------------------------------------------------------/

    class Usuario:

        # tabela

        tabela = "tb_Usuarios"

        # colunas

        n_Id = "n_IdUsuario"
        t_Conta = "t_ContaUsuario"
        t_Nome = "t_NameUsuario"
        n_Nivel = "n_Nivel"
        t_Senha = "t_SenhaUsuario"
            
    #---------------------------------------------------------------------\

    #--------------- Hospedes ----------------------------------------------------------/

    class Hospede:

        # tabela

        tabela = "tb_Hospedes"

        # culunas

        n_Id = "n_IdHospede"
        t_Conta = "t_NameHospede"
        t_Nome = "t_NameHospede"
        t_TipoCobranca = "t_TipoCobranca"
        n_IdQuarto = "n_IdQuarto"

        #----------------- Valores -----------------/

        # Tipo Conbrança

        diaria = {
            
            "view":"Diaria",
            "value":"D"
            
        }

        mensal = {
        
            "view":"Mensal",
            "value":"M"
            
        }

        anual = {
            
            "view":"Anual",
            "value":"A"
        }

        #----------------------------------\

    #----------------------------------------------------\

    #------------------- quartos ----------------------------------/

    class Quarto:

        # tabela 

        tabela = "tb_Quartos"

        # Colunas

        n_Id = "n_IdQuarto"
        t_Nome = "t_NameQuarto"
        t_Estado = "t_EstadoQuarto"
        t_Tipo = "t_TipoQuarto"
        n_Cap = "n_CapQuarto"

        #----------- valores --------------------/

        # Tipo

        standard = {
            
            "view":"Standard", 
            "value":"D"
            
        }

        luxo = {
            
            "view":"Luxo",
            "value":"O"
            
        }

        suite = {
            
            "view":"Suíte", 
            "value":"E"
            
        }

        # status

        disponivel = {
            
            "view":"Disponível", 
            "value":"D"
            
        }

        oculpado = {
            
            "view":"Oculpado",
            "value":"O"
            
        }

        bloqueado = {
            
            "view":"Bloqueado", 
            "value":"B"
            
        }

        #----------------------------\

    #---------------------------------------------------\

#-------------------------------------------------------------------------------------\