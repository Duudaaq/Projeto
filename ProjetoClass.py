# from abc import ABC, abstractmethod 
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
    def __init__ (self, nome, dataAniversario) -> None:
        self.nome = nome
        self.dataAniversario = dataAniversario

    # @abstractmethod
    # def dataNascimento (self, idade):
    #     pass

class Cliente (Pessoa):
    def __init__ (self, nome, dataAniversario, email, senha) -> None:
        super().__init__ (nome, dataAniversario)
        self.email = email
        self.senha = senha

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
    def inserirCliente(self, nome, dataAniversario, email, senha):
        self.membro.append (Cliente (nome, dataAniversario, email, senha))
    def printarClientes(self):
        for i in self.membro:
            print(f"Membro: {i.nome} \nIdade: {i.dataAniversario}")
    def inserirLivros (self, nomeLivro, autor, dataPublicar, faixaEt):
        self.livros.append (Livro (nomeLivro, autor, dataPublicar, faixaEt))
    def printarLivros (self):
        for i in self.livros:
            print (f"Livro: {i.nomeLivro} \nAutor: {i.autor} \nAno de publicação: {i.dataPublicar} \nClassificação etária: {i.faixaEt}")
    def emprestarLivro (self, valor):
        
