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

    match escolha:
        case "1":
            while True:
                print ()
                print ("[1] Login")
                print ("[2] Cadastre-se")
                print ("[3] Esqueceu sua senha?")
                print ("[4] Voltar")
                loginOption = input (">> ")

                match loginOption:
                    case "1":
                        print ()
                        bio = Biblioteca ()
                        bio.loginCliente ()
                        while True:
                            print ()
                            print ("[1] Emprestar novo livro")
                            print ("[2] Ver livros emprestados")
                            print ("[3] Devolver livro(s) emprestado(s)")
                            print ("[4] Sair da conta")
                            print ("[5] Deletar sua conta")
                            logon = input (">> ")

                            match logon:
                                case "1":
                                    
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
                                                                                    
                                case "2":
                                    bio.verLivroEmprestado ()
                                    continue

                                case "3":
                                    bio.devolverLivro ()

                                case "4":
                                    break

                                case "5":
                                    bio.deletarConta()
                                    break
                                case _:
                                    print ("Opção incorreta!")
                                    continue
                            continue

                    case "2":
                        bio = Biblioteca ()
                        bio.inserirCliente ()
                        continue

                    case "3":
                        bio.recuperarSenha ()
                        break

                    case "4":
                        break

                    case _:
                        print ("Opção incorreta!")
                        continue

        case "2":
            print ()
            print ("[1] Ver acervo")
            print ("[2] Cadastrar novo livro")
            print ("[3] Voltar")
            livroOption = input (">> ")

            match livroOption:
                case "1":
                    bio = Biblioteca ()
                    bio.printarLivros ()
                    continue

                case "2":
                    bio.inserirLivros ()
                    bio.printarLivros ()
                    continue

                case "3":
                    continue
                case _:
                    print ("Opção incorreta!")
                    continue

        case "3":
            break

        case _:
            print ("Opção incorreta.")
    
cursor.close()
conexao.close ()