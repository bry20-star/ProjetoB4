import sqlite3
import os

class Banco:

    nomeBanco = "bd_Sistema.db"
    caminho = os.path.dirname(os.path.abspath(__file__))
    caminhoBanco = os.path.join(caminho, nomeBanco)

    @staticmethod
    def __ConnectionBanco():

        connect = sqlite3.connect(Banco.caminhoBanco)
        connect.row_factory = sqlite3.Row
        return connect

    @staticmethod
    def DML(query: str):
        
        with Banco.__ConnectionBanco() as conexao:

            curso = conexao.cursor()
            curso.execute(query)

    @staticmethod
    def DQL(query: str):

        with Banco.__ConnectionBanco() as conexao:

            curso = conexao.cursor()
            curso.execute(query)
            return curso.fetchall()

    @staticmethod
    def DeleteDado(dadoId: int, tabela: str, idKey: str):

        with Banco.__ConnectionBanco() as conexao:

            curso = conexao.cursor()
            curso.execute(f"DELETE FROM {tabela} WHERE {idKey} == {dadoId}")
            conexao.commit()

    @staticmethod
    def SetDado(dadoId: int, tabela: str, idKey:str, dados: dict):

        with Banco.__ConnectionBanco() as conexao:

            curso = conexao.cursor()
            
            listKeys = ", ".join([f"{key} = ?" for key in dados.keys()])

            cmd = f"UPDATE {tabela} SET {listKeys} WHERE {idKey} == ?"

            valores = list(dados.values()) + [dadoId]

            curso.execute(cmd, valores)
            conexao.commit()

    @staticmethod
    def GetDado(tabela: str, idKey: str = "", dadoÌd: int = -1, paramsKey: str = "", params: str = ""):

        with Banco.__ConnectionBanco() as conexao:

            curso = conexao.cursor()

            if idKey != "":

                cmd = f"SELECT * FROM {tabela} WHERE {idKey} = ?"
                valor = (dadoÌd,)

            elif paramsKey != "":

                cmd = f"SELECT * FROM {tabela} WHERE {paramsKey} = ?"
                valor = (params,)

            try:

                curso.execute(cmd, valor)
                return curso.fetchall()

            except:

                return None

    @staticmethod
    def AddDado(tabela: str, dados: dict):

        with  Banco.__ConnectionBanco() as conexao:

            listKeys = ", ".join(dados.keys())
            listValues = ", ".join(["?"] * len(dados.values()))

            curso = conexao.cursor()

            cmd = f"INSERT INTO {tabela} ({listKeys}) VALUES ({listValues})"

            curso.execute(cmd, tuple(dados.values()))

            conexao.commit()
                
            return curso.lastrowid
