from abc import ABC, abstractmethod 
import re
from datetime import date
import time
from time import sleep
import sys

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
        print (listaData)
        dia = int (f"{listaData.pop(0)}{listaData.pop(0)}")
        mes = int (f"{listaData.pop(0)}{listaData.pop(0)}")
        ano = int (f"{listaData.pop(0)}{listaData.pop(0)}{listaData.pop(0)}{listaData.pop(0)}")
        dataCompleta = f"{dia}/{mes}/{ano}"
        idade = self.dataNascimento (date (ano, mes, dia))
        print (dataCompleta)
        return idade

class Cliente (Pessoa):
    def __init__ (self, nome, dataCompleta, email, senha) -> None:
        super().__init__ (nome)
        self.email = email
        self.senha = senha
        self.dataCompleta = dataCompleta
        self.idade = self.calculadora(self.dataCompleta)
class Livro:
    def __init__(self, nomeLivro, autor, dataPublicar,faixaEt) -> None:
        self.nomeLivro = nomeLivro
        self.autor = autor
        self.dataPublicar = dataPublicar
        self.faixaEt = faixaEt

class Biblioteca:
    def __init__(self) -> None:
        self.membro = []
        self.livros = []
    def inserirCliente(self, nome, dataCompleta, email, senha):
        self.membro.append (Cliente (nome, dataCompleta, email, senha))
    def printarClientes(self):
        for i in self.membro:
            print(f"Membro: {i.nome} \nIdade: {i.idade} \nData de Nascimento: {i.dataCompleta}")
    def inserirLivros (self, nomeLivro, autor, dataPublicar, faixaEt):
        self.livros.append (Livro (nomeLivro, autor, dataPublicar, faixaEt))
    def printarLivros (self):
        for i in self.livros:
            print (f"Livro: {i.nomeLivro} \nAutor: {i.autor} \nAno de publicação: {i.dataPublicar} \nClassificação etária: {i.faixaEt}")
    def emprestarLivro (self, valor):
        pass