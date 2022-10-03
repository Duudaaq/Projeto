print('''

     Bem vindo
     
        a
        
biblioteca Livrinho Bom

''')
import datetime       
import sqlite3
import random
# livros = sqlite3.connect()
# cursor = livros.cursor()

print("O que você deseja fazer hoje?\n")
print("[1] Acessar conta.")
print("[2] Cadastro.")
deseja = input("")
print ()

if deseja == "1":
    matricula = input ("Digite sua matricula.\n")
    senha = input ("Digite sua senha.\n")
    #falta ainda colocar s/n upgrade(se não tiver, perguntar se deseja ter), limite de livros, datas.
    
elif deseja == "2":
    print()
    print(
    '''Oiii
        
Seja muito bem vindo *-*
    
Vamos começar seu cadastro''')
    print()
    matricula = ""
    ano = datetime.date.today()
    cont = random.randint(10,99)
    f = random.randint(10,99)
    cont += 1
    print(f"Sua matrícula é {ano.year}.{f}{cont}")
    
    
    
    
    