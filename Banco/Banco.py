from shlex import join
import sqlite3
import os

class Banco:

    nomeBanco = "bd_Sistema.db"
    caminho = os.path.dirname(os.path.abspath(__file__))
    caminhoBanco = os.path.join(caminho, nomeBanco)

    @staticmethod
    def __ConnectionBanco():

        return sqlite3.connect(Banco.caminhoBanco)

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
