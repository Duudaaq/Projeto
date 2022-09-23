# Nome 
# Data de Aniversário
# Matrícula
# E-mail
# Senha

                                                                    #CRIANDO
# nomeV=input("digite seu nome\n")
# dataN=input("digite sua data de nascimento\n")
# matricula=input("digite sua matricula\n")
# email=input("digite seu email\n")
# senha=input("digite uma senha\n")
import sqlite3

conexao = sqlite3.connect('biblioteca.db')
cursor = conexao.cursor()

# cursor.execute('INSERT INTO cadastro (nome,data_de_aniversario,matricula,email) VALUES (?,?,?,?)',(nomeV,dataN,matricula,email))
# conexao.commit()
# cursor.execute('INSERT INTO validacao (email,senha) VALUES (?,?)',(email,senha))
# conexao.commit()

#                                                                #ATUALIZANDO

# emailD=input("digite o seu email atual para podermos atualizar seus dados \n:")
# emailN=input("digite seu novo email\n")
# senhaN=input("digite sua senha nova \n")

# cursor.execute(f'UPDATE cadastro SET email = ? WHERE email = "{emailD}"',(emailN,))
# conexao.commit()
# cursor.execute(f'UPDATE validacao SET email = ?, senha = ? WHERE email ="{emailD}"',(emailN,senhaN))             
# conexao.commit()

                                                                 #DELETAR
indentificacao=str(input("qual o email da conta que você quer deletar?\nCUIDADO AS ALTERAÇÕES SÂO IRREVERSIVEIS\n\n"))
cursor.execute(f'DELETE FROM cadastro WHERE email ="{indentificacao}"')                                            
conexao.commit()
cursor.execute(f'DELETE FROM validacao WHERE email ="{indentificacao}"')
conexao.commit()