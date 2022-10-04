import sqlite3
from abc import ABC, abstractmethod 
import re
from datetime import date
import time
from time import sleep
import sys
import datetime
import random

conexao = sqlite3.connect ("biblioteca.maria.db")
cursor = conexao.cursor ()

cursor.execute ("SELECT * FROM cadastro")
for linha in cursor.fetchall ():
    print (linha)

# cursor.execute ("DELETE FROM cadastro")
# conexao.commit ()
# cursor.execute ("DELETE FROM livros_na_estante")
# conexao.commit ()

def escrever (texto):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush ()
        time.sleep (0.04)

class Pessoa:
    def __init__ (self, nome) -> None:
        self.nome = nome

    def dataNascimento (self, idade):
        today = date.today() 
        age = today.year - idade.year - ((today.month, today.day) < (idade.month, idade.day))
        return age

    def calculadora (self, data):
        data = str (data)
        data = re.sub (r"[^0-9]","", data)
        listaData = list (data)
        dia = int (f"{listaData.pop(0)}{listaData.pop(0)}")
        mes = int (f"{listaData.pop(0)}{listaData.pop(0)}")
        ano = int (f"{listaData.pop(0)}{listaData.pop(0)}{listaData.pop(0)}{listaData.pop(0)}")
        idade = self.dataNascimento (date (ano, mes, dia))
        return idade

    def data_Completa (self,data):
        datalist=[]
        for i in data:
            datalist.append(i)
        for i in range(len(datalist)):
            if i == 2:
                datalist[2]='/'+ datalist[2]
            if i == 4:
                datalist[4]='/'+ datalist[4]
        data = ''.join(datalist)
        return data

class Cliente (Pessoa):
    def __init__ (self, nome, dataCompleta, email, senha) -> None:
        super().__init__ (nome)
        self.dataCompleta = dataCompleta
        self.idade = self.calculadora (self.dataCompleta)
        self.data = self.data_Completa (dataCompleta)
        self.matricula = self.matriculaFunc ()
        self.email = email
        self.senha = senha

    def matriculaFunc (self):
        ano = datetime.date.today().strftime('%Y')
        cont = random.randint(0000, 9999)
        matricula = f"{ano}.{cont}"
        return matricula

class Livro:
    def __init__(self, titulo, autor, quantidade, genero, faixa_etaria, npaginas, data_de_edicao) -> None:
        self.titulo = titulo
        self.autor = autor
        self.quantidade = quantidade
        self.genero = genero
        self.faixa_etaria = faixa_etaria
        self.npaginas = npaginas
        self.data_de_edicao = data_de_edicao

class Biblioteca:
    def __init__(self) -> None:
        self.membro = ''
        self.livros = []

    def inserirCliente (self, nome, dataCompleta, email, senha):
        self.membro = (Cliente (nome, dataCompleta, email, senha))
        cursor.execute (f"INSERT INTO cadastro (nome, data_de_aniversario, matricula, email, senha) VALUES (?, ?, ?, ?, ?)", (nome, self.membro.idade, self.membro.matricula, email, senha))
        conexao.commit ()
        print (f"Membro: {self.membro.nome} \nData de nascimento: {self.membro.data} \nIdade: {self.membro.idade} \nMatrícula: {self.membro.matricula} \nE-mail: {self.membro.email} \nSenha: {len (self.membro.senha) * '*'}")

    def loginCliente (self):
        matricula_login = input ("Matrícula: \n")
        senha_login = input ("Senha: \n")
        cursor.execute (f"SELECT matricula FROM cadastro WHERE matricula = '{matricula_login}'")
        listaMatricula = []
        for matricula_for in cursor.fetchall():
            listaMatricula = matricula_for[0]
        cursor.execute (f"SELECT senha FROM cadastro WHERE senha = '{senha_login}'")
        for senha_for in cursor.fetchall():
            pass
        
        while True:
            if matricula_login in listaMatricula and senha_login in senha_for:
                break
            else:
                print ("Matrícula ou senha incorretas.")
                self.loginCliente()
            
    def recuperarSenha (self):
        matricula_esqueceu = input ("Digite sua matrícula: \n")
        email_esqueceu = input ("Digite seu e-mail: \n")

        cursor.execute (f"SELECT matricula FROM cadastro WHERE matricula = '{matricula_esqueceu}'")
        for matricula_for in cursor.fetchall():
            pass

        cursor.execute (f"SELECT email FROM cadastro WHERE email = '{email_esqueceu}'")
        for email_for in cursor.fetchall():
            pass
                                    
        if matricula_esqueceu in matricula_for and email_esqueceu in email_for:
            cursor.execute (f"SELECT senha FROM cadastro WHERE senha = '{matricula_esqueceu}'")
            for i in cursor.fetchall():
                print (i)

        else:
            print ("Não deu bom")

    def inserirLivros (self, titulo, autor, quantidade_disponivel, genero, faixa_etaria, npaginas, data_de_edicao):
        self.livros.append (Livro (titulo, autor, quantidade_disponivel, genero, faixa_etaria, npaginas, data_de_edicao))
        cursor.execute (f"INSERT INTO livros_na_estante (titulo, autor, quantidade_disponivel, genero, faixa_etaria, npaginas, data_de_edicao) VALUES (?, ?, ?, ?, ?, ?, ?)", (titulo, autor, quantidade_disponivel, genero, faixa_etaria, npaginas, data_de_edicao))
        conexao.commit ()
    def printarLivros (self):
        cursor.execute (f"SELECT * FROM livros_na_estante WHERE quantidade_disponivel > 0")
        print ("Livros disponíveis:")
        print()
        for i in cursor.fetchall():
            print (f"Livro: {i [1]}")
            print (f"Quantidade disponível: {i [3]}")
            print ()

    def emprestarLivro (self):

        livro_emprestado = input ("Que livro deseja emprestar? \n")
        cursor.execute (f"SELECT titulo, quantidade_disponivel,autor FROM livros_na_estante WHERE titulo = '{livro_emprestado}'")
        for i in cursor.fetchall():
            titulo, y, autor = i
            cursor.execute (f"UPDATE livros_na_estante SET quantidade_disponivel = ? WHERE titulo = '{titulo}' and autor = '{autor}'", (y-1,))
            conexao.commit ()
            matricula_verifica = input ("Digite sua matrícula novamente: \n")
            nomeVerifica = input ("Digite seu nome: \n")
            cursor.execute (f"SELECT matricula, nome FROM cadastro")
            for matricula_i in cursor.fetchall():
                if matricula_verifica in matricula_i and nomeVerifica in matricula_i:
                    cursor.execute (f"INSERT INTO livros_emprestados (matricula, cliente, titulo) VALUES (?,?,?)", (matricula_verifica, nomeVerifica.title(), livro_emprestado))
                    conexao.commit ()

        '''Verificação se tem livros para emrestar
        Se tiver: diminuir 1 de livro disponivel
        se nao: não é possivel emprestar'''

        '''Inserir na tabela de livros emprestados o cliente que pegou e o titulo do livro
        
        Depois fazer uma função para devolver o livro:
        deletando o livro da tabela livros emprestados com select e where matricula
        '''