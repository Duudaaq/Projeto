import sqlite3
from abc import ABC, abstractmethod 
import re
from datetime import date
import time
from time import sleep
import sys
import datetime
import random

conexao = sqlite3.connect ("biblioteca.db")
cursor = conexao.cursor ()

cursor.execute ("SELECT * FROM cadastro")
for linha in cursor.fetchall ():
    print (linha)

# cursor.execute ("DELETE FROM cadastro")
# conexao.commit ()
# cursor.execute ("DELETE FROM conta")
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
        # dataCompleta = (f"{dia}/{mes}/{ano}")
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
    def __init__ (self, nome, dataCompleta, email, senha, palavra_chave) -> None:
        super().__init__ (nome)
        self.dataCompleta = dataCompleta
        self.idade = self.calculadora (self.dataCompleta)
        # self.data = data
        self.data = self.data_Completa (dataCompleta)
        self.matricula = self.matriculaFunc ()
        self.email = email
        self.senha = senha
        self.palavra_chave = palavra_chave

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

    def inserirCliente (self, nome, dataCompleta, email, senha, palavra_chave):
        self.membro = (Cliente (nome, dataCompleta, email, senha, palavra_chave))
        cursor.execute (f"INSERT INTO cadastro (nome, data_de_aniversario, matricula, email, senha, palavra_chave) VALUES (?, ?, ?, ?, ?, ?)", (nome, self.membro.idade, self.membro.matricula, email, senha, palavra_chave))
        conexao.commit ()
        print(f"Membro: {self.membro.nome} \nData de nascimento: {self.membro.data} \nIdade: {self.membro.idade} \nMatr??cula: {self.membro.matricula} \nE-mail: {self.membro.email} \nSenha: {len (self.membro.senha) * '*'}")

    def inserirLivros (self, titulo, autor, quantidade, genero, faixa_etaria, npaginas, data_de_edicao):
        self.livros.append (Livro (titulo, autor, quantidade, genero, faixa_etaria, npaginas, data_de_edicao))
        cursor.execute (f"INSERT INTO livros_na_estante (titulo, autor, quantidade, genero, faixa_etaria, npaginas, data_de_edicao) VALUES (?, ?, ?, ?, ?, ?, ?)", (titulo, autor, quantidade, genero, faixa_etaria, npaginas, data_de_edicao))
        conexao.commit ()
    def printarLivros (self):
        for i in self.livros:
            print (f"Livro: {i.titulo} \nAutor: {i.autor} \nQuantidade dispon??vel: {i.quantidade_disponivel} \nG??nero: {i.genero} \nFaixa Et??ria: {i.faixa_etaria} \nN??mero de p??ginas: {i.npaginas} \nData de publica????o da edi????o: {i.data_de_edicao}")

    def emprestarLivro (self):

        '''Verifica????o se tem livros para emrestar
        Se tiver: diminuir 1 de livro disponivel
        se nao: n??o ?? possivel emprestar'''

        '''Inserir na tabela de livros emprestados o clienmte que pegou e o titulo do livro
        
        Deposi fazer uma fun????o para devolver o livro:
        deletando o livro da tabela livros emprestados com select e where matricula
        '''