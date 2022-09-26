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
    def emprestarLivro ():
        pass

print ()
simbolo = "✿ " * 25
texto = "✿   Bem vindo(a) á biblioteca Livrinho Bom!!!   ✿"
print (simbolo)
print (texto.center(50))
print (simbolo)

while True:
    print ()
    print ("[1] Acessar Biblioteca")
    print ("[2] Nosso Acervo")
    escolha = input (">> ")

    if escolha == "1":
        print ()
        print ("[1] Login")
        print ("[2] Cadastre-se")
        print ("[3] Esqueceu sua senha?")
        print ("[4] Voltar")

        option = input (">> ")
        if option == "1":
            email = input ("Digite seu e-mail:")
            senha = input ("Digite sua senha:")

        elif option == "2":
            print ()
            nome = input ("Digite seu nome completo: \n")
            while True:
                idade = input ("Digite sua data de nascimento: \n")
                if not idade.isdigit():
                    print ("Digite apenas números.")
                    continue
                email = input ("Digite seu e-mail: \n")
                print ()
                print ("Sua senha deve ter ao menos 8 dígitos, pelo menos 1 letra maiúscula e 1 caracter especial!")
                print ("Digite uma senha válida:")
                senha = input (">> ")

                bio = Biblioteca ()
                bio.inserirCliente (nome.title(), idade, email, senha)
                
                sleep (2)
                print ()
                print ("Cadastro realizado com sucesso!")
                print ()
                break
            break

        elif option == "3":
            pass
        
        elif option == "4":
            continue

        else:
            print ("Opção incorreta!")
            continue

    elif escolha == "2":
        bio = Biblioteca()
        bio.printarLivros()

    else:
        print ("Opçao incorreta!")
        continue

# bio = Biblioteca ()

# bio.inserirCliente (nome.title(), idade)

# livro = input ("Nome do livro: \n")
# autor = input ("Autor: \n")
# data = int (input ("Data de publicação: \n"))
# faixa = int (input ("Classificação etária: \n"))

# bio.inserirLivros (livro.title(), autor.title(), data, faixa)

# print()
# bio.printarClientes()
# print()
# bio.printarLivros()