# from abc import ABC, abstractmethod 
from datetime import date

class Pessoa:
    def __init__ (self, nome, dataAniversario) -> None:
        self.nome = nome
        self.dataAniversario = dataAniversario

    # @abstractmethod
    # def dataNascimento (self, idade):
    #     pass

class Cliente (Pessoa):
    def __init__ (self, nome, dataAniversario) -> None:
        super().__init__ (nome, dataAniversario)
    

class Biblioteca:
    def __init__(self) -> None:
        self.membro = []
    def inserirCliente(self, nome, dataAniversario):
        self.membro.append (Cliente (nome, dataAniversario))
    def printarClientes(self):
        for i in self.membro:
            print(f"Membro: {i.nome} \nIdade: {i.dataAniversario}")


nome = input ("Nome. \n")
idade = int (input ("Idade. \n"))

cliente = Biblioteca ()

cliente.inserirCliente (nome.title(), idade)

cliente.printarClientes()

print 