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
    print ("[3] Exit")
    escolha = input (">> ")

    if escolha == "1":
        while True:
            print ()
            print ("[1] Login")
            print ("[2] Cadastre-se")
            print ("[3] Esqueceu sua senha?")
            print ("[4] Voltar")
            loginOption = input (">> ")

            if loginOption == "1":
                print ()
                bio = Biblioteca ()
                bio.loginCliente ()
                while True:
                    print ()
                    print ("[1] Emprestar novo livro")
                    print ("[2] Ver livros emprestados")
                    print ("[3] Devolver livro(s) emprestado(s)")
                    print ("[4] Sair da conta")
                    logon = input (">> ")

                    if logon == "1":
                        print ()
                        sleep (2)
                        bio.printarLivros ()
                        bio.emprestarLivro ()
                        print()
                        print ("Mais alguma coisa?")
                        print ("[1] Sim")
                        print ("[2] Não")
                        mais = input (">> ")
                        if mais == "1":
                            continue
                        else:
                            break
                                                                        
                    elif logon == "2":
                        print()
                        bio.verLivroEmprestado ()
                        sleep (2)
                        continue
                    elif logon == "3":
                        pass

                    elif logon == "4":
                        break

                    else:
                        print ("Opção incorreta!")
                        continue
                    continue

            elif loginOption == "2":
                print ()
                nome = input ("Digite seu nome completo: \n")
                print()
                print ("Digite sua data de nascimento:")
                while True:
                    data = input ("(Apenas números.) \n")
                    if not data.isdigit():
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
                print ()
                bio = Biblioteca ()
                bio.inserirCliente (nome.title(), data, email, senha)
                
                sleep (2)
                print ()
                print ("Cadastro realizado com sucesso!")
                continue

            elif loginOption == "3":

                recuperar = Biblioteca ()
                recuperar.recuperarSenha ()
                break

            elif loginOption == "4":
                break

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
            bio = Biblioteca ()
            bio.printarLivros ()
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

            bio.printarLivros ()
            break

        elif livroOption == "3":
            continue
        else:
            print ("Opção incorreta!")
            continue

    elif escolha == "3":
        break

    else:
        print ("Opção incorreta.")
    
cursor.close()
conexao.close ()