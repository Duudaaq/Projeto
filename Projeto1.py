from ProjetoClass import *
# from abc import ABC, abstractmethod 
from datetime import date
import time
from time import sleep
import sys

print ()
simbolo = "📚 " * 17
texto = "📚   Bem vindo(a) á biblioteca Livrinho Bom!!!  📚"
print (simbolo)
print (texto)
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
        loginOption = input (">> ")

        if loginOption == "1":
            email = input ("Digite seu e-mail:")
            senha = input ("Digite sua senha:")

        elif loginOption == "2":
            print ()
            nome = input ("Digite seu nome completo: \n")
            while True:
                data = input ("Digite sua data de nascimento: \n")
                if not data.isdigit():
                    print ("Digite apenas números.")
                    continue
                email = input ("Digite seu e-mail: \n")
                print ()
                print ("Sua senha deve ter ao menos 8 dígitos, pelo menos 1 letra maiúscula e 1 caracter especial!")
                print ("Digite uma senha válida:")
                senha = input (">> ")
                palavra_chave=input("escreva uma palavra chave para que possamos redefinir sua senha caso precise\nEx:comida favorita\n.\n\nCUIDADO se você esquecer a palavra chave não havera como recuperar a senha\n")
                print ()

                bio = Biblioteca ()
                bio.inserirCliente (nome.title(), data, email, senha)
                
                sleep (2)
                print ()
                print ("Cadastro realizado com sucesso!")
                print ()

                break
            break
#AQUI
        elif loginOption == "3":
            while True :
                print("digite abaixo sua palavra chave para que podemos redefinir sua senha\nEx:sua comida predileta\n se você quiser voltar digite 3")
                verificar_palavra_chave=input(":")
                cursor.execute('SELECT palavra-chave FROM cadastro')#PROBLEMA
                for jabuticaba in cursor.fetchall():                # AQUI
        
                    if verificar_palavra_chave == jabuticaba :
                        print("palavra chave certa\ncrie sua nova senha\n")
                        senha2=input(":")
                        emailCF=input("digite o email dessa conta por favor\n")
                        cursor.execute(f'UPDATE cadastro SET senha = ? WHERE email = {emailCF}',(senha2))
                        conexao.commit()
                        print("senha criada com sucesso\n")
                        pass
                    if verificar_palavra_chave == '3' :
                        print("saindo...\n\n")
                    
                    
                    else:
                        verificar_palavra_chave != jabuticaba 
                        print("essa não é sua palavra chave\npara sair digite 3")
                        continue
                        
        elif loginOption == "4":
            continue

        else:
            print ("Opção incorreta!")
            continue

    elif escolha == "2":
        print ()
        print ("[1] Ver acervo")
        print ("[2] Cadastrar novo livro")
        print ("[3] Voltar")
        livroOption = input (">> ")

        if livroOption == "1":
            bio = Biblioteca()
            bio.printarLivros()
            break

        elif livroOption == "2":
            print ()
            nomeLivro = input ("Digite o título do livro: \n")
            autor = input ("Digite o nome do autor: \n")
            quantidade_disponivel = int (input ("Quantidade de exemplares disponíveis: \n"))
            genero = input ("Á que gênero pertecence o seu livro: \n")
            faixaEt = input ("Faixa etária do livro: \n")
            Npaginas = int (input ("Número de páginas: \n"))
            data_de_edicao = input ("Data de publicação dessa edição: \n")
            print ()

            bio = Biblioteca ()
            bio.inserirLivros (nomeLivro.title(), autor, quantidade_disponivel, genero, faixaEt, Npaginas, data_de_edicao)
            
            sleep (2)
            print ()
            print ("Cadastro realizado com sucesso!")
            print ()

            bio.printarLivros()

            break

        elif livroOption == "3":
            continue
        else:
            print ("Opção incorreta!")
            continue

    else:
        print ("Opçao incorreta!")
        continue
    
cursor.close()
conexao.close ()

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
