# import sqlite3

# conexao = sqlite3.connect ("")
# cursor = conexao.cursor ()

class Pessoa:
    def __init__(self, nome, dataAniversario) -> None:
        self.__nome = nome
        self.__dataAniversario = dataAniversario

    @property
    def nome (self):
        return self.__nome

    @property
    def dataAniversario (self):
        return self.__dataAniversario
        
class Cliente (Pessoa):
    def __init__(self, nome, dataAniversario, matricula, email, senha) -> None:
        super().__init__(nome, dataAniversario)

class Biblioteca:
    def __init__(self) -> None:
        self.biblioteca = []
    def inserirCliente (self, cliente):
         self.biblioteca.append (cliente)
    def printarClientes (self):
        for i in self.biblioteca:
            print (f"nome: {i.nome}")
            print (f"Data: {i.dataAniversario}")
            # print (f"Matricula: {i.matricula}")
            # print (f"Email: {i.email}")
            # print (f"Senha: {i.senha}")

nome = input ("Digite seu nome. \n")
idade = int (input ("Digite seu ano de nascimento. \n"))
matricula = int (input ("Digite sua matricula. \n"))
email = input ("Digite seu email. \n")
senha = input ("Digite sua senha. \n")

b = Cliente (nome.title(), idade, matricula, email, senha)

c = Biblioteca ()

c.inserirCliente(b)

c.printarClientes()

# cursor.close ()
# conexao.close ()