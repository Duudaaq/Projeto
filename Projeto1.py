from ProjetoClass import *
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
            bio = Biblioteca ()
            bio.loginCliente ()
            break

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
                palavra_chave = input("escreva uma palavra chave para que possamos usar pra lhe ajudar mais tarde\n")
                print ()

                bio = Biblioteca ()
                bio.inserirCliente (nome.title(), data, email, senha)
                
                sleep (2)
                print ()
                print ("Cadastro realizado com sucesso!")
                print ()

                break
            break

        elif loginOption == "3":

            recuperar = Biblioteca ()
            recuperar.recuperarSenha ()
            break

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
        print ("Opção incorreta!")
        continue
    
cursor.close()
conexao.close ()