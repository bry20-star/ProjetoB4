class Usuario:
    
    conta: str 
    nivel: int
    nome: str

class Tabelas:

    class Usuario:

        tabela = "tb_Usuarios"
        n_Id = "n_IdUsuario"
        t_Conta = "t_ContaUsuario"
        t_Nome = "t_NameUsuario"
        n_Nivel = "n_Nivel"
        t_Senha = "t_SenhaUsuario"
            
    class Hospede:

        tabela = "tb_Hospedes"
        n_Id = "n_IdHospede"
        t_Conta = "t_NameHospede"
        t_Nome = "t_NameHospede"
        t_TipoCobranca = "t_TipoCobranca"
        n_IdQuarto = "n_IdQuarto"