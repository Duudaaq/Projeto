import sqlite3
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

def escrever (texto):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush ()
        time.sleep (0.02)

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

    def data_Completa (self, data):
        datalist = []
        for i in data:
            datalist.append (i)
        for i in range (len (datalist)):
            if i == 2:
                datalist [2] = '/' + datalist [2]
            if i == 4:
                datalist [4] = '/' + datalist [4]
        data = ''.join (datalist)
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
        cont = random.randint (0000, 9999)
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

    def inserirCliente (self):
        print ()
        while True:
            nome = input ("Digite seu nome completo: \n")
            if not nome.isalpha ():
                print ("Utilize apenas letras para seu nome!")
                continue
            else:
                break
        print()
        print ("Digite sua data de nascimento:")
        while True:
            dataCompleta = input ("(Apenas números.) \n")
            if not dataCompleta.isdigit():
                continue
            else:
                break
        print ()
        email = input ("Digite seu e-mail: \n")
        print ()
        print ("Sua senha deve ter ao menos 8 caracteres, 1 número, 1 caractere maiúsculo e 1 caractere especial.")
        while True:
            senha = input ("Digite sua senha: \n")
            if len (senha) < 7:
                print ("A senha deve ter ao menos 8 caracteres:")
            elif senha.islower():
                print ("A senha deve ter ao menos 1 caractere maiúsculo:")
            elif senha.isalpha():
                print ("A senha deve ter ao menos 1 número:")
            elif senha.isalnum():
                print ("A senha deve ter ao menos 1 caractere especial:")
            else:
                break
        sleep (2)
        print ()
        print ("Cadastro realizado com sucesso!")
        print ()
        self.membro = (Cliente (nome.title(), dataCompleta, email, senha))
        cursor.execute (f"INSERT INTO cadastro (nome, idade, matricula, email, senha) VALUES (?, ?, ?, ?, ?)", (nome.title(), self.membro.idade, self.membro.matricula, email, senha))
        conexao.commit ()
        print (f"Membro: {self.membro.nome} \nData de nascimento: {self.membro.data} \nIdade: {self.membro.idade} \nMatrícula: {self.membro.matricula} \nE-mail: {self.membro.email} \nSenha: {len (self.membro.senha) * '*'}")

    def loginCliente (self):
        while True:
            matricula_login = input ("Matrícula: \n")
            senha_login = input ("Senha: \n")
            
            cursor.execute (f"SELECT matricula FROM cadastro WHERE matricula = '{matricula_login}'")
            listaMatricula = []
            for matricula_for in cursor.fetchall():
                listaMatricula = matricula_for [0]

            cursor.execute (f"SELECT senha FROM cadastro WHERE senha = '{senha_login}'")
            listaSenha = []
            for senha_for in cursor.fetchall():
                listaSenha = senha_for [0]
            
            if matricula_login in listaMatricula and senha_login in listaSenha:
                break
            else:
                print ("Matrícula ou senha incorretas.")
                continue
            
    def recuperarSenha (self):
        print ()
        matricula_esqueceu = input ("Digite sua matrícula: \n")
        email_esqueceu = input ("Digite seu e-mail: \n")

        cursor.execute (f"SELECT matricula FROM cadastro WHERE matricula = '{matricula_esqueceu}'")
        for matricula_for in cursor.fetchall():
            pass

        cursor.execute (f"SELECT email FROM cadastro WHERE email = '{email_esqueceu}'")
        for email_for in cursor.fetchall():
            pass
                                    
        if matricula_esqueceu in matricula_for and email_esqueceu in email_for:
            while True:
                print ()
                senha_nova = input ("Digite sua nova senha: \n")
                if len (senha_nova) < 7:
                    print ("A senha deve ter ao menos 8 caracteres:")
                elif senha_nova.islower():
                    print ("A senha deve ter ao menos 1 caractere maiúsculo:")
                elif senha_nova.isalpha():
                    print ("A senha deve ter ao menos 1 número:")
                elif senha_nova.isalnum():
                    print ("A senha deve ter ao menos 1 caractere especial:")
                else:
                    break
            cursor.execute (f"UPDATE cadastro SET senha = ? WHERE matricula = '{matricula_esqueceu}'", (senha_nova,))
            conexao.commit ()
            print ()
            sleep (1)
            print ("Sua senha foi alterada com sucesso!")

        else:
            print ("Matrícula ou senha incorretos.")

    def inserirLivros (self):
        print ()
        titulo = input ("Digite o título do livro: \n")
        autor = input ("Digite o nome do autor: \n")
        quantidade_disponivel = int (input ("Quantidade de exemplares disponíveis: \n"))
        genero = input ("Á que gênero pertecence o seu livro: \n")
        faixa_etaria = input ("Faixa etária do livro: \n")
        npaginas = int (input ("Número de páginas: \n"))
        data_de_edicao = input ("Data de publicação dessa edição: \n")
        print ()

        self.livros.append (Livro (titulo.title(), autor, quantidade_disponivel, genero, faixa_etaria, npaginas, data_de_edicao))
        cursor.execute (f"INSERT INTO livros_na_estante (titulo, autor, quantidade_disponivel, genero, faixa_etaria, npaginas, data_de_edicao) VALUES (?, ?, ?, ?, ?, ?, ?)", (titulo, autor, quantidade_disponivel, genero, faixa_etaria, npaginas, data_de_edicao))
        conexao.commit ()
        sleep (2)
        print ()
        print ("Cadastro realizado com sucesso!")
        print ()

    def printarLivros (self):
        cursor.execute (f"SELECT * FROM livros_na_estante WHERE quantidade_disponivel > 0")
        print ("Livros disponíveis:")
        print()
        contador = 0
        for i in cursor.fetchall():
            contador += 1
            print (f"{contador} - {i [1]}")
            print (f"Quantidade disponível: {i [3]}")

    def printarPesquisar(self):
        print ()
        print ("[1] Nome")
        print ("[2] Autor")
        print ("[3] Gênero")
        print ()
        while True: 
            pesquisa = input ("Como você desja fazer sua pesquisa?\n")
            print()

            if pesquisa == "1":
                titulo = input ("Digite o nome.\n")
                cursor.execute (f"SELECT * FROM livros_na_estante WHERE titulo LIKE '%{titulo}%' OR titulo LIKE '%{titulo}%'")
                for i in cursor.fetchall():
                    print(i [1])
                break
            elif pesquisa == "2":
                autor = input ("Digite o autor.\n")
                cursor.execute (f"SELECT * FROM livros_na_estante WHERE autor LIKE '%{autor}%' OR titulo LIKE '%{autor}%'")
                for i in cursor.fetchall():
                    print(i [1])
                break
            elif pesquisa == "3":
                genero = input ("Digite o gênero.\n")
                cursor.execute (f"SELECT * FROM livros_na_estante WHERE genero LIKE '%{genero}%' OR genero LIKE '%{genero}%'")
                for i in cursor.fetchall():
                    print(i [1])
                break
            else:
                pass

    def emprestarLivro (self):
        matricula_verifica = input ("Digite sua matrícula novamente: \n")
        cursor.execute (f"SELECT * FROM cadastro WHERE matricula = '{matricula_verifica}'")
        for idade_i in cursor.fetchall ():
            pass

        if int (idade_i [4]) <= 10:
            cursor.execute (f"SELECT * FROM livros_na_estante WHERE faixa_etaria <= '10'")
            print ("Livros disponíveis:")
            print()
            contador = 0
            for i in cursor.fetchall():
                contador += 1
                print (f"{contador} - {i [1]}")
                print (f"Quantidade disponível: {i [3]}")

            print ()
            livro_emprestado = input ("Que livro deseja emprestar? \n")
            print ()
            cursor.execute (f"SELECT titulo FROM livros_na_estante WHERE titulo = '{livro_emprestado}'")
            listaLivro = []
            for livro_i in cursor.fetchall():
                listaLivro = livro_i [0]
            if livro_emprestado in listaLivro:
                senha_verifica = input ("Digite sua senha novamente: \n")
                cursor.execute (f"SELECT matricula, senha FROM cadastro")
                for matricula_i in cursor.fetchall():
                    pass
                if matricula_verifica in matricula_i and senha_verifica in matricula_i:
                    cursor.execute (f"SELECT * FROM cadastro WHERE matricula = '{matricula_verifica}'")
                    for nome_i in cursor.fetchall ():
                        pass
                    cursor.execute (f"INSERT INTO livros_emprestados (matricula, cliente, titulo) VALUES (?,?,?)", (matricula_verifica, nome_i[3], livro_emprestado))
                    conexao.commit ()
                    cursor.execute (f"SELECT titulo, quantidade_disponivel, autor FROM livros_na_estante WHERE titulo = '{livro_emprestado}'")
                    for i in cursor.fetchall():
                        titulo, y, autor = i
                        cursor.execute (f"UPDATE livros_na_estante SET quantidade_disponivel = ? WHERE titulo = '{titulo}' and autor = '{autor}'", (y-1,))
                        conexao.commit ()
                    print ()
                    print (f'Livro "{livro_emprestado}" emprestado para você.')
                else:
                    print ("Matrícula ou senha incorretos. Livro não foi emprestado.")
            else:
                print ("Livro não encontrando.")

        elif int (idade_i [4]) <= 11:
            cursor.execute (f"SELECT * FROM livros_na_estante WHERE faixa_etaria <= '11'")
            print ("Livros disponíveis:")
            print()
            contador = 0
            for i in cursor.fetchall():
                contador += 1
                print (f"{contador} - {i [1]}")
                print (f"Quantidade disponível: {i [3]}")

            print ()
            livro_emprestado = input ("Que livro deseja emprestar? \n")
            print ()
            cursor.execute (f"SELECT titulo FROM livros_na_estante WHERE titulo = '{livro_emprestado}'")
            listaLivro = []
            for livro_i in cursor.fetchall():
                listaLivro = livro_i [0]
            if livro_emprestado in listaLivro:
                senha_verifica = input ("Digite sua senha novamente: \n")

                cursor.execute (f"SELECT matricula, senha FROM cadastro")
                for matricula_i in cursor.fetchall():
                    pass
                if matricula_verifica in matricula_i and senha_verifica in matricula_i:
                    cursor.execute (f"SELECT * FROM cadastro WHERE matricula = '{matricula_verifica}'")
                    for nome_i in cursor.fetchall ():
                        pass
                    cursor.execute (f"INSERT INTO livros_emprestados (matricula, cliente, titulo) VALUES (?,?,?)", (matricula_verifica, nome_i[3], livro_emprestado))
                    conexao.commit ()
                    cursor.execute (f"SELECT titulo, quantidade_disponivel, autor FROM livros_na_estante WHERE titulo = '{livro_emprestado}'")
                    for i in cursor.fetchall():
                        titulo, y, autor = i
                        cursor.execute (f"UPDATE livros_na_estante SET quantidade_disponivel = ? WHERE titulo = '{titulo}' and autor = '{autor}'", (y-1,))
                        conexao.commit ()
                    print ()
                    print (f'Livro "{livro_emprestado}" emprestado para você.')
                else:
                    print ("Matrícula ou senha incorretos. Livro não foi emprestado.")
            else:
                print ("Livro não encontrando.")

        elif int (idade_i [4]) <= 12:
            cursor.execute (f"SELECT * FROM livros_na_estante WHERE faixa_etaria <= '12'")
            print ("Livros disponíveis:")
            print()
            contador = 0
            for i in cursor.fetchall():
                contador += 1
                print (f"{contador} - {i [1]}")
                print (f"Quantidade disponível: {i [3]}")

            print ()
            livro_emprestado = input ("Que livro deseja emprestar? \n")
            print ()
            cursor.execute (f"SELECT titulo FROM livros_na_estante WHERE titulo = '{livro_emprestado}'")
            listaLivro = []
            for livro_i in cursor.fetchall():
                listaLivro = livro_i [0]
            if livro_emprestado in listaLivro:
                senha_verifica = input ("Digite sua senha novamente: \n")

                cursor.execute (f"SELECT matricula, senha FROM cadastro")
                for matricula_i in cursor.fetchall():
                    pass
                if matricula_verifica in matricula_i and senha_verifica in matricula_i:
                    cursor.execute (f"SELECT * FROM cadastro WHERE matricula = '{matricula_verifica}'")
                    for nome_i in cursor.fetchall ():
                        pass
                    cursor.execute (f"INSERT INTO livros_emprestados (matricula, cliente, titulo) VALUES (?,?,?)", (matricula_verifica, nome_i[3], livro_emprestado))
                    conexao.commit ()
                    cursor.execute (f"SELECT titulo, quantidade_disponivel, autor FROM livros_na_estante WHERE titulo = '{livro_emprestado}'")
                    for i in cursor.fetchall():
                        titulo, y, autor = i
                        cursor.execute (f"UPDATE livros_na_estante SET quantidade_disponivel = ? WHERE titulo = '{titulo}' and autor = '{autor}'", (y-1,))
                        conexao.commit ()
                    print ()
                    print (f'Livro "{livro_emprestado}" emprestado para você.')
                else:
                    print ("Matrícula ou senha incorretos. Livro não foi emprestado.")
            else:
                print ("Livro não encontrando.")

        elif int (idade_i [4]) <= 13:
            cursor.execute (f"SELECT * FROM livros_na_estante WHERE faixa_etaria <= '13'")
            print ("Livros disponíveis:")
            print()
            contador = 0
            for i in cursor.fetchall():
                contador += 1
                print (f"{contador} - {i [1]}")
                print (f"Quantidade disponível: {i [3]}")

            print ()
            livro_emprestado = input ("Que livro deseja emprestar? \n")
            print ()
            cursor.execute (f"SELECT titulo FROM livros_na_estante WHERE titulo = '{livro_emprestado}'")
            listaLivro = []
            for livro_i in cursor.fetchall():
                listaLivro = livro_i [0]
            if livro_emprestado in listaLivro:
                senha_verifica = input ("Digite sua senha novamente: \n")

                cursor.execute (f"SELECT matricula, senha FROM cadastro")
                for matricula_i in cursor.fetchall():
                    pass
                if matricula_verifica in matricula_i and senha_verifica in matricula_i:
                    cursor.execute (f"SELECT * FROM cadastro WHERE matricula = '{matricula_verifica}'")
                    for nome_i in cursor.fetchall ():
                        pass
                    cursor.execute (f"INSERT INTO livros_emprestados (matricula, cliente, titulo) VALUES (?,?,?)", (matricula_verifica, nome_i[3], livro_emprestado))
                    conexao.commit ()
                    cursor.execute (f"SELECT titulo, quantidade_disponivel, autor FROM livros_na_estante WHERE titulo = '{livro_emprestado}'")
                    for i in cursor.fetchall():
                        titulo, y, autor = i
                        cursor.execute (f"UPDATE livros_na_estante SET quantidade_disponivel = ? WHERE titulo = '{titulo}' and autor = '{autor}'", (y-1,))
                        conexao.commit ()
                    print ()
                    print (f'Livro "{livro_emprestado}" emprestado para você.')
                else:
                    print ("Matrícula ou senha incorretos. Livro não foi emprestado.")
            else:
                print ("Livro não encontrando.")

        elif int (idade_i [4]) <= 14:
            cursor.execute (f"SELECT * FROM livros_na_estante WHERE faixa_etaria <= '14'")
            print ("Livros disponíveis:")
            print()
            contador = 0
            for i in cursor.fetchall():
                contador += 1
                print (f"{contador} - {i [1]}")
                print (f"Quantidade disponível: {i [3]}")

            print ()
            livro_emprestado = input ("Que livro deseja emprestar? \n")
            print ()
            cursor.execute (f"SELECT titulo FROM livros_na_estante WHERE titulo = '{livro_emprestado}'")
            listaLivro = []
            for livro_i in cursor.fetchall():
                listaLivro = livro_i [0]
            if livro_emprestado in listaLivro:
                senha_verifica = input ("Digite sua senha novamente: \n")

                cursor.execute (f"SELECT matricula, senha FROM cadastro")
                for matricula_i in cursor.fetchall():
                    pass
                if matricula_verifica in matricula_i and senha_verifica in matricula_i:
                    cursor.execute (f"SELECT * FROM cadastro WHERE matricula = '{matricula_verifica}'")
                    for nome_i in cursor.fetchall ():
                        pass
                    cursor.execute (f"INSERT INTO livros_emprestados (matricula, cliente, titulo) VALUES (?,?,?)", (matricula_verifica, nome_i[3], livro_emprestado))
                    conexao.commit ()
                    cursor.execute (f"SELECT titulo, quantidade_disponivel, autor FROM livros_na_estante WHERE titulo = '{livro_emprestado}'")
                    for i in cursor.fetchall():
                        titulo, y, autor = i
                        cursor.execute (f"UPDATE livros_na_estante SET quantidade_disponivel = ? WHERE titulo = '{titulo}' and autor = '{autor}'", (y-1,))
                        conexao.commit ()
                    print ()
                    print (f'Livro "{livro_emprestado}" emprestado para você.')
                else:
                    print ("Matrícula ou senha incorretos. Livro não foi emprestado.")
            else:
                print ("Livro não encontrando.")

        elif int (idade_i [4]) <= 15:
            cursor.execute (f"SELECT * FROM livros_na_estante WHERE faixa_etaria <= '15'")
            print ("Livros disponíveis:")
            print()
            contador = 0
            for i in cursor.fetchall():
                contador += 1
                print (f"{contador} - {i [1]}")
                print (f"Quantidade disponível: {i [3]}")

            print ()
            livro_emprestado = input ("Que livro deseja emprestar? \n")
            print ()
            cursor.execute (f"SELECT titulo FROM livros_na_estante WHERE titulo = '{livro_emprestado}'")
            listaLivro = []
            for livro_i in cursor.fetchall():
                listaLivro = livro_i [0]
            if livro_emprestado in listaLivro:
                senha_verifica = input ("Digite sua senha novamente: \n")

                cursor.execute (f"SELECT matricula, senha FROM cadastro")
                for matricula_i in cursor.fetchall():
                    pass
                if matricula_verifica in matricula_i and senha_verifica in matricula_i:
                    cursor.execute (f"SELECT * FROM cadastro WHERE matricula = '{matricula_verifica}'")
                    for nome_i in cursor.fetchall ():
                        pass
                    cursor.execute (f"INSERT INTO livros_emprestados (matricula, cliente, titulo) VALUES (?,?,?)", (matricula_verifica, nome_i[3], livro_emprestado))
                    conexao.commit ()
                    cursor.execute (f"SELECT titulo, quantidade_disponivel, autor FROM livros_na_estante WHERE titulo = '{livro_emprestado}'")
                    for i in cursor.fetchall():
                        titulo, y, autor = i
                        cursor.execute (f"UPDATE livros_na_estante SET quantidade_disponivel = ? WHERE titulo = '{titulo}' and autor = '{autor}'", (y-1,))
                        conexao.commit ()
                    print ()
                    print (f'Livro "{livro_emprestado}" emprestado para você.')
                else:
                    print ("Matrícula ou senha incorretos. Livro não foi emprestado.")
            else:
                print ("Livro não encontrando.")

        elif int (idade_i [4]) <= 16:
            cursor.execute (f"SELECT * FROM livros_na_estante WHERE faixa_etaria <= '16'")
            print ("Livros disponíveis:")
            print()
            contador = 0
            for i in cursor.fetchall():
                contador += 1
                print (f"{contador} - {i [1]}")
                print (f"Quantidade disponível: {i [3]}")

            print ()
            livro_emprestado = input ("Que livro deseja emprestar? \n")
            print ()
            cursor.execute (f"SELECT titulo FROM livros_na_estante WHERE titulo = '{livro_emprestado}'")
            listaLivro = []
            for livro_i in cursor.fetchall():
                listaLivro = livro_i [0]
            if livro_emprestado in listaLivro:
                senha_verifica = input ("Digite sua senha novamente: \n")

                cursor.execute (f"SELECT matricula, senha FROM cadastro")
                for matricula_i in cursor.fetchall():
                    pass
                if matricula_verifica in matricula_i and senha_verifica in matricula_i:
                    cursor.execute (f"SELECT * FROM cadastro WHERE matricula = '{matricula_verifica}'")
                    for nome_i in cursor.fetchall ():
                        pass
                    cursor.execute (f"INSERT INTO livros_emprestados (matricula, cliente, titulo) VALUES (?,?,?)", (matricula_verifica, nome_i[3], livro_emprestado))
                    conexao.commit ()
                    cursor.execute (f"SELECT titulo, quantidade_disponivel, autor FROM livros_na_estante WHERE titulo = '{livro_emprestado}'")
                    for i in cursor.fetchall():
                        titulo, y, autor = i
                        cursor.execute (f"UPDATE livros_na_estante SET quantidade_disponivel = ? WHERE titulo = '{titulo}' and autor = '{autor}'", (y-1,))
                        conexao.commit ()
                    print ()
                    print (f'Livro "{livro_emprestado}" emprestado para você.')
                else:
                    print ("Matrícula ou senha incorretos. Livro não foi emprestado.")
            else:
                print ("Livro não encontrando.")

        else:
            cursor.execute (f"SELECT * FROM livros_na_estante WHERE quantidade_disponivel > 0")
            print ("Livros disponíveis:")
            print()
            contador = 0
            for i in cursor.fetchall():
                contador += 1
                print (f"{contador} - {i [1]}")
                print (f"Quantidade disponível: {i [3]}")
            print ()

            livro_emprestado = input ("Que livro deseja emprestar? \n")
            print ()
            cursor.execute (f"SELECT titulo FROM livros_na_estante WHERE titulo = '{livro_emprestado}'")
            listaLivro = []
            for livro_i in cursor.fetchall():
                listaLivro = livro_i [0]
            if livro_emprestado in listaLivro:
                senha_verifica = input ("Digite sua senha novamente: \n")

                cursor.execute (f"SELECT matricula, senha FROM cadastro")
                for matricula_i in cursor.fetchall():
                    pass
                if matricula_verifica in matricula_i and senha_verifica in matricula_i:
                    cursor.execute (f"SELECT * FROM cadastro WHERE matricula = '{matricula_verifica}'")
                    for nome_i in cursor.fetchall ():
                        pass
                    cursor.execute (f"INSERT INTO livros_emprestados (matricula, cliente, titulo) VALUES (?,?,?)", (matricula_verifica, nome_i[3], livro_emprestado))
                    conexao.commit ()
                    cursor.execute (f"SELECT titulo, quantidade_disponivel, autor FROM livros_na_estante WHERE titulo = '{livro_emprestado}'")
                    for i in cursor.fetchall():
                        titulo, y, autor = i
                        cursor.execute (f"UPDATE livros_na_estante SET quantidade_disponivel = ? WHERE titulo = '{titulo}' and autor = '{autor}'", (y-1,))
                        conexao.commit ()
                    print ()
                    print (f'Livro "{livro_emprestado}" emprestado para você.')
                else:
                    print ("Matrícula ou senha incorretos. Livro não foi emprestado.")
            else:
                print ("Livro não encontrando.")

    def verLivroEmprestado (self):
        print()
        while True:
            matricula_verificarLivro = input ("Digite sua matricula novamente: \n")

            cursor.execute (f"SELECT matricula FROM livros_emprestados WHERE matricula = '{matricula_verificarLivro}'")
            for matricula_for in cursor.fetchall():
                pass

            if len (matricula_verificarLivro) == 9:
                cursor.execute (f"SELECT * FROM livros_emprestados WHERE matricula = '{matricula_verificarLivro}'")
                verificar = cursor.fetchall()
                print ()
                if len (verificar) != 0:
                    cursor.execute (f"SELECT * FROM livros_emprestados WHERE matricula = '{matricula_verificarLivro}'")
                    sleep (1)
                    print ("Livros emprestados para você:")
                    sleep (2)
                    for i in cursor.fetchall():
                        print(f"- {i [2]}")
                    break
                else:
                    sleep (1)
                    print ("Nenhum livro emprestado registrado.")
                    sleep (2)
                    break
            else:
                print ("Matricula incorreta.")
                continue

    def devolverLivro (self):
        print()
        while True:
            matricula_verificarLivro = input ("Digite sua matricula novamente: \n")

            cursor.execute (f"SELECT matricula FROM livros_emprestados WHERE matricula = '{matricula_verificarLivro}'")
            for matricula_for in cursor.fetchall():
                pass

            if len (matricula_verificarLivro) == 9:
                cursor.execute (f"SELECT * FROM livros_emprestados WHERE matricula = '{matricula_verificarLivro}'")
                verificar = cursor.fetchall()
                print ()
                if len (verificar) != 0:
                    cursor.execute (f"SELECT * FROM livros_emprestados WHERE matricula = '{matricula_verificarLivro}'")
                    sleep (1)
                    print ("Livros emprestados para você:")
                    sleep (2)
                    for i in cursor.fetchall():
                        print(f"- {i [2]}")
                    print()
                    livro_devolver = input ("Qual destes acima desejas devolver? \n")
                    cursor.execute (f"DELETE FROM livros_emprestados WHERE titulo = '{livro_devolver}'")
                    conexao.commit ()
                    cursor.execute (f"SELECT titulo, quantidade_disponivel, autor FROM livros_na_estante WHERE titulo = '{livro_devolver}'")
                    for i in cursor.fetchall():
                        titulo, y, autor = i
                        cursor.execute (f"UPDATE livros_na_estante SET quantidade_disponivel = ? WHERE titulo = '{titulo}' and autor = '{autor}'", (y + 1,))
                        conexao.commit ()
                    print ()
                    print (f'Livro "{livro_devolver}" devolvido á estante.')
                    break
                else:
                    sleep (1)
                    print ("Nenhum livro emprestado registrado.")
                    sleep (2)
                    break
            else:
                print ("Matricula incorreta.")
                continue

    def deletarConta (self):
        print ()
        while True:
            matricula_deletar = input ("Digite sua matrícula novamente: \n")
            senha_deletar = input ("Digite sua senha novamente: \n")

            cursor.execute (f"SELECT matricula, senha FROM cadastro WHERE matricula = '{matricula_deletar}'")
            for i in cursor.fetchall ():
                if matricula_deletar in i and senha_deletar in i:
                    print ()
                    print ("Tem certeza que deseja excluir sua conta?")
                    print ("[1] Sim")
                    print ("[2] Não")
                    delete = input (">> ")
                    match delete:
                        case "1":
                            cursor.execute (f"SELECT * FROM livros_emprestados WHERE matricula = '{matricula_deletar}'")
                            verificar_livro = cursor.fetchall ()
                            if len (verificar_livro) != 0:
                                print ()
                                print ("Você ainda tem livros á serem devolvidos!")
                                break
                            else:
                                cursor.execute (f"DELETE FROM cadastro WHERE matricula = '{matricula_deletar}'")
                                conexao.commit ()
                                print ()
                                print ("Sua conta foi deletada!")
                                break

                        case "2":
                            print ("Conta não deletada.")
                            break

                        case _:
                            print ("Opção incorreta.")
                            continue

                else:
                    print ("Matrícula ou senha incorreto.")
                    continue
            break